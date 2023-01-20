#! /usr/bin/python3
# -*- coding: UTF-8 -*-

if __name__ == "__main__":
	raise Exception("不支持从这里调用")

__version__ = "1.0"
__all__ = ["MouseChshHttpClientCmd"]

import re

from com.mousechsh.common.cmd.MouseChshCmd import MouseChshCmd, mousechsh_cmd_annotation
from com.mousechsh.common.log.MouseChshLog import mousechsh_logging_exception
from com.mousechsh.common.middle.http.MouseChshHttpClient import MouseChshHttpClient
from com.mousechsh.common.sys.MouseChshThread import mousechsh_thread_annotation


@mousechsh_cmd_annotation()
class MouseChshHttpClientCmd(MouseChshCmd):

	def __init__(self):
		super().__init__()
		self.__host = None
		self.__port = None
		self.__content = ''

	def get_host(self):
		return self.__host

	def get_port(self):
		return self.__port

	def get_content(self):
		return self.__content

	def command(self):
		return 'http-client'

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
		_mousechsh_httpclient_cmd_processing(self)

	def interrupt(self):
		self.__object.close()


@mousechsh_thread_annotation(name='MouseChshHttpClientCmd')
def _mousechsh_httpclient_cmd_processing(client):
	try:
		client.__object = MouseChshHttpClient()
		client.__object.set_host(client.get_host())
		client.__object.set_port(client.get_port())
		client.__object.run()
		client.__object.sync(client.get_content())
	except Exception as ex:
		mousechsh_logging_exception(ex, "遇到无法恢复的错误：")
	finally:
		client.__object.close()
