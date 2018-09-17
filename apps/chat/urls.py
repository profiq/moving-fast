import logging

from django.urls import path

from .views import index, room

logger = logging.getLogger(__name__)

urlpatterns = [
    path('', index, name='index'),
    path('<room_name>/', room, name='room'),
]
