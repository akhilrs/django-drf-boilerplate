# -*- coding: utf-8 -*-
from allauth.socialaccount.providers.facebook.views import (
    FacebookOAuth2Adapter
)
from rest_auth.registration.views import SocialConnectView
from rest_auth.social_serializers import TwitterConnectSerializer


class FacebookConnectView(SocialConnectView):
    adapter_class = FacebookOAuth2Adapter


class TwitterConnectView(SocialConnectView):
    serializer_class = TwitterConnectSerializer
    adapter_class = TwitterConnectSerializer
