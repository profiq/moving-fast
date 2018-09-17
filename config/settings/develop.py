from .base import *  # pylint: disable=W0401,W0614

DEBUG = True
SECRET_KEY = env.str('SECRET_KEY')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': env.str('POSTGRES_DB'),
        'USER': env.str('POSTGRES_USER'),
        'PASSWORD': env.str('POSTGRES_PASSWORD'),
        'HOST': env.str('POSTGRES_HOST'),
        'PORT': env.str('POSTGRES_PORT'),
        'ATOMIC_REQUESTS': True,
        'CONN_MAX_AGE': None,
    },
}

# Static and media roots for development
STATIC_ROOT = str(ROOT_DIR('staticfiles'))
MEDIA_ROOT = str(ROOT_DIR('mediafiles'))

# Mail
EMAIL_PORT = 1025
EMAIL_HOST = 'mailhog'
