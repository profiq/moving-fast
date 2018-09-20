import json
import logging

from django.http import (
    HttpRequest,
    HttpResponse,
    JsonResponse,
    HttpResponseNotAllowed,
    HttpResponseBadRequest,
)

from .models import User

logger = logging.getLogger(__name__)


def get_token(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        try:
            body = json.loads(request.body.decode("utf-8"))
        except json.JSONDecodeError:
            body = {}
        user_id = body.get("user_id")

        if user_id is not None:
            try:
                user = User.objects.get(pk=user_id)
                return JsonResponse({"token": user.token})
            except User.DoesNotExist:
                return HttpResponseBadRequest(
                    json.dumps({"error": f"User with ID {user_id} not found"})
                )
        else:
            return HttpResponseBadRequest(
                json.dumps({"error": 'Required parameter "user_id" is missing'})
            )
    else:
        return HttpResponseNotAllowed(permitted_methods=["POST"])
