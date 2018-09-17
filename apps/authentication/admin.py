import logging

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User

logger = logging.getLogger(__name__)

admin.site.register(User, UserAdmin)
