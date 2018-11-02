from .base import *  # pylint: disable=W0401,W0614

SECRET_KEY = env.str("SECRET_KEY")

# Database
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": env.str("POSTGRES_DB").rstrip(),
        "USER": env.str("POSTGRES_USER").rstrip(),
        "PASSWORD": env.str("POSTGRES_PASSWORD").rstrip(),
        "HOST": env.str("POSTGRES_HOST"),
        "PORT": env.str("POSTGRES_PORT"),
        "ATOMIC_REQUESTS": True,
        "CONN_MAX_AGE": None,
    }
}

# Static files
MIDDLEWARE.insert(1, 'whitenoise.middleware.WhiteNoiseMiddleware')
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Security
# SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
# SECURE_HSTS_SECONDS = 31536000
# SECURE_FRAME_DENY = True
# SECURE_CONTENT_TYPE_NOSNIFF = True
# SECURE_BROWSER_XSS_FILTER = True
# SESSION_COOKIE_SECURE = True
# X_FRAME_OPTIONS = "DENY"
