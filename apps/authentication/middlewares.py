import logging

from django.http import HttpRequest, HttpResponse
from django.contrib.auth import authenticate

logger = logging.getLogger(__name__)


class JwtAuthMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request: HttpRequest) -> HttpResponse:
        header: str = request.META.get('HTTP_AUTHORIZATION')
        if header is not None and header.startswith('Bearer '):
            header = header.replace('Bearer ', '', 1)
            user = authenticate(request, jwt_token=header)
            if user is not None:
                request.user = user
        return self.get_response(request)
