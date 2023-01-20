#! /usr/bin/python3
# -*- coding: UTF-8 -*-

if __name__ == "__main__":
	raise Exception("不支持从这里调用")

__version__ = "1.0"
__all__ = ["MouseChshSM4pECBpPKCS5"]

from gmssl.sm4 import CryptSM4, SM4_ENCRYPT, SM4_DECRYPT

from com.mousechsh.common.log.MouseChshLog import mousechsh_logging_exception
from com.mousechsh.common.util.crypto.MouseChshCrypto import MouseChshCrypto


class MouseChshSM4pECBpPKCS5(MouseChshCrypto):

	def __init__(self):
		super().__init__()
		self.bit_len(128)

	def bit_len(self, bit_len=None):
		if bit_len is None:
			return super().bit_len()
		if bit_len == 128:
			super().bit_len(128)
		else:
			super().bit_len(128)

	def byte_len(self, byte_len=None):
		if byte_len is None:
			return super().byte_len()
		if byte_len == 16:  # = 128 / 8
			super().byte_len(16)
		else:  # = 128 / 8
			super().byte_len(16)

	def encrypt(self):
		if not isinstance(self.plaintext(), bytes):
			self.ciphertext(self.default_data())
			return
		try:
			cryptor = CryptSM4()
			cryptor.set_key(self.key(), SM4_ENCRYPT)

			data = cryptor.crypt_ecb(self.plaintext())
			self.ciphertext(data)
		except Exception as ex:
			mousechsh_logging_exception(ex, '加密编码SM4/ECB时遇到错误：')
			self.ciphertext(self.default_data())

	def decrypt(self):
		if not isinstance(self.ciphertext(), bytes):
			self.plaintext(self.default_data())
			return
		try:
			cryptor = CryptSM4()
			cryptor.set_key(self.key(), SM4_DECRYPT)

			data = cryptor.crypt_ecb(self.ciphertext())
			self.plaintext(data)
		except Exception as ex:
			mousechsh_logging_exception(ex, '解密解码SM4/ECB时遇到错误：')
			self.plaintext(self.default_data())
