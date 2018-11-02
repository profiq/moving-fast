import logging

from django.urls import path

from .views import get_token, health

logger = logging.getLogger(__name__)

urlpatterns = [
    path("", health, name="health"),
    path("jwt/", get_token, name="jwt"),
]
