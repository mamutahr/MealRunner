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


@MealRunner.app.route('/')
def show_index():
    """Display / route."""

    if 'username' not in flask.session:
        return flask.redirect(flask.url_for('show_login'))
    user = flask.session['username']
    connection = get_db().cursor()
    connection.execute("SELECT * FROM users WHERE username = \'" + user
                       + "\'")
    userInfo = connection.fetchall()[0]
    userType = userInfo['type']
    userName = userInfo['fullname']

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

    '''
    if userType == 'Giver':
         WHERE giverowner = \'"+user+"\'")
        connection.fetchall()

    elif userType == 'Receiver':
        connection.execute("SELECT * FROM requests WHERE receiverowner = \'"+user+"\' ")
        acceptedRequests = connection.fetchall()
        connection.execute("SELECT * FROM requests WHERE receiveraccept = 0 AND driveraccept = 0")
        availableRequests = connection.fetchall()

    elif userType == 'Driver':
        connection.execute("SELECT * FROM requests WHERE driverrowner = \'"+user+"\' ")
        acceptedRequests = connection.fetchall()
        connection.execute("SELECT * FROM requests WHERE receiveraccept = 0 AND driveraccept = 0")
        availableRequests = connection.fetchall()
	'''




    context ={
    	'type': userType,
    	'fullname': userName,
    	'allrequests': requests,
    	'username': user

    }
    return flask.render_template("index.html", **context)
