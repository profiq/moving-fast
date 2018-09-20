import logging
from typing import Callable, Dict, List
from urllib import parse

from django.contrib.auth import authenticate, models
from django.db import close_old_connections
from django.http import HttpRequest, HttpResponse

from .backends import decode
from .models import User

logger = logging.getLogger(__name__)


class JwtAuthMiddleware:
    def __init__(self, get_response: Callable[[HttpRequest], HttpResponse]):
        self.get_response = get_response

    def __call__(self, request: HttpRequest) -> HttpResponse:
        header: str = request.META.get("HTTP_AUTHORIZATION")
        if header is not None and header.startswith("Bearer "):
            token = header.replace("Bearer ", "", 1)
            user: User = authenticate(request, jwt_token=token)
            if user is not None:
                request.user = user
        return self.get_response(request)


class WebSocketJwtAuthMiddleware:
    def __init__(self, inner):
        self.inner = inner

    def __call__(self, scope: dict):
        query_string: str = bytes(scope["query_string"]).decode("utf-8")
        parsed: Dict[str, List[str]] = parse.parse_qs(query_string)
        user = None

        if "Bearer" in parsed and len(parsed["Bearer"]) == 1:
            token: str = parsed["Bearer"][0]
            payload: dict = decode(token)

            if payload is not None:
                try:
                    user = User.objects.get(pk=payload.get("id"))
                except User.DoesNotExist:
                    pass
                finally:
                    close_old_connections()

        user = user or models.AnonymousUser()
        return self.inner(dict(scope, user=user))
