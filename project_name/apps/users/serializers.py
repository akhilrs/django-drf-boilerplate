# -*- coding: utf-8 -*-
from rest_auth.registration.serializers import RegisterSerializer
from rest_framework import serializers

from .models import User


class StringListField(serializers.ListField):
    child = serializers.CharField()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("user_uid", "username", "first_name", "last_name", "email")
        read_only_fields = ("username",)


class UserRegisterSerializer(RegisterSerializer):
    first_name = serializers.CharField(required=True, max_length=20)
    last_name = serializers.CharField(required=True, max_length=50)

    def get_cleaned_data(self):
        data_dict = super(UserRegisterSerializer, self).get_cleaned_data()
        data_dict["first_name"] = self.validated_data.get("first_name", "")
        data_dict["last_name"] = self.validated_data.get("last_name", "")
        return data_dict
