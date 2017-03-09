from .common import *

INSTALLED_APPS.append("finalware")

# This field is stored in `User.USERNAME_FIELD`.
# This is usually a `username` or  an `email`.
SITE_SUPERUSER_USERNAME = env.get('SFM_SITE_ADMIN_NAME', 'sfmadmin')

# This field is stored in the `email` field, provided,
# that `User.USERNAME_FIELD` is not an `email`.
# If `User.USERNAME_FIELD` is already an email address,
# set `SITE_SUPERUSER_EMAIL = SITE_SUPERUSER_USERNAME`
SITE_SUPERUSER_EMAIL = env.get('SFM_SITE_ADMIN_EMAIL', 'nowhere@example.com')

# A hashed version of `SITE_SUPERUSER_PASSWORD` will be store
# in superuser's `password` field.
SITE_SUPERUSER_PASSWORD = env.get('SFM_SITE_ADMIN_PASSWORD', 'password')

# Configure sites
SITE_OBJECTS_INFO_DICT = {
    '1': {
        'name': 'SFM',
        'domain': env.get('SFM_HOST', 'localhost')
    }
}
SITE_ID = 1

if 'SFM_SITE_ADMIN_EMAIL' in env:
    ADMINS = [(env.get('SFM_SITE_ADMIN_NAME', 'sfmadmin'), env.get('SFM_SITE_ADMIN_EMAIL'))]

STATIC_ROOT = "/opt/sfm-static"

DEFAULT_LEVEL = 'INFO'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(process)d %(name)s %(message)s'
        }
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': env.get('SFM_DJANGO_LOG', DEFAULT_LEVEL),
            'propagate': True,
        },
        'django.request': {
            'handlers': ['console'],
            'level': env.get('SFM_DJANGO_REQUEST_LOG', DEFAULT_LEVEL),
            'propagate': True,
        },
        'apscheduler': {
            'handlers': ['console'],
            'level': env.get('SFM_APSCHEDULER_LOG', DEFAULT_LEVEL),
            'propagate': True,
        },
        'ui': {
            'handlers': ['console'],
            'level': env.get('SFM_UI_LOG', DEFAULT_LEVEL),
            'propagate': True,
        },
        'message_consumer': {
            'handlers': ['console'],
            'level': env.get('SFM_UI_LOG', DEFAULT_LEVEL),
            'propagate': True,
        },
    },
}
RABBITMQ_HOST = "mq"
RABBITMQ_USER = env.get('RABBITMQ_USER')
RABBITMQ_PASSWORD = env.get('RABBITMQ_PASSWORD')
RABBITMQ_MANAGEMENT_PORT = env.get('RABBITMQ_MANAGEMENT_PORT', '15672')
