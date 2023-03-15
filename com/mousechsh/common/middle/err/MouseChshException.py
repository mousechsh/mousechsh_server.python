#! /usr/bin/python3
# -*- coding: UTF-8 -*-

if __name__ == "__main__":
	raise Exception("不支持从这里调用")

__version__ = "1.0"
__all__ = [
	"MouseChshException",
	"mousechsh_exception_catcher"
]

from com.mousechsh.common.log.MouseChshLog import mousechsh_logging_data, mousechsh_logging_exception


class MouseChshException(Exception):

	def text(self):
		return '系统发生了未处理事项：'

	def error(self, *args_arr):
		mousechsh_logging_data(args_arr, '异常内的数据')
		return None


def mousechsh_exception_catcher(ex, text='未命名的异常：', *args_arr):
	if isinstance(ex, MouseChshException):
		text = ex.text()
		mousechsh_logging_exception(ex, text)
		return ex.error(*args_arr)
	else:
		mousechsh_logging_exception(ex, text)
		return None
