#! /usr/bin/python3
# -*- coding: UTF-8 -*-

if __name__ == "__main__":
	raise Exception("不支持从这里调用")

__version__ = "1.0"
__all__ = ["MouseChshHttpRequest"]

from com.mousechsh.common.middle.http.MouseChshHttpConst import MOUSECHSH_HTTP_METHOD_GET, MOUSECHSH_HTTP_VERSION_1_1
from com.mousechsh.common.middle.http.MouseChshHttpHeader import MouseChshHttpHeader


class MouseChshHttpRequest:

	def __init__(self):
		self.__method = MOUSECHSH_HTTP_METHOD_GET
		self.__path = '/'
		self.__version = MOUSECHSH_HTTP_VERSION_1_1
		self.__header = MouseChshHttpHeader()
		self.__body = ''

	def get_method(self):
		return str(self.__method)

	def set_method(self, value):
		self.__method = str(value).upper()

	def get_path(self):
		return str(self.__path)

	def set_path(self, value):
		self.__path = value

	def get_version(self):
		return str(self.__version)

	def set_version(self, value):
		self.__version = value

	def get_header(self):
		return self.__header

	def get_body(self):
		return str(self.__body)

	def set_body(self, value):
		self.__body = str(value).strip()

	def to_string(self):
		result = ''
		result += self.get_method()
		result += ' '
		result += self.get_path()
		result += ' '
		result += self.get_version()
		result += '\r\n'
		result += self.get_header().to_string()
		result += '\r\n'
		result += self.get_body()
		result += '\r\n\r\n'
		return result

	def parse(self, text):
		idx = text.find(' ')
		if idx < 0:
			return
		self.set_method(text[0: idx])
		text = text[idx + 1:]
		idx = text.find(' ')
		if idx < 0:
			return
		self.set_path(text[0: idx])
		text = text[idx + 1:]
		idx = text.find('\r\n')
		if idx < 0:
			return
		self.set_version(text[0: idx])
		text = text[idx + 2:]

		idx = text.find('\r\n\r\n')
		if idx < 0:
			return
		self.get_header().parse(text[0: idx])

		self.set_body(text[idx + 4:])
