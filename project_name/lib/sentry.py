# -*- coding: utf-8 -*-
from django.conf import settings


def get_sentry_client():
    from raven import Client

    return Client(settings.SENTRY_DSN)
