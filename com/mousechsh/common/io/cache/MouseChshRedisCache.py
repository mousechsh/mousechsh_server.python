#! /usr/bin/python3
# -*- coding: UTF-8 -*-

if __name__ == "__main__":
	raise Exception("不支持从这里调用")

__version__ = "1.0"
__all__ = ["MouseChshRedisCache"]

import redis

from com.mousechsh.common.io.cache.MouseChshCache import MouseChshCache
from com.mousechsh.common.io.cache.MouseChshRedisExceptions import MouseChshRedisException
from com.mousechsh.common.middle.conf.MouseChshConfiguration import mousechsh_configuration_get
from com.mousechsh.common.sys.MouseChshHostPort import MouseChshHostPort


class MouseChshRedisCache(MouseChshCache, MouseChshHostPort):

	def __init__(self):
		super().__init__()
		super(MouseChshCache, self).__init__()
		self.set_host(mousechsh_configuration_get('redis.connection.host', '127.0.0.1'))
		self.set_port(mousechsh_configuration_get('redis.connection.port', 6379))
		self.__db = (mousechsh_configuration_get('redis.connection.db', 0))
		self.__server = None

	def connect(self):
		self.__server = redis.Redis(host=self.get_host(), port=self.get_port(), db=self.__db, decode_responses=True)

	def close(self):
		self.__server.close()
		self.__server = None

	def get(self, key):
		if not self.__server:
			return None
		key = str(key)
		try:
			return self.__server.get(key)
		except Exception as ex:
			raise MouseChshRedisException(ex)

	def set(self, key, value, ex=None):
		if ex is None:
			ex = self.expire
		if not self.__server:
			return
		key = str(key)
		value = str(value)
		try:
			self.__server.set(key, value, ex)
		except Exception as ex:
			raise MouseChshRedisException(ex)

	def remove(self, key):
		if not self.__server:
			return
		key = str(key)
		try:
			self.__server.delete(key)
		except Exception as ex:
			raise MouseChshRedisException(ex)

	def clean(self):
		if not self.__server:
			return
		try:
			self.__server.clean()
		except Exception as ex:
			raise MouseChshRedisException(ex)
