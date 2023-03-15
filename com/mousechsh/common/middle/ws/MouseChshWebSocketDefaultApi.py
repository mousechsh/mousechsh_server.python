#! /usr/bin/python3
# -*- coding: UTF-8 -*-

if __name__ == "__main__":
	raise Exception("不支持从这里调用")

__version__ = "1.0"
__all__ = []

from com.mousechsh.common.data.json.MouseChshJsonUtil import mousechsh_json_util_to_json
from com.mousechsh.common.middle.http.MouseChshHttpHeader import mousechsh_http_header_accept_language_annotation
from com.mousechsh.common.middle.router.MouseChshHttpRouter import mousechsh_http_router_annotation
from com.mousechsh.common.middle.ws.MouseChshWebSocketClientItem import mousechsh_websocket_client_item_print_all


@mousechsh_http_router_annotation(method='POST', path='/')
@mousechsh_http_header_accept_language_annotation()
def index(url, request, response, *argsArr, **argsDict):
	response.get_header().set_content_type('json')
	response.set_body(
		mousechsh_json_util_to_json({
			'': 'WebSocket服务器已经启动',
			'url': url.to_string(),
			'request': request.get_header().to_string(),
			'response': response.get_header().to_string(),
			'clients': mousechsh_websocket_client_item_print_all()
		})
	)
