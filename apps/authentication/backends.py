import jwt
import logging

from django.conf import settings

from .models import User

logger = logging.getLogger(__name__)


class JwtAuthBackend:

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None

    def authenticate(self, request, jwt_token=None):
        message = jwt.decode(jwt_token, settings.SECRET_KEY, algorithm='HS256')
        user = self.get_user(message.get('id'))
        if user is not None:
            return user
