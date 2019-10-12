"""
MealRunner create button view.

URLs include:
"""
import flask
import MealRunner
import hashlib
import uuid


@MealRunner.app.route('/accounts/create/', methods=['GET', 'POST'])
def show_create():
    """Display /accounts/create/ route."""
    if flask.request.method == 'POST':
        if "giver" in flask.request.form:
            return flask.redirect(flask.url_for('show_create_user', user_type='Giver'))
        if "driver" in flask.request.form:
            return flask.redirect(flask.url_for('show_create_user', user_type='Driver'))
        if "receiver" in flask.request.form:
            return flask.redirect(flask.url_for('show_create_user', user_type='receiver'))
    context = {}
    return flask.render_template("create.html", **context)


@MealRunner.app.route('/accounts/create/user/', methods=['GET', 'POST'])
def show_create_user():
    """Display /accounts/create/ route."""
    context = {}
    context['type'] = flask.request.args.get('user_type')
    
    if flask.request.method == 'POST':
        database = MealRunner.model.get_db()
        cur = database.cursor()
        cur.execute("Select count(*) from users where username = ?",
                    (flask.request.form['username'],))
        count_username = cur.fetchall()[0]["count(*)"]
        if count_username:
            flask.abort(409)
        if not flask.request.form['password']:
            flask.abort(400)
        cur.execute("Insert into users(username, fullname, email,\
                    password, type, address) VALUES(?,?,?,?,?,?) ",
                    (flask.request.form['username'],
                     flask.request.form['fullname'],
                     flask.request.form['email'],
                     create_password(flask.request.form['password']),
                     flask.request.form['type']),
                     flask.request.form['address'])
        flask.session['username'] = flask.request.form['username']
        return flask.redirect(flask.url_for('show_index'))
    return flask.render_template("createUser.html", **context)


def create_password(password):
    """Create a password with a hash and salt."""
    algorithm = "sha512"
    salt = uuid.uuid4().hex
    hash_obj = hashlib.new(algorithm)
    password_salted = salt + password
    hash_obj.update(password_salted.encode("utf-8"))
    password_hash = hash_obj.hexdigest()
    password_db_string = "$".join([algorithm, salt, password_hash])
    return password_db_string
