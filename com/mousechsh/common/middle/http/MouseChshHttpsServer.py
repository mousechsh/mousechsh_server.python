#! /usr/bin/python3
# -*- coding: UTF-8 -*-

if __name__ == "__main__":
	raise Exception("不支持从这里调用")

__version__ = "1.0"
__all__ = [
	"MouseChshHttpsServer",
	"mousechsh_https_server_runner"
]

from com.mousechsh.common.io.net.MouseChshTcpSslServer import MouseChshTcpSslServer
from com.mousechsh.common.middle.http.MouseChshHttpServerFramework import MouseChshHttpServerFramework
from com.mousechsh.common.sys.MouseChshThread import mousechsh_thread_annotation


class MouseChshHttpsServer(MouseChshHttpServerFramework, MouseChshTcpSslServer):

	def __init__(self):
		super().__init__(protocol='https')
		super(MouseChshHttpServerFramework, self).__init__()


@mousechsh_thread_annotation(name='MouseChshHttpsServer')
def mousechsh_https_server_runner(host=None, port=None, *, pk_path, key_path, prefix=None):
	server = MouseChshHttpsServer()
	if host is not None:
		server.set_host(host)
	if port is not None:
		server.set_port(port)
	if prefix is not None:
		server.set_path_prefix(prefix)
	if pk_path is not None:
		server.set_pk_path(pk_path)
	if key_path is not None:
		server.set_key_path(key_path)
	server.run()
	return server
