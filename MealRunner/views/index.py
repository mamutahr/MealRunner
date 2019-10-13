#!/usr/bin/python
"""
MealRunner index (main) view.

URLs include:
/
"""

import flask
import MealRunner
from MealRunner.views.helper import get_user
from MealRunner.model import get_db


@MealRunner.app.route('/', methods=['GET', 'POST'])
def show_index():
    """Display / route."""
    database = get_db()
    connection = database.cursor()
    if 'username' not in flask.session:
        return flask.redirect(flask.url_for('show_login'))
    user = flask.session['username']
    connection.execute("SELECT * FROM users WHERE username = \'" + user
                       + "\'")
    userInfo = connection.fetchall()[0]
    userType = userInfo['type']
    userName = userInfo['fullname']

    if flask.request.method == 'POST':
        if "makepost" in flask.request.form:
            connection.execute("INSERT INTO REQUESTS(description, giverowner, receiveraccept, driveraccept) \
            VALUES (?, ?, 0, 0)", (flask.request.form["description"], flask.session['username']))
            database.commit()
        if "deletepost" in flask.request.form:
            connection.execute("DELETE FROM REQUESTS WHERE requestid = ?", (flask.request.form["postid"],))
            database.commit()
        if "receivertake" in flask.request.form:
            connection.execute("UPDATE requests SET receiverowner = ?, receiveraccept = 1 \
            WHERE requestid = ?", (user, flask.request.form["postid"]))
            database.commit()
        if "receivergiveback" in flask.request.form:
            connection.execute("UPDATE requests SET receiverowner = NULL, driverowner = NULL, \
            receiveraccept = 0, driveraccept = 0 WHERE requestid = ?", (flask.request.form["postid"],))
            database.commit()
        if "droppedoff" in flask.request.form:
            connection.execute("DELETE FROM requests WHERE requestid = ?", (flask.request.form["postid"],))
            database.commit()
        if "drivertake" in flask.request.form:
            connection.execute("UPDATE requests SET driverowner = ?, driveraccept = 1 \
            WHERE requestid = ?", (user, flask.request.form["postid"]))
            database.commit()
        if "drivergiveback" in flask.request.form:
            connection.execute("UPDATE requests SET driverowner = NULL, driveraccept = 0 \
            WHERE requestid = ?", (flask.request.form["postid"],))
            database.commit()

    connection.execute('SELECT * FROM requests')
    requests = connection.fetchall()
    for (idx, req) in enumerate(requests):
        connection.execute("SELECT address FROM users WHERE username = \'"
                            + req['giverowner'] + "\'")
        fetch = connection.fetchone()
        if fetch:
            requests[idx]['giveraddress'] = fetch['address']
        if req['receiverowner']:
            connection.execute("SELECT address FROM users WHERE username = \'"
                                + req['receiverowner'] + "\'")
            fetch = connection.fetchone()
            if fetch:
                requests[idx]['receiveraddress'] = fetch['address']

    cur = connection.execute("Select count(*) from requests")
    numPosts = connection.fetchone()['count(*)']

    cur = connection.execute("Select count(*) from requests where receiveraccept = 1")
    numRecieverAcceptedPosts = connection.fetchone()['count(*)']

    cur = connection.execute("Select count(*) from requests where driveraccept = 1")
    numDriverAcceptedPosts = connection.fetchone()['count(*)']

    requests.reverse()
    context ={
    	'type': userType,
    	'fullname': userName,
    	'allrequests': requests,
    	'username': user,
        'numPosts': numPosts,
        'numReceiverAccept': numRecieverAcceptedPosts,
        'numDriverAccept': numDriverAcceptedPosts
    }
    return flask.render_template("index.html", **context)
