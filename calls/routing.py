from django.urls import re_path
from . import consumers

websocket_urlpatterns = [
    re_path(r'ws/call/(?P<room_name>\d+)/$', consumers.CallConsumer.as_asgi()),
] 