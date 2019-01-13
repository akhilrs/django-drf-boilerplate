# -*- coding: utf-8 -*-
from allauth.socialaccount.providers.facebook.views import (
    FacebookOAuth2Adapter
)
from allauth.socialaccount.providers.github.views import GitHubOAuth2Adapter
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from rest_auth.registration.views import SocialConnectView
from rest_auth.social_serializers import TwitterConnectSerializer


class FacebookConnectView(SocialConnectView):
    adapter_class = FacebookOAuth2Adapter


class TwitterConnectView(SocialConnectView):
    serializer_class = TwitterConnectSerializer
    adapter_class = TwitterConnectSerializer


class GoogleConnectView(SocialConnectView):
    adapter_class = GoogleOAuth2Adapter


class GithubConnectView(SocialConnectView):
    adapter_class = GitHubOAuth2Adapter
