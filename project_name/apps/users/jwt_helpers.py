# -*- coding: utf-8 -*-
import logging
from calendar import timegm
from datetime import datetime

from rest_framework_jwt.compat import get_username
from rest_framework_jwt.compat import get_username_field
from rest_framework_jwt.settings import api_settings

from project_name.users.serializers import UserSerializer

LOG = logging.getLogger("project_name.%s" % __name__)


def jwt_payload_handler(user):
    username_field = get_username_field()
    username = get_username(user)
    try:
        mvp_user_id = user.mvp_user.mvp_user_xid
    except Exception as e:
        mvp_user_id = ""
        LOG.error(e)
    # role_names = []
    role_queryset = user.user_role_user.all()
    if role_queryset.count() > 0:
        role_name = role_queryset[0].role.name
    else:
        role_name = ""
    # for role in roles:
    #     role_names.append(role.role.name)
    expiry_dt = datetime.now() + api_settings.JWT_EXPIRATION_DELTA
    payload = {
        "user_xid": str(user.user_xid),
        "role": role_name,
        "mvp_user_id": mvp_user_id,
        "issue_datetime": f"{datetime.now():%Y-%m-%d %H-%M-%S.%f}",
        "expiry_datetime": f"{expiry_dt:%Y-%m-%d %H-%M-%S.%f}",
    }

    payload[username_field] = username

    if api_settings.JWT_ALLOW_REFRESH:
        payload["orig_iat"] = timegm(datetime.now().utctimetuple())

    if api_settings.JWT_AUDIENCE is not None:
        payload["aud"] = api_settings.JWT_AUDIENCE

    if api_settings.JWT_ISSUER is not None:
        payload["iss"] = api_settings.JWT_ISSUER

    return payload


def jwt_response_payload_handler(token, user=None, request=None):
    expiry_dt = datetime.now() + api_settings.JWT_EXPIRATION_DELTA
    return {
        "access_token": token,
        "expiry_datetime": f"{expiry_dt:%Y-%m-%d %H-%M-%S.%f}",
        "user": UserSerializer(user, context={"request": request}).data,
    }
