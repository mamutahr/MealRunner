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

def get_request(user):
    """Get a user object from username"""
    connection = get_db().cursor()
    connection.execute("SELECT * FROM users WHERE username = \'"+user+"\'")
    userInfo = connection.fetchall()
    userType = userInfo.type 
    
    if userType == 'Giver':
        connection.execute("SELECT * FROM requests WHERE giverowner = \'"+user+"\'")

    database = MealRunner.model.get_db()
    cur = database.execute(
        "Select * from requests where requestid = ?", (id,)
        )
    return cur.fetchone()