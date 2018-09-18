from django.db import models

from apps.authentication.models import User


class Room(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'chat room'
        verbose_name_plural = 'chat rooms'
        get_latest_by = 'created_at'

    def __str__(self) -> str:
        return self.name

    def get_absolute_url(self):
        return f'/chat/{self.slug}/'


class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='messages')
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='messages')
    content = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'chat message'
        verbose_name_plural = 'chat messages'
        get_latest_by = 'created_at'

    def __str__(self) -> str:
        return f'Message {self.id} from {self.user}'
