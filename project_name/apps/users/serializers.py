# -*- coding: utf-8 -*-
from rest_framework import serializers

from .models import User


class StringListField(serializers.ListField):
    child = serializers.CharField()


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = (
            "user_xid",
            "username",
            "first_name",
            "last_name",
            "email",
        )
        read_only_fields = ("username",)

