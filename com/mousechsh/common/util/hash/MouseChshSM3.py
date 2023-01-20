#! /usr/bin/python3
# -*- coding: UTF-8 -*-

if __name__ == "__main__":
	raise Exception("不支持从这里调用")

__version__ = "1.0"
__all__ = [
	"MouseChshSM3Bytes",
]

from gmssl.sm3 import sm3_hash

from com.mousechsh.common.log.MouseChshLog import mousechsh_logging_exception
from com.mousechsh.common.util.hash.MouseChshHash import MouseChshHash


class MouseChshSM3Bytes(MouseChshHash):

	def __init__(self):
		super().__init__()

	def to_data(self):
		try:
			result = sm3_hash(bytearray(self.content()))
			return bytes(bytearray.fromhex(result))
		except Exception as ex:
			mousechsh_logging_exception(ex, '编码SM3时遇到错误：')
			return self.default_data()
