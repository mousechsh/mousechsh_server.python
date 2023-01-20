#! /usr/bin/python3
# -*- coding: UTF-8 -*-

if __name__ == "__main__":
	raise Exception("不支持从这里调用")

__version__ = "1.0"
__all__ = [
	"mousechsh_codec_int_bytes",
	"mousechsh_codec_long_bytes",
	"mousechsh_codec_longlong_bytes",
	"MouseChshCodec"
]

import struct

from com.mousechsh.common.log.MouseChshLog import mousechsh_logging_data


def mousechsh_codec_int_bytes(origin):
	return struct.pack('>i', origin)


def mousechsh_codec_long_bytes(origin):
	return struct.pack('>l', origin)


def mousechsh_codec_longlong_bytes(origin):
	return struct.pack('>q', origin)


class MouseChshCodec:

	def __init__(self):
		self.__left = self.default_left()
		self.__right = self.default_right()

	@staticmethod
	def default_left():
		return ''

	@staticmethod
	def default_right():
		return b''

	def left(self, data=None):
		if data is None:
			return self.__left
		self.__left = self.verity_left(data)
		self.__right = self.from_left_to_right()

	def left__(self, data):
		self.left(data)
		return self

	def verity_left(self, data):
		if isinstance(data, str):
			return data
		mousechsh_logging_data(data, '左侧数据验证不通过，原始数据如下：')
		return self.__left

	def right(self, data=None):
		if data is None:
			return self.__right
		self.__right = self.verity_right(data)
		self.__left = self.from_right_to_left()

	def right__(self, data):
		self.right(data)
		return self

	def verity_right(self, data):
		if isinstance(data, bytes):
			return data
		mousechsh_logging_data(data, '右侧数据验证不通过，原始数据如下：')
		return self.__right

	def from_right_to_left(self):
		return self.default_left()

	def from_left_to_right(self):
		return self.default_right()
