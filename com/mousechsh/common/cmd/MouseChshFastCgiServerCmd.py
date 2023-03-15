#! /usr/bin/python3
# -*- coding: UTF-8 -*-

if __name__ == "__main__":
	raise Exception("不支持从这里调用")

__version__ = "1.0"
__all__ = ["MouseChshFastCgiServerCmd"]

import re

from com.mousechsh.common.cmd.MouseChshCmd import MouseChshCmd, mousechsh_cmd_annotation
from com.mousechsh.common.log.MouseChshLog import mousechsh_logging_exception
from com.mousechsh.common.middle.cgi.MouseChshFastCgiServer import mousechsh_fastcgi_server_runner


@mousechsh_cmd_annotation()
class MouseChshFastCgiServerCmd(MouseChshCmd):

	def __init__(self):
		super().__init__()
		self.__host = None
		self.__port = None

	def command(self):
		return 'fastcgi-server'

	def parse(self, *params):
		for item in params:
			if re.match('--host=', item):
				self.__host = item[7:]
			elif re.match('--port=', item):
				self.__port = item[7:]

	def run(self):
		try:
			self.set_object(mousechsh_fastcgi_server_runner(self.__host, self.__port))
		except Exception as ex:
			mousechsh_logging_exception(ex, "遇到无法恢复的错误：")

	def interrupt(self):
		server = self.get_object().get_object()
		server.close()
