# pylint: disable=W0401,W0614
from .base import *  # noqa: F403

# DEBUG
# ------------------------------------------------------------------------------
# Turn debug off so tests run faster
DEBUG = False
TEMPLATES[0]["OPTIONS"]["debug"] = False  # noqa: F405

# SECRET CONFIGURATION
# ------------------------------------------------------------------------------
SECRET_KEY = env.str("SECRET_KEY", default="!!!SET DJANGO_SECRET_KEY!!!")  # noqa: F405

# CACHES
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#caches
CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.locmem.LocMemCache",
        "LOCATION": "",
    }
}

# DATABASE
# ------------------------------------------------------------------------------
# Local SQLite for testing
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": str(ROOT_DIR("db.sqlite3")),  # noqa: F405
    }
}
CHANNEL_LAYERS = {}

# Static and media roots for tests
STATIC_ROOT = str(ROOT_DIR("staticfiles"))  # noqa: F405
MEDIA_ROOT = str(ROOT_DIR("mediafiles"))  # noqa: F405

# TESTING
# ------------------------------------------------------------------------------
TEST_RUNNER = "django.test.runner.DiscoverRunner"

# PASSWORD HASHING
# ------------------------------------------------------------------------------
# Use fast password hasher so tests run faster
PASSWORD_HASHERS = ["django.contrib.auth.hashers.MD5PasswordHasher"]

# TEMPLATE LOADERS
# ------------------------------------------------------------------------------
# Keep templates in memory so tests run faster
TEMPLATES[0]["OPTIONS"]["loaders"] = [  # noqa: F405
    [
        "django.template.loaders.cached.Loader",
        [
            "django.template.loaders.filesystem.Loader",
            "django.template.loaders.app_directories.Loader",
        ],
    ]
]
