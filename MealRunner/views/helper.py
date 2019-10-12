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

def get_request(id):
    """Get a user object from username"""
    database = MealRunner.model.get_db()
    cur = database.execute(
        "Select * from requests where requestid = ?", (id,)
        )
    return cur.fetchone()