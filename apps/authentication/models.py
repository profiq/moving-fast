from datetime import datetime, timedelta
import jwt
import logging

from django.conf import settings
from django.contrib.auth.models import AbstractUser

logger = logging.getLogger(__name__)


class User(AbstractUser):
    @property
    def token(self):
        return self._generate_jwt_token()

    def _generate_jwt_token(self):
        dt = datetime.now() + timedelta(days=60)
        data = {"id": self.pk, "exp": int(dt.strftime("%s"))}
        token: bytes = jwt.encode(data, settings.SECRET_KEY, algorithm="HS256")
        return token.decode("utf-8")
