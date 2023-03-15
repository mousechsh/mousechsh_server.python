#! /usr/bin/python3
# -*- coding: UTF-8 -*-

if __name__ == "__main__":
	raise Exception("不支持从这里调用")

__version__ = "1.0"
__all__ = ["MouseChshDatabase"]

from com.mousechsh.common.log.MouseChshLog import mousechsh_logging_exception
from com.mousechsh.common.middle.conf.MouseChshConfiguration import mousechsh_configuration_get
from com.mousechsh.common.sys.MouseChshHostPort import MouseChshHostPort


class MouseChshDatabase(MouseChshHostPort):

	def __init__(self):
		super().__init__()
		self.__limit = 100
		self.set_host(mousechsh_configuration_get('database.connection.host'))
		self.set_port(mousechsh_configuration_get('database.connection.port'))
		self.__username = mousechsh_configuration_get('database.connection.user')
		self.__password = mousechsh_configuration_get('database.connection.password')
		self.__dbname = mousechsh_configuration_get('database.connection.database')

	def set_limit(self, value):
		try:
			value = int(value)
			if value < 10 or value > 1000:
				raise Exception('为了防止服务器内存溢出，不允许设置过大的值，请使用分页查询代替')
			self.__limit = value
		except Exception as ex:
			mousechsh_logging_exception(ex, "试图将不合法的数值作为数据库查询结果上限来使用：")

	def get_limit(self):
		return self.__limit

	def set_username(self, value):
		if value is None:
			return
		self.__username = str(value)

	def get_username(self):
		return self.__username

	def set_password(self, value):
		if value is None:
			return
		self.__password = str(value)

	def get_password(self):
		return self.__password

	def set_dbname(self, value):
		if value is None:
			return
		self.__dbname = str(value)

	def get_dbname(self):
		return self.__dbname

	def connect(self):
		pass

	def close(self):
		pass

	def begin(self):
		pass

	def get(self, sql, params):
		pass

	def execute(self, sql, params):
		pass

	def commit(self):
		pass

	def rollback(self):
		pass
