#! /usr/bin/python3
# -*- coding: UTF-8 -*-

if __name__ == "__main__":
	raise Exception("不支持从这里调用")

__version__ = "1.0"
__all__ = [
	"MouseChshWebSocketServerFramework",
]

from com.mousechsh.common.log.MouseChshLog import mousechsh_logging, mousechsh_logging_data
from com.mousechsh.common.middle.http.MouseChshHttpRequest import MouseChshHttpRequest
from com.mousechsh.common.middle.http.MouseChshHttpResponse import MouseChshHttpResponse, mousechsh_http_response_200
from com.mousechsh.common.middle.router.MouseChshRouter import mousechsh_router_call
from com.mousechsh.common.middle.url.MouseChshUrl import MouseChshUrl
from com.mousechsh.common.middle.ws.MouseChshWebSocketClientItem import mousechsh_websocket_client_item_get, \
	mousechsh_websocket_client_item_new, mousechsh_websocket_client_item_remove, mousechsh_websocket_client_item_join, \
	mousechsh_websocket_client_item_send, mousechsh_websocket_client_item_all_send, \
	mousechsh_websocket_client_item_group_send
from com.mousechsh.common.middle.ws.MouseChshWebSocketFrame import MouseChshWebSocketFrame, \
	MOUSECHSH_WEBSOCKET_FRAME_OPCODE_TEXT, MOUSECHSH_WEBSOCKET_FRAME_OPCODE_CLOSE, \
	MOUSECHSH_WEBSOCKET_FRAME_OPCODE_PING, MOUSECHSH_WEBSOCKET_FRAME_OPCODE_PONG
from com.mousechsh.common.util.MouseChshCodeUtil import mousechsh_codec, mousechsh_code_util_type_bytes, \
	mousechsh_code_util_type_utf8string, mousechsh_hash, mousechsh_code_util_hash_sha1, \
	mousechsh_code_util_type_base64string

_MOUSECHSH_WEBSOCKET_MAGIC_STRING = '258EAFA5-E914-47DA-95CA-C5AB0DC85B11'


def _mousechsh_websocket_response_maker(key):
	response = MouseChshHttpResponse()
	response.set_status_code(101)
	response.get_header().set('Upgrade', 'websocket')
	response.get_header().set('Connection', 'Upgrade')
	value = key + _MOUSECHSH_WEBSOCKET_MAGIC_STRING
	value = mousechsh_hash(
		value,
		method=mousechsh_code_util_hash_sha1,
		source_type=mousechsh_code_util_type_utf8string,
		target_type=mousechsh_code_util_type_base64string
	)
	response.get_header().set('Sec-WebSocket-Accept', value)
	return response.to_string()


