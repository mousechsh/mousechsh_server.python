#! /usr/bin/python3
# -*- coding: UTF-8 -*-

if __name__ == "__main__":
	raise Exception("不支持从这里调用")

__version__ = "1.0"
__all__ = ["MouseChshTcpClientCmd"]

import re

from com.mousechsh.common.cmd.MouseChshCmd import MouseChshCmd, mousechsh_cmd_annotation
from com.mousechsh.common.io.net.MouseChshTcpClient import MouseChshTcpClient
from com.mousechsh.common.log.MouseChshLog import mousechsh_logging_exception
from com.mousechsh.common.sys.MouseChshThread import mousechsh_thread_annotation


@mousechsh_cmd_annotation()
class MouseChshTcpClientCmd(MouseChshCmd):

	def __init__(self):
		super().__init__()
		self.__host = None
		self.__port = None
		self.__content = ''

	def host(self):
		return self.__host

	def port(self):
		return self.__port

	def content(self):
		return self.__content

	def command(self):
		return 'tcp-client'

	def parse(self, *params):
		for item in params:
			if re.match('--host=', item):
				self.__host = item[7:]
			elif re.match('--port=', item):
				self.__port = item[7:]
			else:
				self.__content += item + ' '
		self.__content.strip()

	def run(self):
		_mousechsh_tcp_client_cmd_processing(self)

	def interrupt(self):
		self.get_object().close()


@mousechsh_thread_annotation(name='MouseChshTcpClientCmd')
def _mousechsh_tcp_client_cmd_processing(client):
	try:
		client.set_object(MouseChshTcpClient())
		client.get_object().set_host(client.host())
		client.get_object().set_port(client.port())
		client.get_object().run()
		client.get_object().sync(client.content())
	except Exception as ex:
		mousechsh_logging_exception(ex, "遇到无法恢复的错误：")
	finally:
		client.__object.close()
