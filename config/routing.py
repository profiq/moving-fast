from channels.routing import ProtocolTypeRouter, URLRouter

from apps.authentication.middlewares import WebSocketJwtAuthMiddleware
import apps.chat.routing

application = ProtocolTypeRouter({
    'websocket': WebSocketJwtAuthMiddleware(
        URLRouter(apps.chat.routing.websocket_urlpatterns)),
})
