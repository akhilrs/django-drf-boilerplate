# -*- coding: utf-8 -*-

from django.urls import include
from rest_framework.urls import url

from .views import (
    FacebookConnectView,
    TwitterConnectView,
    GoogleConnectView,
    GithubConnectView,
)

urlpatterns = [
    # django-rest-auth with social
    url(r"^", include("rest_auth.urls")),
    url(r"^registration/", include("rest_auth.registration.urls")),
    url(
        r"^facebook/connect/$",
        FacebookConnectView.as_view(),
        name="fb_connect",
    ),
    url(
        r"^twitter/connect/$",
        TwitterConnectView.as_view(),
        name="twitter_connect",
    ),
    url(
        r"^google/connect/$",
        GoogleConnectView.as_view(),
        name="google_connect",
    ),
    url(
        r"^github/connect/$",
        GithubConnectView.as_view(),
        name="github_connect",
    ),
]
