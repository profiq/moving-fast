from django.urls import include, path
from django.contrib import admin
from graphene_django.views import GraphQLView

urlpatterns = [
    path('', include('apps.authentication.urls')),
    path('chat/', include('apps.chat.urls')),
    path('graphql/', GraphQLView.as_view(graphiql=True), name='graphql'),
    path('admin/', admin.site.urls),
]
