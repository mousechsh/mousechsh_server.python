#! /usr/bin/python3
# -*- coding: UTF-8 -*-
from com.mousechsh.common.middle.ws.MouseChshWebSocketServerFramework import MouseChshWebSocketServerFramework

if __name__ == "__main__":
	raise Exception("不支持从这里调用")

__version__ = "1.0"
__all__ = [
	"MouseChshWebSocketServer",
	"mousechsh_websocket_server_runner",
]

from com.mousechsh.common.io.net.MouseChshTcpServer import MouseChshTcpServer
from com.mousechsh.common.sys.MouseChshThread import mousechsh_thread_annotation


class MouseChshWebSocketServer(MouseChshWebSocketServerFramework, MouseChshTcpServer):

	def __init__(self):
		super().__init__()
		super(MouseChshWebSocketServerFramework, self).__init__()


@mousechsh_thread_annotation(name='MouseChshWebSocketServer')
def mousechsh_websocket_server_runner(host=None, port=None):
	server = MouseChshWebSocketServer()
	if host is not None:
		server.set_host(host)
	if port is not None:
		server.set_port(port)
	server.run()
	return server