class MouseChshWebSocketServerFramework:

	def __init__(self, *, protocol='ws'):
		self.__open_mode = True
		if protocol == 'ws':
			self.__protocol = 'ws'
		elif protocol == 'wss':
			self.__protocol = 'wss'

	def enable_open_mode(self):
		self.__open_mode = True

	def disable_open_mode(self):
		self.__open_mode = False

	def proc(self, sn, net_id, request):
		client = mousechsh_websocket_client_item_get(net_id)
		if client is None:
			client = mousechsh_websocket_client_item_new(net_id)
		if client.is_opened():
			if request:
				req = MouseChshWebSocketFrame()
				req.parse(request)
				data = req.get_data()
				mousechsh_logging_data({
					'Content': mousechsh_codec(
						data,
						source_type=mousechsh_code_util_type_bytes,
						target_type=mousechsh_code_util_type_utf8string
					) if req.get_opcode() == MOUSECHSH_WEBSOCKET_FRAME_OPCODE_TEXT else data,
					'Fin': req.get_fin(),
					'OpCode': req.get_opcode()
				}, '收到通过WebSocket发送的内容：')
				if req.get_opcode() == MOUSECHSH_WEBSOCKET_FRAME_OPCODE_CLOSE:
					mousechsh_logging('断开WebSocket连接，连接目标为【', net_id, '】')
					mousechsh_websocket_client_item_remove(net_id)
					response = MouseChshWebSocketFrame()
					response.set_opcode(MOUSECHSH_WEBSOCKET_FRAME_OPCODE_CLOSE)
					response.set_data(req.get_data())
					return {
						'': response.to_bytes(),
						'conn': False,
						'reset': False,
					}
				elif req.get_opcode() == MOUSECHSH_WEBSOCKET_FRAME_OPCODE_PING:
					response = MouseChshWebSocketFrame()
					response.set_opcode(MOUSECHSH_WEBSOCKET_FRAME_OPCODE_PONG)
					response.set_data(req.get_data())
					return {
						'': response.to_bytes(),
						'conn': True,
						'reset': True,
					}
				self.render(client.get_id(), client.get_group_id(), client.get_header(), data)
			data = client.pop_data()
			if data:
				response = MouseChshWebSocketFrame()
				response.set_opcode(MOUSECHSH_WEBSOCKET_FRAME_OPCODE_TEXT)
				response.set_data(data)
				return {
					'': response.to_bytes(),
					'conn': True,
					'reset': True,
				}
			else:
				return {
					'': None,
					'conn': True,
					'reset': True,
				}
		else:
			data = mousechsh_codec(
				request,
				source_type=mousechsh_code_util_type_bytes,
				target_type=mousechsh_code_util_type_utf8string
			)
			req = MouseChshHttpRequest()
			req.parse(data)
			connection = req.get_header().get('Connection')
			upgrade = req.get_header().get('Upgrade')
			key = req.get_header().get('Sec-WebSocket-Key')
			if 'Upgrade' in connection and 'websocket' in upgrade:
				url = MouseChshUrl()
				url.parse(self.__protocol + '://' + req.get_header().get('Host') + req.get_path())
				mousechsh_websocket_client_item_join(client.get_id(), url.get_path())
				client.set_url(url.to_string())
				client.set_header(
					req.get_header().set__('WebSocket-Url', url.to_string()).to_string()
				)
				client.set_opened(True)
				mousechsh_logging('新的WebSocket连接，连接目标为【', net_id, '】')
				return {
					'': mousechsh_codec(
						_mousechsh_websocket_response_maker(key),
						source_type=mousechsh_code_util_type_utf8string,
						target_type=mousechsh_code_util_type_bytes
					),
					'conn': True,
					'reset': True,
				}
			else:
				mousechsh_websocket_client_item_remove(net_id)
				return {
					'': mousechsh_codec(
						mousechsh_http_response_200(string=True),
						source_type=mousechsh_code_util_type_utf8string,
						target_type=mousechsh_code_util_type_bytes
					),
					'conn': False,
					'reset': False,
				}

	def render(self, client_id, group_id, header, data):
		if not self.__open_mode:
			return
		content = mousechsh_codec(
			data,
			source_type=mousechsh_code_util_type_bytes,
			target_type=mousechsh_code_util_type_utf8string
		)
		if not content:
			return
		index = content.find('#')
		if index >= 0:
			if index == 0:
				mousechsh_websocket_client_item_all_send(content[1:])
			else:
				path = content[0: index]
				content = content[index + 1:]
				if path.startswith('group:'):
					mousechsh_websocket_client_item_group_send(path[6:], content)
				elif path.startswith('client:'):
					mousechsh_websocket_client_item_send(path[7:], content)
				elif path.startswith('ws://'):
					request = MouseChshHttpRequest()
					request.get_header().parse(header)
					url = MouseChshUrl()
					url.parse(path)
					path = url.get_path()
					if not path.strip('/'):
						path = request.get_header().get('WebSocket-Url')
					url.parse(path)
					request.set_path(url.to_string())
					request.get_header().set('WebSocket-Group', group_id)
					request.get_header().set('WebSocket-Client', client_id)
					request.set_body(content)
					mousechsh_logging_data(url.to_string(), '解析出的资源地址：')
					response = MouseChshHttpResponse()
					response.set_status_code(200)
					mousechsh_logging_data(request.to_string(), "请求内容展开：")
					mousechsh_router_call(url, request, response)
					mousechsh_logging_data(response.to_string(), "响应内容展开：")
					target = response.get_header().get_target_type()
					target_id = response.get_header().get_target_id(client_id)
					if target == 'all':
						mousechsh_websocket_client_item_all_send(response.get_body())
					elif target == 'group':
						mousechsh_websocket_client_item_group_send(target_id, response.get_body())
					elif target == 'client':
						mousechsh_websocket_client_item_send(target_id, response.get_body())
					else:
						mousechsh_websocket_client_item_send(client_id, response.get_body())
				else:
					mousechsh_websocket_client_item_group_send(group_id, content)
		else:
			mousechsh_websocket_client_item_send(client_id, data)
