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
    context = {}
    user = get_user('mamutahr')
    context['username'] = user['username']
    return flask.render_template("index.html", **context)
