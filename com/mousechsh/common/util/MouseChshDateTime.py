#! /usr/bin/python3
# -*- coding: UTF-8 -*-

if __name__ == "__main__":
	raise Exception("不支持从这里调用")

__version__ = "1.0"
__all__ = ["MouseChshDateTime"]

from datetime import datetime, timedelta, timezone

from com.mousechsh.common.log.MouseChshLog import mousechsh_logging_exception


class MouseChshDateTime:

	def __init__(self, *, tz=8):
		self.__time = datetime.now()
		self.__tz = timezone(timedelta(hours=tz))
		self.__time = self.__time.replace(tzinfo=self.__tz)

	def set_timezone(self, value):
		try:
			if isinstance(value, int):
				self.__tz = timezone(timedelta(hours=value))
				self.__time = self.__time.astimezone(self.__tz)
			elif value == 'UTC':
				self.__tz = timezone(timedelta(hours=0))
				self.__time = self.__time.astimezone(self.__tz)
			elif value == 'Asia/Shanghai':
				self.__tz = timezone(timedelta(hours=8))
				self.__time = self.__time.astimezone(self.__tz)
			elif value == 'Asia/Tokyo':
				self.__tz = timezone(timedelta(hours=9))
				self.__time = self.__time.astimezone(self.__tz)
		except Exception as ex:
			mousechsh_logging_exception(ex, '设置时区时遇到错误：')

	def set_timezone__(self, value):
		self.set_timezone(value)
		return self

	def from_string(self, value):
		try:
			self.__time = datetime.strptime(value, '%Y-%m-%d %H:%M:%S')
			self.__time = self.__time.replace(tzinfo=self.__tz)
		except Exception as ex:
			mousechsh_logging_exception(ex, '从字符串转换时间时遇到错误：')

	def from_string__(self, value):
		self.from_string(value)
		return self

	def to_string(self):
		return self.__time.strftime('%Y-%m-%d %H:%M:%S')

	def from_timestamp(self, stamp):
		try:
			self.__time = datetime.fromtimestamp(stamp, self.__tz)
		except Exception as ex:
			mousechsh_logging_exception(ex, '从时间戳转换时间时遇到错误：')

	def from_timestamp__(self, stamp):
		self.from_timestamp(stamp)
		return self

	def to_timestamp(self):
		return int(self.__time.timestamp())
