#! /usr/bin/python3
# -*- coding: UTF-8 -*-
from com.mousechsh.common.middle.union.MouseChshUnionSslServer import mousechsh_union_ssl_server_runner

if __name__ == "__main__":
	raise Exception("不支持从这里调用")

__version__ = "1.0"
__all__ = ["MouseChshUnionServerCmd"]

import re

from com.mousechsh.common.cmd.MouseChshCmd import MouseChshCmd, mousechsh_cmd_annotation
from com.mousechsh.common.log.MouseChshLog import mousechsh_logging_exception
from com.mousechsh.common.middle.union.MouseChshUnionServer import mousechsh_union_server_runner


@mousechsh_cmd_annotation()
class MouseChshUnionServerCmd(MouseChshCmd):

	def __init__(self):
		super().__init__()
		self.__ssl = False
		self.__host = None
		self.__port = None
		self.__pk_path = ''
		self.__key_path = ''

	def reference(self):
		return [
			'com.mousechsh.common.middle.http.MouseChshHttpServerDefaultPage',
			'com.mousechsh.common.middle.ws.MouseChshWebSocketDefaultApi',
		]

	def command(self):
		return 'union-server'

	def parse(self, *params):
		for item in params:
			if re.match('--ssl', item):
				self.__ssl = True
			elif re.match('--host=', item):
				self.__host = item[7:]
			elif re.match('--port=', item):
				self.__port = item[7:]
			elif re.match('--pk-path=', item):
				self.__pk_path = item[10:]
			elif re.match('--key-path=', item):
				self.__key_path = item[11:]

	def run(self):
		try:
			if self.__ssl:
				self.set_object(mousechsh_union_ssl_server_runner(
					self.__host, self.__port,
					pk_path=self.__pk_path, key_path=self.__key_path
				))
			else:
				self.set_object(mousechsh_union_server_runner(self.__host, self.__port))
		except Exception as ex:
			mousechsh_logging_exception(ex, "遇到无法恢复的错误：")

	def interrupt(self):
		server = self.get_object().get_object()
		server.close()
