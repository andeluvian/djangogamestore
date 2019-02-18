# source: https://teamtreehouse.com/library/making-our-project-productionready

import dj_database_url

from gamestore.settings import *

DEBUG = False
TEMPLATE_DEBUG = False

ALLOWED_HOSTS = [
    'localhost',
    '.herokuapp.com',
]

SECRET_KEY = get_env_variable("SECRET_KEY")

db_from_env = dj_database_url.config()
DATABASES['default'].update(db_from_env)
