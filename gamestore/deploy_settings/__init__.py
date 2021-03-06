# source: https://teamtreehouse.com/library/making-our-project-productionready

import dj_database_url

from gamestore.settings import *

# Django Core
DEBUG = False
TEMPLATE_DEBUG = False

ALLOWED_HOSTS = [
    'localhost',
    '.herokuapp.com',
]

SECRET_KEY = get_env_variable("SECRET_KEY")

# Postgres
db_from_env = dj_database_url.config()
DATABASES['default'].update(db_from_env)

# WHitenoise static files
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Github login
SITE_ID = 2

# AWS S3 Settings
INSTALLED_APPS += ('storages',)
AWS_QUERYSTRING_AUTH = False
AWS_ACCESS_KEY_ID = get_env_variable("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = get_env_variable("AWS_SECRET_ACCESS_KEY")
AWS_STORAGE_BUCKET_NAME = get_env_variable("AWS_STORAGE_BUCKET_NAME")
MEDIA_URL = 'http://%s.s3.amazonaws.com/s3/buckets/' % AWS_STORAGE_BUCKET_NAME
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
AWS_DEFAULT_ACL = None

# Payment
seller_id = get_env_variable("seller_id")
seller_key = get_env_variable("seller_key")

# Misc settings
SECURE_SSL_REDIRECT = False