# -*- coding: utf-8 -*-
import logging

from rest_framework import viewsets, mixins
from rest_framework.permissions import AllowAny

from .models import User
from .permissions import IsUserOrReadOnly
from .serializers import UserSerializer

LOG = logging.getLogger("project_name.%s" % __name__)


class UserViewSet(
    mixins.RetrieveModelMixin, mixins.UpdateModelMixin, viewsets.GenericViewSet
):
    """
    Updates and retrieves user accounts
    """

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsUserOrReadOnly,)

