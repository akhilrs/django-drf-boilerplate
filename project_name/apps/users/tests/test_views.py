# -*- coding: utf-8 -*-
from django.forms.models import model_to_dict
from django.urls import reverse
from faker import Faker
from nose.tools import eq_
from rest_framework import status
from rest_framework.test import APITestCase

from .factories import UserFactory

fake = Faker()


class TestUserListTestCase(APITestCase):
    """
    Tests /users list operations.
    """

    def setUp(self):
        self.url_login = reverse("login")
        self.url_user = reverse("user-list")
        self.user_data = model_to_dict(UserFactory.build())
        self.client.post(self.url_user, self.user_data)

    def test_post_request_with_no_data_fails(self):
        response = self.client.post(self.url_user, {})
        eq_(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_post_request_with_valid_data_succeeds(self):
        user_data = model_to_dict(UserFactory.build())
        response = self.client.post(self.url_user, user_data)
        eq_(response.status_code, status.HTTP_201_CREATED)

    def test_login_with_valid_data(self):
        login_data = {
            "username": self.user_data["username"],
            "password": self.user_data["password"],
        }
        response = self.client.post(self.url_login, login_data)
        eq_(response.status_code, status.HTTP_200_OK)

    def test_login_with_invalid_data(self):
        login_data = {"username": self.user_data["username"], "password": "1"}
        response = self.client.post(self.url_login, login_data)
        eq_(response.status_code, status.HTTP_400_BAD_REQUEST)
