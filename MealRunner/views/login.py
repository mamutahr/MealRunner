"""
MealRunner login view.

URLs include:
"""
import hashlib
import flask
import MealRunner
from MealRunner.model import get_db
APP = flask.Flask(__name__)


@MealRunner.app.route('/accounts/login/', methods=['GET', 'POST'])
def show_login():
    print('xxxx')
    """Display route."""
    if 'username' in flask.session:
        return flask.redirect(flask.url_for('show_index'))
    if flask.request.method == 'POST':
        flask.session['username'] = flask.request.form['username']
        if not flask.session['username']:
            flask.session.clear()
            return flask.redirect(flask.url_for('show_login'))
        user_password = flask.request.form['password']
        connection = get_db().cursor()
        connection.execute("SELECT password FROM users WHERE username "
                           "LIKE \'" + flask.session['username'] + "\' ")
        hashed_password = connection.fetchall()
        if not hashed_password:
            flask.session.clear()
            return flask.redirect(flask.url_for('show_login'))
        hashed_password = hashed_password[0]['password']
        if check_password(hashed_password, user_password):
            return flask.redirect(flask.url_for('show_index'))

        flask.session.clear()
        return flask.redirect(flask.url_for('show_login'))
    context = {}
    return flask.render_template("login.html", **context)


@MealRunner.app.route('/accounts/logout/')
def show_logout():
    """Display .. route."""
    flask.session.clear()
    return flask.redirect(flask.url_for('show_login'))


def check_password(hashed_password, user_password):
    """Check password."""
    algorithm, salt, password = hashed_password.split('$')
    print(algorithm, salt, password)
    return password == hashlib.sha512(salt.encode() +
                                      user_password.encode()).hexdigest()
