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
    return flask.render_template("index.html", **context)
