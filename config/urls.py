from django.urls import include, path
from django.contrib import admin

urlpatterns = [
    path('', include('apps.authentication.urls')),
    path('chat/', include('apps.chat.urls')),
    path('admin/', admin.site.urls),
]
