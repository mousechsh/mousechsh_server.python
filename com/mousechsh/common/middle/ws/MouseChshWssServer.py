#! /usr/bin/python3
# -*- coding: UTF-8 -*-

if __name__ == "__main__":
	raise Exception("不支持从这里调用")

__version__ = "1.0"
__all__ = [
	"MouseChshWssServer",
	"mousechsh_wss_server_runner",
]

from com.mousechsh.common.io.net.MouseChshTcpSslServer import MouseChshTcpSslServer
from com.mousechsh.common.middle.ws.MouseChshWebSocketServerFramework import MouseChshWebSocketServerFramework
from com.mousechsh.common.sys.MouseChshThread import mousechsh_thread_annotation


class MouseChshWssServer(MouseChshWebSocketServerFramework, MouseChshTcpSslServer):

	def __init__(self):
		super().__init__(protocol='wss')
		super(MouseChshWebSocketServerFramework, self).__init__()


@mousechsh_thread_annotation(name='MouseChshWssServer')
def mousechsh_wss_server_runner(host=None, port=None, *, pk_path, key_path):
	server = MouseChshWssServer()
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
