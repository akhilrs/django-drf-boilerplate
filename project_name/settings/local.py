# -*- coding: utf-8 -*-
import os

from .common import Common

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class Local(Common):
    DEBUG = True

    # Testing
    INSTALLED_APPS = Common.INSTALLED_APPS
    INSTALLED_APPS += (
        "django_nose",
        "django_extensions",
        "debug_toolbar",
        "silk",
    )

    MIDDLEWARE = Common.MIDDLEWARE
    MIDDLEWARE += (
        "silk.middleware.SilkyMiddleware",
        "debug_toolbar.middleware.DebugToolbarMiddleware",
    )
    TEST_RUNNER = "django_nose.NoseTestSuiteRunner"
    NOSE_ARGS = [
        BASE_DIR,
        "-s",
        "--nologcapture",
        "--with-coverage",
        "--with-progressive",
        "--cover-package={{ project_name }}",
    ]

    # Mail
    EMAIL_HOST = "localhost"
    EMAIL_PORT = 1025
    EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
