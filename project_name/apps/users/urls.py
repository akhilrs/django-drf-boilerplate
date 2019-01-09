# -*- coding: utf-8 -*-
from rest_framework import routers

from .views import UserViewSet

routers = routers.SimpleRouter(trailing_slash=False)
routers.register(r"", UserViewSet)
urlpatterns = routers.urls
