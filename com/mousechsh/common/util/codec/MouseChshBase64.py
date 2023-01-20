#! /usr/bin/python3
# -*- coding: UTF-8 -*-

if __name__ == "__main__":
	raise Exception("不支持从这里调用")

__version__ = "1.0"
__all__ = ["MouseChshBase64Bytes"]

import base64

from com.mousechsh.common.log.MouseChshLog import mousechsh_logging_exception
from com.mousechsh.common.util.codec.MouseChshCodec import MouseChshCodec
from com.mousechsh.common.util.codec.MouseChshUTF8String import MouseChshUTF8StringBytes


# left: bytes from Base64String, right: bytes
class MouseChshBase64Bytes(MouseChshCodec):

	def __init__(self):
		super().__init__()
		self.__utf8bytes = MouseChshUTF8StringBytes()

	def from_right_to_left(self):
		try:
			data = base64.b64encode(self.right())
			return self.__utf8bytes.right__(data).left()
		except Exception as ex:
			mousechsh_logging_exception(ex, '二进制字符串转为Base64字符串时遇到错误：')
			return self.default_left()

	def from_left_to_right(self):
		try:
			data = self.__utf8bytes.left__(self.left()).right()
			return base64.b64decode(data)
		except Exception as ex:
			mousechsh_logging_exception(ex, 'Base64字符串转为二进制字符串时遇到错误：')
			return self.default_right()
