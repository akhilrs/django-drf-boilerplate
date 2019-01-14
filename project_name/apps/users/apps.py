# -*- coding: utf-8 -*-
from django.apps import AppConfig


class UserConfig(AppConfig):
    """
    Initializing user app configuration
    """

    name = "{{ project_name }}.apps.users"
    verbose_name = "User App"

    def ready(self):
        pass
