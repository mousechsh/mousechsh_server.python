#! /usr/bin/python3
# -*- coding: UTF-8 -*-

if __name__ == "__main__":
	raise Exception("不支持从这里调用")

__version__ = "1.0"
__all__ = ["MouseChshURLStringBytes"]

from urllib import parse

from com.mousechsh.common.log.MouseChshLog import mousechsh_logging_exception
from com.mousechsh.common.util.codec.MouseChshCodec import MouseChshCodec


# left: bytes from URLString, right: bytes
class MouseChshURLStringBytes(MouseChshCodec):

	def __init__(self):
		super().__init__()

	def from_right_to_left(self):
		try:
			return parse.quote(self.right())
		except Exception as ex:
			mousechsh_logging_exception(ex, '二进制字符串转为URL字符串时遇到错误：')
			return self.default_left()

	def from_left_to_right(self):
		try:
			return parse.unquote_to_bytes(self.left())
		except Exception as ex:
			mousechsh_logging_exception(ex, 'URL字符串转为二进制字符串时遇到错误：')
			return self.default_right()
