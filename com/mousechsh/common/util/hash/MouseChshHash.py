#! /usr/bin/python3
# -*- coding: UTF-8 -*-

if __name__ == "__main__":
	raise Exception("不支持从这里调用")

__version__ = "1.0"
__all__ = [
	"MouseChshHash",
]

from com.mousechsh.common.log.MouseChshLog import mousechsh_logging_data


class MouseChshHash:

	def __init__(self):
		self.__content = self.default_data()
		self.__data = self.default_data()
		self.__cryptor = None

	def cryptor(self, obj=None):
		if obj is None:
			return self.__cryptor
		self.__cryptor = obj

	def content(self, content=None):
		if content is None:
			return self.__content
		self.__content = self.verity_content(content)
		self.__data = self.to_data()

	def content__(self, content):
		self.content(content)
		return self

	def verity_content(self, content):
		if isinstance(content, bytes):
			return content
		mousechsh_logging_data(content, '数据验证不通过，原始数据如下：')
		return self.__content

	def data(self):
		return self.__data

	@staticmethod
	def default_data():
		return b''

	def to_data(self):
		return self.default_data()
