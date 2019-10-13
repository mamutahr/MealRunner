"""
MealRunner index (main) view.

URLs include:
/
"""
import flask
import MealRunner
from MealRunner.views.helper import get_user


@MealRunner.app.route('/')
def show_index():
    """Display / route."""
    if 'username' not in flask.session:
        return flask.redirect(flask.url_for('show_login'))
    user = flask.session['username']
	connection = get_db().cursor()
    connection.execute("SELECT * FROM users WHERE username = \'"+user+"\'")
    userInfo = connection.fetchall()
    userType = userInfo.type 
    
    requests = []
    if userType == 'Giver':
    	connection.execute("SELECT * FROM requests WHERE giverowner = \'"+user+"\'")
    	connection.fetchall()

    else if userType == 'Receiver':
        connection.execute("SELECT * FROM requests WHERE receiverowner = \'"+user+"\' ")
        acceptedRequests = connection.fetchall()
        connection.execute("SELECT * FROM requests WHERE receiveraccept = 0 AND driveraccept = 0")
        availableRequests = connection.fetchall()

    else if userType == 'Driver':
    	connection.execute("SELECT * FROM requests WHERE receiverowner = \'"+user+"\' ")
        acceptedRequests = connection.fetchall()
        connection.execute("SELECT * FROM requests WHERE receiveraccept = 0 AND driveraccept = 0")
        availableRequests = connection.fetchall()




    context = {
    	'user':
    }
    user = get_user('mamutahr')
    context['username'] = user['username']
    return flask.render_template("index.html", **context)
