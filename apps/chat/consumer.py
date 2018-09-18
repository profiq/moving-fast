import logging
from typing import Optional

from asgiref.sync import async_to_sync
from channels.db import database_sync_to_async
from channels.generic.websocket import AsyncJsonWebsocketConsumer

from .models import Room, Message

logger = logging.getLogger(__name__)


class ChatConsumer(AsyncJsonWebsocketConsumer):

    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = f'chat_{self.room_name}'

        self.room = await self.get_room(self.room_name)
        self.user = self.scope.get('user')

        if not self.user.is_authenticated:
            await self.close(code=401)
        elif self.room is None:
            await self.close(code=404)
        else:
            await self.channel_layer.group_add(self.room_group_name, self.channel_name)
            await self.accept()

    async def disconnect(self, code):
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

    async def receive_json(self, content, **kwargs):
        if 'message' in content:
            await self.channel_layer.group_send(
                self.room_group_name, {
                    'type': 'chat_message',
                    'content': dict(content, user=str(self.scope.get('user'))),
                })
            await self.create_message(message=content.get('message'))

    async def chat_message(self, event):
        await self.send_json(event['content'])

    @database_sync_to_async
    def get_room(self, slug: str) -> Optional[Room]:
        try:
            return Room.objects.get(slug=slug)
        except Room.DoesNotExist:
            return None

    @database_sync_to_async
    def create_message(self, message: str) -> Message:
        return Message.objects.create(room=self.room, user=self.user, content=message)
