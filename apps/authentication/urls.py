import logging

from django.urls import path

from .views import get_token

logger = logging.getLogger(__name__)

urlpatterns = [
    path('jwt/', get_token, name='jwt'),
]
