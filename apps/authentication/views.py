import logging

from django.http import HttpRequest, HttpResponse, HttpResponseNotAllowed

from .models import User

logger = logging.getLogger(__name__)


def get_token(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        user_id = 1  # TODO: change this to really obtain user_id and check password
        user = User.objects.get(pk=user_id)
        return HttpResponse(user.token)
    else:
        return HttpResponseNotAllowed(permitted_methods=['POST'])
