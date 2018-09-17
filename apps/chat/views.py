import logging

from django.http.response import JsonResponse
from django.utils.safestring import mark_safe

logger = logging.getLogger(__name__)


def index(request):
    return JsonResponse({'message': 'Success', 'user': str(request.user)})


def room(request, room_name):
    return JsonResponse({'message': 'Success', 'data': {'room': mark_safe(room_name)}})
