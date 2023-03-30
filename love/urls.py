from django.conf.urls import url
from django.conf import settings
from django.views import static
from love import views


urlpatterns = [
    url(r'^static/(?P<path>.*)$', static.serve, {'document_root': settings.STATIC_ROOT}, name='static'),
    url(r'^SaveMe', views.save_me),
    url(r'^MarryMe', views.marry_me)
]