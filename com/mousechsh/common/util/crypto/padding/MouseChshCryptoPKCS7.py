#! /usr/bin/python3
# -*- coding: UTF-8 -*-

if __name__ == "__main__":
	raise Exception("不支持从这里调用")

__version__ = "1.0"
__all__ = ["MouseChshCryptoPKCS7"]

from com.mousechsh.common.util.crypto.padding.MouseChshCryptoPadding import MouseChshCryptoPadding


class MouseChshCryptoPKCS7(MouseChshCryptoPadding):

	def __init__(self):
		self.__block_size = 0
		self.__content = self.default_data()
		self.__data = self.default_data()

	def block_size(self, size=0):
		if 0 < size <= 0xFF:
			self.__block_size = size

	def content(self, content=None):
		if content is None:
			return self.__content
		if isinstance(content, bytes):
			self.__content = content
		self.__data = self.pad()

	def data(self, data=None):
		if data is None:
			return self.__data
		if isinstance(data, bytes):
			self.__data = data
		self.__content = self.dis_pad()

	def pad(self):
		if self.__block_size <= 0 or self.__block_size > 0xFF:
			return self.default_data()
		if not self.__content:
			return self.default_data()
		last_bit_count = self.__block_size - len(self.__content) % self.__block_size
		will_fill_char = chr(last_bit_count)
		new_content = self.__content + bytes(last_bit_count * will_fill_char, 'UTF-8')
		return new_content

	def dis_pad(self):
		if self.__block_size <= 0:
			return self.default_data()
		if not self.__data:
			return self.default_data()
		last_char = self.__data[len(self.__data) - 1:]
		filled_length = ord(last_char)
		new_content = self.__data[: filled_length * -1]
		return new_content
