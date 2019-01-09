# -*- coding: utf-8 -*-
import logging

from rest_framework.response import Response

logger = logging.getLogger(__name__)


class LoggedResponse(Response):
    def __init__(self, **kwargs):
        super(LoggedResponse, self).__init__(**kwargs)
        kwargs['http_status_code'] = self.status_code
        logger.info(kwargs)
