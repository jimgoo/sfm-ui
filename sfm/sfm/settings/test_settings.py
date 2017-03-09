from .common import *
import tempfile
import os

DATABASES = {
    # for unit tests
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'testdb'
    }
}

SFM_DATA_DIR=os.path.join(tempfile.gettempdir(), "test-data")

SCHEDULER_DB_URL = "sqlite:///testdb"

SCHEDULE_HARVESTS = False

PERFORM_EXPORTS = False

PERFORM_EMAILS = False

PERFORM_USER_HARVEST_EMAILS = False

PERFORM_SERIALIZE = False

ADMINS = [("sfmadmin", "superuser@test.com")]

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
            'level': DEFAULT_LEVEL,
            'propagate': True,
        },
        'django.request': {
            'handlers': ['console'],
            'level': DEFAULT_LEVEL,
            'propagate': True,
        },
        'apscheduler': {
            'handlers': ['console'],
            'level': DEFAULT_LEVEL,
            'propagate': True,
        },
        'ui': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': True,
        },
        'message_consumer': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
}