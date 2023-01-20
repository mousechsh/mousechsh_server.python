#! /usr/bin/python3
# -*- coding: UTF-8 -*-

if __name__ == "__main__":
	raise Exception("不支持从这里调用")

__version__ = "1.0"
__all__ = [
	"MouseChshCrypto",
]

from com.mousechsh.common.log.MouseChshLog import mousechsh_logging_data


class MouseChshCrypto:

	def __init__(self):
		self.__bit_len = 0
		self.__public_key = self.default_key()
		self.__private_key = self.default_key()
		self.__iv = self.default_key()
		self.__plaintext = self.default_data()
		self.__ciphertext = self.default_data()
		self.__sign = self.default_data()
		self.__verity_result = False

	@staticmethod
	def default_data():
		return b''

	@staticmethod
	def default_key():
		return b''

	def key_generate(self):
		pass

	def key_generate__(self):
		self.key_generate()
		return self

	def bit_len(self, bit_len=None):
		if bit_len is None:
			return self.__bit_len
		if isinstance(bit_len, int):
			if bit_len > 0:
				self.__bit_len = bit_len

	def byte_len(self, byte_len=None):
		if byte_len is None:
			return int(self.__bit_len / 8)
		if isinstance(byte_len, int):
			if byte_len > 0:
				self.__bit_len = byte_len * 8

	def bit_len__(self, bit_len=None):
		self.bit_len(bit_len)
		return self

	def byte_len__(self, byte_len=None):
		self.byte_len(byte_len)
		return self

	def public_key(self, key=None):
		if key is None:
			return self.__public_key
		key = self.verity_key(key)
		self.__public_key = key

	def private_key(self, key=None):
		if key is None:
			return self.__private_key
		key = self.verity_key(key)
		self.__private_key = key

	def key(self, key=None):
		if key is None:
			return self.__private_key
		key = self.verity_key(key)
		if key != self.default_key() and len(key) != self.byte_len():
			mousechsh_logging_data(key, '对称密钥验证长度不通过，原始数据如下：')
			key = self.default_key()
		self.__public_key = key
		self.__private_key = key

	def iv(self, key=None):
		if key is None:
			return self.__iv
		self.__iv = key

	def verity_key(self, data):
		if isinstance(data, bytes):
			return data
		mousechsh_logging_data(data, '密钥验证不通过，原始数据如下：')
		return self.default_key()

	def plaintext(self, data=None):
		if data is None:
			return self.__plaintext
		self.__plaintext = self.verity_data(data)
		self.__ciphertext = self.default_data()
		self.__sign = self.default_data()
		self.__verity_result = False

	def plaintext__(self, data=None):
		self.plaintext(data)
		return self

	def ciphertext(self, data=None):
		if data is None:
			return self.__ciphertext
		self.__ciphertext = self.verity_data(data)
		self.__plaintext = self.default_data()
		self.__sign = self.default_data()
		self.__verity_result = False

	def ciphertext__(self, data=None):
		self.ciphertext(data)
		return self

	def sign_text(self, data=None):
		if data is None:
			return self.__sign
		self.__ciphertext = self.default_data()
		self.__sign = self.verity_data(data)
		self.__verity_result = False

	def sign_text__(self, data=None):
		self.sign_text(data)
		return self

	def verity_data(self, data):
		if isinstance(data, bytes):
			return data
		mousechsh_logging_data(data, '数据验证不通过，原始数据如下：')
		return self.default_data()

	def verity_data__(self, data):
		self.verity_data(data)
		return self

	def verity_result(self, data=None):
		if data is None:
			return self.__verity_result
		self.__verity_result = bool(data)

	def mode(self):
		return None

	def padding(self):
		return None

	def hash(self):
		return None

	def encrypt(self):
		pass

	def encrypt__(self):
		self.encrypt()
		return self

	def decrypt(self):
		pass

	def decrypt__(self):
		self.decrypt()
		return self

	def sign(self):
		pass

	def sign__(self):
		self.sign()
		return self

	def verify(self):
		pass

	def verify__(self):
		self.verify()
		return self
