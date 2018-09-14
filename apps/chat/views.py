from django.http.response import JsonResponse
from django.utils.safestring import mark_safe


def index(request):
    return JsonResponse({'message': 'Success'})


def room(request, room_name):
    return JsonResponse({'message': 'Success', 'data': {'room': mark_safe(room_name)}})
