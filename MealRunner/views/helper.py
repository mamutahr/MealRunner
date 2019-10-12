"""
Helper Functions
"""
import MealRunner


def get_user(uname):
    """Get a user object from username"""
    database = MealRunner.model.get_db()
    cur = database.execute(
        "Select * from users where username = ?", (uname,)
        )
    return cur.fetchone()