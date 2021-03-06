# -*- coding: utf-8 -*-
import datetime
import os
from distutils.util import strtobool
from os.path import join, dirname

import raven
from configurations import Configuration

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class Common(Configuration):
    INSTALLED_APPS = (
        "django.contrib.admin",
        "django.contrib.auth",
        "django.contrib.contenttypes",
        "django.contrib.sessions",
        "django.contrib.messages",
        "django.contrib.staticfiles",
        "django.contrib.sites",
        # Third party apps
        "rest_framework",  # utilities for rest apis
        "django_filters",  # for filtering rest endpoints
        "corsheaders",
        "raven.contrib.django.raven_compat",
        "drf_yasg",
        "rest_auth",
        # django-rest-auth with social
        "allauth",
        "allauth.account",
        "rest_auth.registration",
        "allauth.socialaccount",
        "allauth.socialaccount.providers.facebook",
        "allauth.socialaccount.providers.twitter",
        # Your apps
        "{{ project_name }}.apps.users",
    )

    # https://docs.djangoproject.com/en/2.0/topics/http/middleware/
    MIDDLEWARE = (
        "django.middleware.security.SecurityMiddleware",
        "django.contrib.sessions.middleware.SessionMiddleware",
        "corsheaders.middleware.CorsMiddleware",
        "django.middleware.common.CommonMiddleware",
        "django.middleware.csrf.CsrfViewMiddleware",
        "django.contrib.auth.middleware.AuthenticationMiddleware",
        "django.contrib.messages.middleware.MessageMiddleware",
        "django.middleware.clickjacking.XFrameOptionsMiddleware",
        "whitenoise.middleware.WhiteNoiseMiddleware",
        "log_request_id.middleware.RequestIDMiddleware",
    )

    SITE_ID = 1
    ALLOWED_HOSTS = ["*"]
    ROOT_URLCONF = "{{ project_name }}.urls"
    SECRET_KEY = os.getenv("DJANGO_SECRET_KEY")
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")
    WSGI_APPLICATION = "{{ project_name }}.wsgi.application"

    # Email
    EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"

    ADMINS = (("Author", "admin@{{ project_name }}.com"),)

    STATICFILES_STORAGE = (
        "whitenoise.storage.CompressedManifestStaticFilesStorage"
    )

    # Database
    # https://docs.djangoproject.com/en/2.1/ref/settings/#databases

    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
        }
    }

    # Postgres Configuration
    # DATABASES = {
    #     "default": {
    #         "ENGINE": "django.db.backends.postgresql_psycopg2",
    #         "OPTIONS": {"options": "-c search_path=public"},
    #         "NAME": os.getenv("POSTGRES_DB"),
    #         "USER": os.getenv("POSTGRES_USER"),
    #         "PASSWORD": os.getenv("POSTGRES_PASSWORD"),
    #         "HOST": os.getenv("POSTGRES_HOST"),
    #         "PORT": os.getenv("POSTGRES_PORT"),
    #     }
    # }

    # General
    APPEND_SLASH = False
    TIME_ZONE = "UTC"
    LANGUAGE_CODE = "en-us"
    # If you set this to False, Django will make some optimizations so as not
    # to load the internationalization machinery.
    USE_I18N = False
    USE_L10N = True
    USE_TZ = True
    LOGIN_REDIRECT_URL = "/"

    # Static files (CSS, JavaScript, Images)
    # https://docs.djangoproject.com/en/2.0/howto/static-files/
    STATIC_ROOT = os.path.normpath(join(os.path.dirname(BASE_DIR), "static"))
    STATICFILES_DIRS = []
    STATIC_URL = "/static/"
    STATICFILES_FINDERS = (
        "django.contrib.staticfiles.finders.FileSystemFinder",
        "django.contrib.staticfiles.finders.AppDirectoriesFinder",
    )

    # Media files
    MEDIA_ROOT = join(os.path.dirname(BASE_DIR), "media")
    MEDIA_URL = "/media/"

    SENTRY_DSN = os.getenv("SENTRY_DSN")

    TEMPLATES = [
        {
            "BACKEND": "django.template.backends.django.DjangoTemplates",
            "DIRS": STATICFILES_DIRS,
            "APP_DIRS": True,
            "OPTIONS": {
                "context_processors": [
                    "django.template.context_processors.debug",
                    "django.template.context_processors.request",
                    "django.contrib.auth.context_processors.auth",
                    "django.contrib.messages.context_processors.messages",
                ]
            },
        }
    ]

    # Set DEBUG to False as a default for safety
    # https://docs.djangoproject.com/en/dev/ref/settings/#debug
    DEBUG = strtobool(os.getenv("DJANGO_DEBUG", "no"))

    # Password Validation
    # https://docs.djangoproject.com/en/2.0/topics/auth/passwords/#module-django.contrib.auth.password_validation
    AUTH_PASSWORD_VALIDATORS = [
        {
            "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"
        },
        {
            "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"
        },
        {
            "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"
        },
        {
            "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"
        },
    ]

    try:
        RAVEN_CONFIG = {
            "dsn": SENTRY_DSN,
            # If you are using git, you can also automatically configure the
            # release based on the git info.
            "release": raven.fetch_git_sha(
                os.path.join(BASE_DIR, os.pardir, os.pardir)
            ),
        }
    except Exception:
        RAVEN_CONFIG = {
            # Docker build inserts git sha into env var
            "release": os.getenv(
                "GIT_COMMIT", "GITSHANOTAVALABLE8CHECKSETTINGSBASE"
            )
        }

    # Log Request Id
    LOG_REQUESTS = True
    LOG_REQUEST_ID_HEADER = "HTTP_X_REQUEST_ID"
    GENERATE_REQUEST_ID_IF_NOT_IN_HEADER = True
    REQUEST_ID_RESPONSE_HEADER = "X-CORRELATION-ID"

    # Logging
    LOGGING = {
        "version": 1,
        "disable_existing_loggers": False,
        "formatters": {
            "django.server": {
                "()": "django.utils.log.ServerFormatter",
                "format": "[%(server_time)s] %(message)s",
            },
            "verbose": {
                "format": "%(levelname)s [%(asctime)s] [%(module)s] [%(process)d] [%(thread)d] [%(request_id)s] "
                "%(name)s:  %(message)s"
            },
            "simple": {
                "format": "%(levelname)s [%(request_id)s] %(name)s: %(message)s"
            },
            "standard": {
                "format": "%(levelname)-5s [%(asctime)s] [%(request_id)s] %(name)s: %(message)s"
            },
        },
        "filters": {
            "require_debug_true": {"()": "django.utils.log.RequireDebugTrue"},
            "request_id": {"()": "log_request_id.filters.RequestIDFilter"},
        },
        "handlers": {
            "django.server": {
                "level": "INFO",
                "class": "logging.StreamHandler",
                "formatter": "django.server",
                "filters": ["request_id"],
            },
            "console": {
                "level": "DEBUG",
                "class": "logging.StreamHandler",
                "formatter": "simple",
                "filters": ["request_id"],
            },
            "mail_admins": {
                "level": "ERROR",
                "class": "django.utils.log.AdminEmailHandler",
            },
            "info_file_handler": {
                "class": "logging.handlers.RotatingFileHandler",
                "level": "INFO",
                "formatter": "standard",
                "filename": os.path.join(
                    dirname(BASE_DIR), "logs/{{ project_name }}_info.log"
                ),
                "maxBytes": 10485760,
                "backupCount": 20,
                "encoding": "utf8",
                "filters": ["request_id"],
            },
            "error_file_handler": {
                "class": "logging.handlers.RotatingFileHandler",
                "level": "ERROR",
                "formatter": "verbose",
                "filename": os.path.join(
                    dirname(BASE_DIR), "logs/{{ project_name }}_errors.log"
                ),
                "maxBytes": 10485760,
                "backupCount": 20,
                "encoding": "utf8",
                "filters": ["request_id"],
            },
            "sentry": {
                "level": "ERROR",
                "formatter": "verbose",
                "class": "raven.handlers.logging.SentryHandler",
                "dsn": SENTRY_DSN,
                "filters": ["request_id"],
            },
        },
        "loggers": {
            "django": {"handlers": ["console"], "propagate": True},
            "django.server": {
                "handlers": ["django.server"],
                "level": "INFO",
                "propagate": False,
            },
            "django.request": {
                "handlers": ["mail_admins", "console"],
                "level": "ERROR",
                "propagate": False,
            },
            "django.db.backends": {"handlers": ["console"], "level": "INFO"},
            "{{ project_name }}": {
                "handlers": [
                    "info_file_handler",
                    "error_file_handler",
                    "sentry",
                ],
                "level": "DEBUG",
                "propagate": False,
            },
        },
    }

    # Custom user app
    AUTH_USER_MODEL = "users.User"

    # Django Rest Framework
    REST_FRAMEWORK = {
        "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.PageNumberPagination",
        "PAGE_SIZE": int(os.getenv("DJANGO_PAGINATION_LIMIT", 10)),
        "DATETIME_FORMAT": "%Y-%m-%dT%H:%M:%S%z",
        "DEFAULT_RENDERER_CLASSES": (
            "{{ project_name }}.core.renderers.JuloJSONRenderer",
        ),
        "DEFAULT_PERMISSION_CLASSES": [
            "rest_framework.permissions.IsAuthenticated"
        ],
        "DEFAULT_AUTHENTICATION_CLASSES": (
            "rest_framework_jwt.authentication.JSONWebTokenAuthentication",
            "rest_framework.authentication.SessionAuthentication",
        ),
    }

    REST_USE_JWT = True  # django-rest-auth to use JWT
    REST_AUTH_REGISTER_SERIALIZERS = {
        "REGISTER_SERIALIZER": "{{ project_name }}.apps.users.serializers.UserRegisterSerializer"
    }
    ACCOUNT_ADAPTER = (
        "{{ project_name }}.apps.users.adapter.UserAccountAdapter"
    )

    JWT_AUTH = {
        "JWT_ENCODE_HANDLER": "rest_framework_jwt.utils.jwt_encode_handler",
        "JWT_DECODE_HANDLER": "rest_framework_jwt.utils.jwt_decode_handler",
        "JWT_PAYLOAD_GET_USER_ID_HANDLER": "rest_framework_jwt.utils.jwt_get_user_id_from_payload_handler",
        "JWT_SECRET_KEY": JWT_SECRET_KEY,
        "JWT_GET_USER_SECRET_KEY": None,
        "JWT_PUBLIC_KEY": None,
        "JWT_PRIVATE_KEY": None,
        "JWT_ALGORITHM": "HS256",
        "JWT_VERIFY": True,
        "JWT_VERIFY_EXPIRATION": True,
        "JWT_LEEWAY": 0,
        "JWT_EXPIRATION_DELTA": datetime.timedelta(seconds=86400),
        "JWT_AUDIENCE": None,
        "JWT_ISSUER": None,
        "JWT_ALLOW_REFRESH": False,
        "JWT_REFRESH_EXPIRATION_DELTA": datetime.timedelta(days=7),
        "JWT_AUTH_HEADER_PREFIX": "JWT",
        "JWT_AUTH_COOKIE": None,
    }

    CORS_ORIGIN_ALLOW_ALL = True
    CORS_ALLOW_CREDENTIALS = True
