from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.getenv(
    "DJANGO_SECRET_KEY",
    "change-this-secret-key"
)

DEBUG = True

ALLOWED_HOSTS = ["*"]


# ============================
# APPLICATIONS
# ============================

INSTALLED_APPS = [
    "django.contrib.contenttypes",
    "django.contrib.staticfiles",
    "love",
]


# ============================
# MIDDLEWARE
# ============================

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
]


# ============================
# URLS
# ============================

ROOT_URLCONF = "date_django.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
            ],
        },
    },
]

WSGI_APPLICATION = "date_django.wsgi.application"


# ============================
# DATABASE
# ============================

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


# ============================
# LANGUAGE / TIMEZONE
# ============================

LANGUAGE_CODE = "fr-fr"

TIME_ZONE = "Africa/Bamako"

USE_I18N = True

USE_TZ = True


# ============================
# STATIC FILES
# ============================

STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "staticfiles"

STORAGES = {
    "default": {
        "BACKEND": "django.core.files.storage.FileSystemStorage",
    },
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
    },
}

# ============================
# DEFAULT
# ============================

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


# ============================
# EMAIL
# ============================

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"

EMAIL_HOST = "smtp.gmail.com"

EMAIL_PORT = 587

EMAIL_USE_TLS = True

EMAIL_HOST_USER = os.getenv(
    "EMAIL_HOST_USER",
    "sidfatou00@gmail.com"
)

EMAIL_HOST_PASSWORD = os.getenv(
    "EMAIL_HOST_PASSWORD",
    ""
)

DATE_RECIPIENT_EMAIL = os.getenv(
    "DATE_RECIPIENT_EMAIL",
    "sidfatou00@gmail.com"
)

DEFAULT_FROM_EMAIL = EMAIL_HOST_USER