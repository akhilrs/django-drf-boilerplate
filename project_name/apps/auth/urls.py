# -*- coding: utf-8 -*-

from rest_framework.urls import url

from .views import FacebookConnectView
from .views import TwitterConnectView

urlpatterns = [
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
]
