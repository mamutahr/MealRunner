"""
MealRunner create button view.

URLs include:
"""
import flask
import MealRunner


@MealRunner.app.route('/accounts/create/', methods=['GET', 'POST'])
def show_create():
    """Display /accounts/create/ route."""
    if flask.request.method == 'POST':
        if "giver" in flask.request.form:
            return flask.redirect(flask.url_for('show_create_user', user_type='Giver'))
        if "driver" in flask.request.form:
            return flask.redirect(flask.url_for('show_create_user', user_type='Driver'))
        if "reciever" in flask.request.form:
            return flask.redirect(flask.url_for('show_create_user', user_type='Reciever'))
    context = {}
    return flask.render_template("create.html", **context)


@MealRunner.app.route('/accounts/create/user/', methods=['GET', 'POST'])
def show_create_user():
    """Display /accounts/create/ route."""
    context = {}
    context['type'] = flask.request.args.get('user_type')
    return flask.render_template("createUser.html", **context)
