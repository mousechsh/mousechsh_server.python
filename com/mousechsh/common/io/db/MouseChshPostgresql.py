#! /usr/bin/python3
# -*- coding: UTF-8 -*-

if __name__ == "__main__":
	raise Exception("不支持从这里调用")

__version__ = "1.0"
__all__ = ["MouseChshPostgresql"]

import psycopg2

from com.mousechsh.common.io.db.MouseChshDatabase import MouseChshDatabase
from com.mousechsh.common.log.MouseChshLog import mousechsh_logging_exception


class MouseChshPostgresql(MouseChshDatabase):
	_connect = None

	def connect(self):
		if self._connect is not None:
			return
		try:
			self._connect = psycopg2.connect(
				host=self.get_host(),
				port=self.get_port(),
				database=self.get_dbname(),
				user=self.get_username(),
				password=self.get_password()
			)
			self._connect.autocommit = False
		except Exception as ex:
			mousechsh_logging_exception(ex, "连接PostgreSQL数据库时遇到错误：")

	def close(self):
		if self._connect is None:
			return
		try:
			self._connect.close()
		except Exception as ex:
			mousechsh_logging_exception(ex, "关闭PostgreSQL数据库时遇到错误：")
		self._connect = None

	def get(self, sql, params):
		if self._connect is None:
			return None
		with self._connect.cursor() as cursor:
			cursor.execute(sql, params)
			result = {'meta': cursor.description, 'data': []}
			item = cursor.fetchone()
			idx = 0
			max_value = self.get_limit()
			while item is not None and idx < max_value:
				result['data'].append(item)
				item = cursor.fetchone()
				idx += 1
			return result

	def execute(self, sql, params):
		if self._connect is None:
			return
		with self._connect.cursor() as cursor:
			cursor.execute(sql, params)

	def commit(self):
		self._connect.commit()

	def rollback(self):
		self._connect.rollback()
