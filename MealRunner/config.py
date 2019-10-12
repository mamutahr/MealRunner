"""
MealRunner development configuration.
"""

import os

# Root of this application, useful if it doesn't occupy an entire domain
APPLICATION_ROOT = '/'

# Secret key for encrypting cookies
SECRET_KEY = b'*\x9a\xd6\x81\x8f\xbfg8\xdc\xfa\x80\x0b\xaa?0jZ[X\xc2\x94\x042+'
SESSION_COOKIE_NAME = 'login'

MAX_CONTENT_LENGTH = 16 * 1024 * 1024

# Database file is var/MealRunner.sqlite3
DATABASE_FILENAME = os.path.join(
    os.path.dirname(os.path.dirname(os.path.realpath(__file__))),
    'var', 'MealRunner.sqlite3'
)