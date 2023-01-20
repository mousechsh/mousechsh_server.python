#! /usr/bin/python3
# -*- coding: UTF-8 -*-

if __name__ == "__main__":
	raise Exception("不支持从这里调用")

__version__ = "1.0"
__all__ = [
	"MouseChshRSApECBpPKCS1",
	"MouseChshRSApECBpPKCS1withSHA1",
	"MouseChshRSApECBpPKCS1withSHA2p256",
]

from Crypto import Random
from Crypto.Cipher import PKCS1_v1_5 as Cipher_pkcs1_v1_5
from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5 as Signature_pkcs1_v1_5

from com.mousechsh.common.log.MouseChshLog import mousechsh_logging_exception
from com.mousechsh.common.util.crypto.MouseChshCrypto import MouseChshCrypto
from com.mousechsh.common.util.hash.MouseChshSHA import MouseChshSHA1Bytes, MouseChshSHA2p256Bytes


class MouseChshRSApECBpPKCS1(MouseChshCrypto):

	def __init__(self):
		super().__init__()
		self.bit_len(1024)

	def bit_len(self, bit_len=None):
		if bit_len is None:
			return super().bit_len()
		if bit_len == 1024:
			super().bit_len(1024)
		elif bit_len == 2048:
			super().bit_len(2048)
		elif bit_len == 4096:
			super().bit_len(4096)
		else:
			super().bit_len(1024)

	def byte_len(self, byte_len=None):
		if byte_len is None:
			return super().byte_len()
		if byte_len == 128:  # = 1024 / 8
			super().byte_len(128)
		elif byte_len == 256:  # = 2048 / 8
			super().byte_len(256)
		elif byte_len == 512:  # = 4096 / 8
			super().byte_len(512)
		else:  # = 1024 / 8
			super().byte_len(128)

	def key_generate(self):
		random_generator = Random.new().read
		rsa = RSA.generate(self.bit_len(), random_generator)
		self.private_key(rsa.exportKey())
		self.public_key(rsa.publickey().exportKey())

	def encrypt(self):
		if not isinstance(self.plaintext(), bytes):
			self.ciphertext(self.default_data())
			return
		try:
			split_len = self.byte_len() - 11

			rsa_key = RSA.importKey(self.public_key())

			cryptor = Cipher_pkcs1_v1_5.new(rsa_key)

			data = b''
			for i in range(0, len(self.plaintext()), split_len):
				data += cryptor.encrypt(self.plaintext()[i:i + split_len])

			self.ciphertext(data)
		except Exception as ex:
			mousechsh_logging_exception(ex, '加密编码RSA/PKCS1时遇到错误：')
			self.ciphertext(self.default_data())

	def decrypt(self):
		if not isinstance(self.ciphertext(), bytes):
			self.plaintext(self.default_data())
			return
		try:
			split_len = self.byte_len()

			rsa_key = RSA.importKey(self.private_key())

			cryptor = Cipher_pkcs1_v1_5.new(rsa_key)

			data = b''
			for i in range(0, len(self.ciphertext()), split_len):
				data += cryptor.decrypt(self.ciphertext()[i:i + split_len], self.default_data())

			self.plaintext(data)
		except Exception as ex:
			mousechsh_logging_exception(ex, '解密解码RSA/PKCS1时遇到错误：')
			self.plaintext(self.default_data())


class MouseChshRSApECBpPKCS1withSHA1(MouseChshRSApECBpPKCS1):

	def hash(self):
		return MouseChshSHA1Bytes()

	def sign(self):
		if not isinstance(self.plaintext(), bytes):
			self.sign_text(self.default_data())
			return
		try:
			hash_obj = self.hash()
			hash_obj.content__(self.plaintext())

			rsa_key = RSA.importKey(self.private_key())

			cryptor = Signature_pkcs1_v1_5.new(rsa_key)

			data = cryptor.sign(hash_obj.cryptor())
			return self.sign_text(data)
		except Exception as ex:
			mousechsh_logging_exception(ex, '签名编码RSA/PKCS1+SHA1时遇到错误：')
			self.sign_text(self.default_data())

	def verify(self):
		if not isinstance(self.plaintext(), bytes):
			self.verity_result(False)
			return
		if not isinstance(self.sign_text(), bytes):
			self.verity_result(False)
			return
		try:
			hash_obj = self.hash()
			hash_obj.content__(self.plaintext())

			rsa_key = RSA.importKey(self.public_key())

			cryptor = Signature_pkcs1_v1_5.new(rsa_key)

			cryptor.verify(hash_obj.cryptor(), self.sign_text())
			self.verity_result(True)
			return
		except Exception as ex:
			mousechsh_logging_exception(ex, '验签解码RSA/PKCS1+SHA1时遇到错误：')
			self.verity_result(False)
			return


class MouseChshRSApECBpPKCS1withSHA2p256(MouseChshRSApECBpPKCS1):

	def hash(self):
		return MouseChshSHA2p256Bytes()

	def sign(self):
		if not isinstance(self.plaintext(), bytes):
			self.sign_text(self.default_data())
			return
		try:
			hash_obj = self.hash()
			hash_obj.content__(self.plaintext())

			rsa_key = RSA.importKey(self.private_key())

			cryptor = Signature_pkcs1_v1_5.new(rsa_key)

			data = cryptor.sign(hash_obj.cryptor())
			return self.sign_text(data)
		except Exception as ex:
			mousechsh_logging_exception(ex, '签名编码RSA/PKCS1+SHA2-256时遇到错误：')
			self.sign_text(self.default_data())

	def verify(self):
		if not isinstance(self.plaintext(), bytes):
			self.verity_result(False)
			return
		if not isinstance(self.sign_text(), bytes):
			self.verity_result(False)
			return
		try:
			hash_obj = self.hash()
			hash_obj.content__(self.plaintext())

			rsa_key = RSA.importKey(self.public_key())

			cryptor = Signature_pkcs1_v1_5.new(rsa_key)

			cryptor.verify(hash_obj.cryptor(), self.sign_text())
			self.verity_result(True)
			return
		except Exception as ex:
			mousechsh_logging_exception(ex, '验签解码RSA/PKCS1+SHA2-256时遇到错误：')
			self.verity_result(False)
			return
