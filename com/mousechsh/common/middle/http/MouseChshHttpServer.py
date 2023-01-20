#! /usr/bin/python3
# -*- coding: UTF-8 -*-

if __name__ == "__main__":
	raise Exception("不支持从这里调用")

__version__ = "1.0"
__all__ = [
	"MouseChshHttpServer",
	"mousechsh_http_server_runner"
]

from com.mousechsh.common.io.net.MouseChshTcpServer import MouseChshTcpServer
from com.mousechsh.common.middle.http.MouseChshHttpServerFramework import MouseChshHttpServerFramework
from com.mousechsh.common.sys.MouseChshThread import mousechsh_thread_annotation


class MouseChshHttpServer(MouseChshHttpServerFramework, MouseChshTcpServer):

	def __init__(self):
		super().__init__()
		super(MouseChshHttpServerFramework, self).__init__()


@mousechsh_thread_annotation(name='MouseChshHttpServer')
def mousechsh_http_server_runner(host=None, port=None, *, prefix=None):
	server = MouseChshHttpServer()
	if host is not None:
		server.set_host(host)
	if port is not None:
		server.set_port(port)
	if prefix is not None:
		server.set_path_prefix(prefix)
	server.run()
	return server
