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
    loginname = flask.session['username']
    connection = get_db().cursor()
    connection.execute("SELECT * FROM users WHERE username = \'"+loginname+"\'")
    userInfo = connection.fetchall()

    if userType == "Giver":


    context = {
    	'user':
    }
    user = get_user('mamutahr')
    context['username'] = user['username']
    return flask.render_template("index.html", **context)
