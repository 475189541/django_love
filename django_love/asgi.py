import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_love.settings')
django.setup(set_prefix=False)
from channels.http import AsgiHandler
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from .routing import urlpatterns


application = ProtocolTypeRouter({
    "http": AsgiHandler(),
    # Just HTTP for now. (We can add other protocols later.)
    'websocket': AuthMiddlewareStack(
        URLRouter(urlpatterns)
    )
})

