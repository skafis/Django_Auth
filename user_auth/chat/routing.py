from channels.staticfiles import StaticFilesConsumer

from channels.routing import route, include
from .consumers import (
		ws_connect,
		ws_message,
		ws_disconnect,
	)

http_routing = [
    route("http.request", StaticFilesConsumer()),
	]

chat_routing = [
	route("websocket.connect", ws_connect),
	route("websocket.receive", ws_message),
	route("websocket.disconnect", ws_disconnect),
	]


channel_routing = [
	include(chat_routing),
	include(http_routing),
	]