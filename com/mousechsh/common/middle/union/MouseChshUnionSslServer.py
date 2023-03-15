#! /usr/bin/python3
# -*- coding: UTF-8 -*-

if __name__ == "__main__":
	raise Exception("不支持从这里调用")

__version__ = "1.0"
__all__ = [
	"MouseChshUnionSslServer",
	"mousechsh_union_ssl_server_runner",
]

from com.mousechsh.common.io.net.MouseChshTcpSslServer import MouseChshTcpSslServer
from com.mousechsh.common.middle.http.MouseChshHttpServerFramework import MouseChshHttpServerFramework
from com.mousechsh.common.middle.ws.MouseChshWebSocketServerFramework import MouseChshWebSocketServerFramework
from com.mousechsh.common.sys.MouseChshThread import mousechsh_thread_annotation


class MouseChshUnionSslServer(MouseChshTcpSslServer):

	def __init__(self):
		super().__init__()
		self.__http_server = MouseChshHttpServerFramework(protocol='https')
		self.__ws_server = MouseChshWebSocketServerFramework(protocol='wss')

	def proc(self, sn, net_id, request):
		if request == b'':
			return self.__ws_server.proc(sn, net_id, request)
		elif request.startswith(b'GET ') \
			or request.startswith(b'POST ') \
			or request.startswith(b'PUT ') \
			or request.startswith(b'DELETE ') \
			or request.startswith(b'OPTIONS '):
			if request.find(b'Upgrade: websocket') >= 0:
				return self.__ws_server.proc(sn, net_id, request)
			else:
				return self.__http_server.proc(sn, net_id, request)
		else:
			return self.__ws_server.proc(sn, net_id, request)


@mousechsh_thread_annotation(name='MouseChshUnionSslServer')
def mousechsh_union_ssl_server_runner(host=None, port=None, *, pk_path, key_path):
	server = MouseChshUnionSslServer()
	if host is not None:
		server.set_host(host)
	if port is not None:
		server.set_port(port)
	if pk_path is not None:
		server.set_pk_path(pk_path)
	if key_path is not None:
		server.set_key_path(key_path)
	server.run()
	return server
