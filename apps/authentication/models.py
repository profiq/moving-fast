from datetime import datetime, timedelta
from jwt import JWT

from django.conf import settings
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):

    @property
    def token(self):
        return self._generate_jwt_token()

    def _generate_jwt_token(self):
        dt = datetime.now() + timedelta(days=60)
        data = {'id': self.pk, 'exp': int(dt.strftime('%s'))}
        jwt = JWT()
        token = jwt.encode(data, settings.SECRET_KEY, 'RS256')

        return token.decode('utf-8')
