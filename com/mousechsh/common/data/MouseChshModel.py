#! /usr/bin/python3
# -*- coding: UTF-8 -*-

if __name__ == "__main__":
	raise Exception("不支持从这里调用")

__version__ = "1.0"
__all__ = ["MouseChshModel"]


class MouseChshModel:

	def __init__(self):
		self.__data = {}

	def __setattr__(self, key, value):
		if key == '__data':
			super.__setattr__(self, key, value)
		elif key.startswith('_'):
			super.__setattr__(self, key, value)
		else:
			self.__data[key] = value

	def get(self, key):
		return self.__data.get(key, None)

	def set(self, key, value):
		if key is None:
			return
		if value is None:
			self.__data.pop(key, None)
		else:
			self.__data[key] = value

	def remove(self, key):
		self.set(key, None)

	def data(self):
		return self.__data

	def to_string(self):
		return str(self.__data)
