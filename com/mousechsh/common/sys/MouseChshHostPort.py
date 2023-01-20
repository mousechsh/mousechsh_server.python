#! /usr/bin/python3
# -*- coding: UTF-8 -*-

if __name__ == "__main__":
	raise Exception("不支持从这里调用")

__version__ = "1.0"
__all__ = ["MouseChshHostPort"]

from com.mousechsh.common.log.MouseChshLog import mousechsh_logging_exception


class MouseChshHostPort:

	def __init__(self):
		self.__host = "127.0.0.1"
		self.__port = 8000

	def set_host(self, host):
		if host:
			self.__host = str(host)

	def get_host(self):
		return self.__host

	def set_port(self, port):
		if port:
			try:
				p = int(port)
				if p <= 0 or p > 65535:
					raise Exception('数值超过端口号允许的范围')
				self.__port = p
			except Exception as ex:
				mousechsh_logging_exception(ex, "试图将不合法的数值作为端口号使用：")

	def get_port(self):
		return self.__port
