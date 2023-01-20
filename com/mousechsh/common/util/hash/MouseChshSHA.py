#! /usr/bin/python3
# -*- coding: UTF-8 -*-

if __name__ == "__main__":
	raise Exception("不支持从这里调用")

__version__ = "1.0"
__all__ = [
	"MouseChshSHA1Bytes",
	"MouseChshSHA2p256Bytes",
]

from Crypto.Hash.SHA1 import SHA1Hash
from Crypto.Hash.SHA256 import SHA256Hash

from com.mousechsh.common.log.MouseChshLog import mousechsh_logging_exception
from com.mousechsh.common.util.hash.MouseChshHash import MouseChshHash


class MouseChshSHA1Bytes(MouseChshHash):

	def __init__(self):
		super().__init__()

	def cryptor(self, obj=None):
		cryptor = super().cryptor()
		if cryptor is None:
			cryptor = SHA1Hash()
			super().cryptor(cryptor)
		return cryptor

	def to_data(self):
		try:
			cryptor = self.cryptor()
			cryptor.update(self.content())
			return cryptor.digest()
		except Exception as ex:
			mousechsh_logging_exception(ex, '编码SHA1时遇到错误：')
			return self.default_data()


class MouseChshSHA2p256Bytes(MouseChshHash):

	def __init__(self):
		super().__init__()

	def cryptor(self, obj=None):
		cryptor = super().cryptor()
		if cryptor is None:
			cryptor = SHA256Hash()
			super().cryptor(cryptor)
		return cryptor

	def to_data(self):
		try:
			cryptor = self.cryptor()
			cryptor.update(self.content())
			return cryptor.digest()
		except Exception as ex:
			mousechsh_logging_exception(ex, '编码SHA2-256时遇到错误：')
			return self.default_data()
