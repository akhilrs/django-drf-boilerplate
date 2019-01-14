# -*- coding: utf-8 -*-
import logging

from django.contrib import admin, messages
from django.contrib.admin.options import IS_POPUP_VAR
from django.contrib.admin.utils import unquote
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.models import Group
from django.core.exceptions import PermissionDenied
from django.http import Http404, HttpResponseRedirect
from django.template.response import TemplateResponse
from django.utils.decorators import method_decorator
from django.utils.encoding import force_text
from django.utils.html import escape
from django.views.decorators.debug import sensitive_post_parameters
from django.utils.translation import ugettext_lazy as _

from .models import User

sensitive_post_parameters_m = method_decorator(sensitive_post_parameters())

LOG = logging.getLogger("{{ project_name }}.%s" % __name__)


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "user_uid",
        "username",
        "first_name",
        "last_name",
        "date_joined",
    ]
    fields = [
        "username",
        "password",
        "first_name",
        "last_name",
        "email",
        "is_staff",
        "is_active",
    ]


admin.site.unregister(Group)
