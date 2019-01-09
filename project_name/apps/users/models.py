# -*- coding: utf-8 -*-
import uuid

from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _

from project_name.core.models import TimeStampedModel


@python_2_unicode_compatible
class User(AbstractUser):
    user_xid = models.UUIDField(default=uuid.uuid4, editable=False)

    class Meta:
        verbose_name = _(u"User")
        verbose_name_plural = _(u"Users")

    def __str__(self):
        return self.username
