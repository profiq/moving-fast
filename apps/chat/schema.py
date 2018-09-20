import logging

import graphene
from graphene_django.types import DjangoObjectType

from .models import Room, Message

logger = logging.getLogger(__name__)


class RoomType(DjangoObjectType):
    class Meta:
        model = Room


class MessageType(DjangoObjectType):
    class Meta:
        model = Message


class Query:
    all_rooms = graphene.List(RoomType)
    room = graphene.Field(RoomType, id=graphene.Int(), slug=graphene.String())

    def resolve_all_rooms(self, info, **kwargs):
        return Room.objects.all()

    def resolve_room(self, info, **kwargs):
        room_id = kwargs.get("id")
        slug = kwargs.get("slug")

        if room_id is not None:
            return Room.objects.get(pk=room_id)

        if slug is not None:
            return Room.objects.get(slug=slug)

        return None
