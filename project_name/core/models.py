# -*- coding: utf-8 -*-
from django.db import models


class TimeStampedModel(models.Model):
    class Meta(object):
        abstract = True

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
