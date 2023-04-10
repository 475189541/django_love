from django.conf.urls import url
from channels.http import AsgiHandler
from channels.routing import ProtocolTypeRouter


application = ProtocolTypeRouter({
    "http": AsgiHandler(),
})

