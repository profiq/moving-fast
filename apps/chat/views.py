import logging

from django.http import HttpRequest, JsonResponse

from .models import Room

logger = logging.getLogger(__name__)


def index(request: HttpRequest) -> JsonResponse:
    return JsonResponse({'message': 'Success', 'user': str(request.user)})


def room(request: HttpRequest, room_name: str) -> JsonResponse:
    try:
        obj = Room.objects.get(slug=room_name)
        return JsonResponse({
            'message': 'Success',
            'data': {
                'id': obj.id,
                'name': obj.name
            }
        })
    except Room.DoesNotExist:
        response = JsonResponse({'message': 'Room does not exist'})
        response.status_code = 404
        return response
