#! /usr/bin/python3
# -*- coding: UTF-8 -*-

if __name__ == "__main__":
	raise Exception("不支持从这里调用")

__version__ = "1.0"
__all__ = ["MouseChsh3DESpECBpPKCS5"]

from Crypto.Cipher import DES3

from com.mousechsh.common.log.MouseChshLog import mousechsh_logging_exception
from com.mousechsh.common.util.crypto.MouseChshCrypto import MouseChshCrypto
from com.mousechsh.common.util.crypto.padding.MouseChshCryptoPKCS5 import MouseChshCryptoPKCS5


class MouseChsh3DESpECBpPKCS5(MouseChshCrypto):

	def __init__(self):
		super().__init__()
		self.byte_len(24)
		self.__padding = MouseChshCryptoPKCS5()
		self.__mode = DES3.MODE_ECB

	def bit_len(self, bit_len=None):
		if bit_len is None:
			return super().bit_len()
		if bit_len == 128:  # = 16 * 8
			super().bit_len(128)
		elif bit_len == 192:  # = 24 * 8
			super().bit_len(192)
		else:  # = 24 * 8
			super().bit_len(192)

	def byte_len(self, byte_len=None):
		if byte_len is None:
			return super().byte_len()
		if byte_len == 16:
			super().byte_len(16)
		elif byte_len == 24:
			super().byte_len(24)
		else:
			super().byte_len(24)

	def mode(self):
		return self.__mode

	def padding(self):
		return self.__padding

	def encrypt(self):
		if not isinstance(self.plaintext(), bytes):
			self.ciphertext(self.default_data())
			return
		try:
			cryptor = DES3.new(key=self.key(), mode=self.mode())

			data = self.padding().content__(self.plaintext()).data()
			data = cryptor.encrypt(data)
			self.ciphertext(data)
		except Exception as ex:
			mousechsh_logging_exception(ex, '加密编码3DES/ECB/PKCS5Padding时遇到错误：')
			self.ciphertext(self.default_data())

	def decrypt(self):
		if not isinstance(self.ciphertext(), bytes):
			self.plaintext(self.default_data())
			return
		try:
			cryptor = DES3.new(key=self.key(), mode=self.mode())

			data = cryptor.decrypt(self.ciphertext())
			data = self.padding().data__(data).content()
			self.plaintext(data)
		except Exception as ex:
			mousechsh_logging_exception(ex, '解密解码3DES/ECB/PKCS5Padding时遇到错误：')
			self.plaintext(self.default_data())
