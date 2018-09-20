import logging
from typing import Optional

import jwt
from jwt.exceptions import DecodeError
from django.conf import settings
from django.http import HttpRequest

from .models import User

logger = logging.getLogger(__name__)


def decode(jwt_token: str) -> Optional[dict]:
    try:
        return jwt.decode(jwt_token, settings.SECRET_KEY, algorithm="HS256")
    except DecodeError:
        return None


class JwtAuthBackend:
    def get_user(self, user_id: int) -> Optional[User]:
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None

    def authenticate(
        self, request: HttpRequest, jwt_token: str = None
    ) -> Optional[User]:
        payload = decode(jwt_token)

        return None if payload is None else self.get_user(payload.get("id"))
