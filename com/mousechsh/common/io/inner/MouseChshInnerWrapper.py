#! /usr/bin/python3
# -*- coding: UTF-8 -*-

if __name__ == "__main__":
	raise Exception("不支持从这里调用")

__version__ = "1.0"
__all__ = [
	"MouseChshInnerWrapper",
]

import time

from com.mousechsh.common.log.MouseChshLog import mousechsh_logging_data, mousechsh_logging_exception


class MouseChshInnerWrapper:

	def __init__(self):
		self.__default = 'MouseChshInnerWrapper'
		self.__run = False

	def run(self):
		self.__run = True

	def call(self, input_value):
		if self.__run:
			try:
				mousechsh_logging_data(input_value, "开始进程内处理请求，请求内容：")
				timer = time.time()
				output = self.proc(input_value)
				mousechsh_logging_data(
					output, "完成对进程内处理的响应，用时【", ('%0.6f' % (time.time() - timer)), "】，响应内容："
				)
				return output
			except Exception as ex:
				mousechsh_logging_exception(ex, "进程内处理在执行处理代码时遇到错误：")
				return None
		return None

	def proc(self, request):
		return self.__default

	def close(self):
		self.__run = False
