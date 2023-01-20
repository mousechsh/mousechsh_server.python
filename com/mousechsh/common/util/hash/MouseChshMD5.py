#! /usr/bin/python3
# -*- coding: UTF-8 -*-

if __name__ == "__main__":
	raise Exception("不支持从这里调用")

__version__ = "1.0"
__all__ = [
	"MouseChshMD5Bytes",
]

from Crypto.Hash.MD5 import MD5Hash

from com.mousechsh.common.log.MouseChshLog import mousechsh_logging_exception
from com.mousechsh.common.util.hash.MouseChshHash import MouseChshHash


class MouseChshMD5Bytes(MouseChshHash):

	def __init__(self):
		super().__init__()

	def cryptor(self, obj=None):
		cryptor = super().cryptor()
		if cryptor is None:
			cryptor = MD5Hash()
			super().cryptor(cryptor)
		return cryptor

	def to_data(self):
		try:
			cryptor = self.cryptor()
			cryptor.update(self.content())
			return cryptor.digest()
		except Exception as ex:
			mousechsh_logging_exception(ex, '编码MD5时遇到错误：')
			return self.default_data()
