from django.db import IntegrityError
from django.test import TestCase

from .models import Room


class RoomTestCase(TestCase):
    def setUp(self):
        Room.objects.create(name="Game Room 1", slug="game-room-1")

    def test_unique_slug_fail(self):
        with self.assertRaises(IntegrityError):
            Room.objects.create(name="Game Room 2", slug="game-room-1")

    def test_unique_slug(self):
        Room.objects.create(name="Game Room 2", slug="game-room-2")

        self.assertEqual(Room.objects.count(), 2)
