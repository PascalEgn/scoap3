"""
With these settings, tests run faster.
"""

from .base import *  # noqa
from .base import env

# GENERAL
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#secret-key
SECRET_KEY = env(
    "DJANGO_SECRET_KEY",
    default="wpQt7H4zQGseXwknqw5RFWSpBXxKwr3FqavY6iEzFMmRLlUJWJ8U3eftfJlh88Ie",
)
# https://docs.djangoproject.com/en/dev/ref/settings/#test-runner
TEST_RUNNER = "django.test.runner.DiscoverRunner"

# PASSWORDS
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#password-hashers
PASSWORD_HASHERS = ["django.contrib.auth.hashers.MD5PasswordHasher"]

# STORAGE
# ------------------------
STORAGES = {
    "default": {
        "BACKEND": "django.core.files.storage.FileSystemStorage",
    },
    "staticfiles": {
        "BACKEND": "django.contrib.staticfiles.storage.StaticFilesStorage",
    },
    "legacy-records": {
        "BACKEND": "django.core.files.storage.FileSystemStorage",
        "OPTIONS": {
            "location": str(BASE_DIR / "legacy_records"),  # noqa: F405
        },
    },
}

# EMAIL
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#email-backend
EMAIL_BACKEND = "django.core.mail.backends.locmem.EmailBackend"

# DEBUGGING FOR TEMPLATES
# ------------------------------------------------------------------------------
TEMPLATES[0]["OPTIONS"]["debug"] = True  # type: ignore # noqa: F405
# django-webpack-loader
# ------------------------------------------------------------------------------
WEBPACK_LOADER["DEFAULT"][  # noqa: F405
    "LOADER_CLASS"
] = "webpack_loader.loader.FakeWebpackLoader"

# Opensearch
# ------------------------------------------------------------------------------
# OPENSEARCH_HOST overrides for the default OpenSearch host and port
ALLOWED_HOSTS = ["127.0.0.1"]
OPENSEARCH_DSL_AUTO_REFRESH = True
OPENSEARCH_DSL = {
    "default": {
        "hosts": [env("OPENSEARCH_HOST")],
        "use_ssl": False,
        "verify_certs": False,
        "timeout": 30,
    },
}
