#! /usr/bin/python3
# -*- coding: UTF-8 -*-

if __name__ == "__main__":
	raise Exception("不支持从这里调用")

__version__ = "1.0"
__all__ = ["MouseChshUTF8StringBytes"]

from com.mousechsh.common.log.MouseChshLog import mousechsh_logging_exception
from com.mousechsh.common.util.codec.MouseChshCodec import MouseChshCodec


# left: bytes from UTF8String, right: bytes
class MouseChshUTF8StringBytes(MouseChshCodec):

	def __init__(self):
		super().__init__()

	def from_right_to_left(self):
		try:
			return self.right().decode('UTF-8')
		except Exception as ex:
			mousechsh_logging_exception(ex, '二进制字符串转为UTF-8字符串时遇到错误：')
			return self.default_left()

	def from_left_to_right(self):
		try:
			return self.left().encode('UTF-8')
		except Exception as ex:
			mousechsh_logging_exception(ex, 'UTF-8字符串转为二进制字符串时遇到错误：')
			return self.default_right()
