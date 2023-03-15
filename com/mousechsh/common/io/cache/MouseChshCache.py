#! /usr/bin/python3
# -*- coding: UTF-8 -*-

if __name__ == "__main__":
	raise Exception("不支持从这里调用")

__version__ = "1.0"
__all__ = ["MouseChshCache"]

import time


class MouseChshCache:

	def __init__(self):
		self.__closed = True
		self.__dict = {}
		self.__info = {}
		self.__expire = 3600

	def connect(self):
		self.__closed = False

	def close(self):
		self.__closed = True

	def get(self, key):
		if self.__closed:
			return None
		info = self.__info.get(key, None)
		if info is None:
			self.__dict.pop(key)
			self.__info.pop(key)
			return None
		exp_time = info.get('exp_time', None)
		if exp_time is None:
			self.__dict.pop(key)
			self.__info.pop(key)
			return None
		if time.time() > exp_time:
			self.__dict.pop(key)
			self.__info.pop(key)
			return None
		return self.__dict.get(key, None)

	def set(self, key, value):
		if self.__closed:
			return
		self.__dict[key] = value
		self.__info[key] = {
			'set_time': time.time(),
			'exp_time': time.time() + self.expire()
		}

	def remove(self, key):
		if self.__closed:
			return
		self.__dict.pop(key)
		self.__info.pop(key)

	def clean(self):
		if self.__closed:
			return
		self.__dict.clear()
		self.__info.clear()

	def expire(self):
		return self.__expire
