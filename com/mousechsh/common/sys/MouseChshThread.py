#! /usr/bin/python3
# -*- coding: UTF-8 -*-

if __name__ == "__main__":
	raise Exception("不支持从这里调用")

__version__ = "1.0"
__all__ = [
	"mousechsh_thread_sleep",
	"mousechsh_thread_annotation",
	"MouseChshThread"
]

import threading
import time

from com.mousechsh.common.code.MouseChshAnnotation import mousechsh_annotation
from com.mousechsh.common.log.MouseChshLog import mousechsh_logging

_mousechsh_thread_index = 0


def mousechsh_thread_sleep():
	time.sleep(0.2)


@mousechsh_annotation
def mousechsh_thread_annotation(func, name, daemon=True):
	def mousechsh_thread_annotation_params(*args_arr, **args_dict):
		global _mousechsh_thread_index
		_mousechsh_thread_index += 1
		thd = MouseChshThread()
		thd.setName(name + '-' + str(_mousechsh_thread_index))
		thd.set_func(func, *args_arr, **args_dict)
		thd.setDaemon(daemon)

		mousechsh_logging("开始线程【", thd.getName(), "】")
		thd.start()

		return thd

	return mousechsh_thread_annotation_params


class MouseChshThread(threading.Thread):

	def __init__(self):
		super().__init__()
		self.__func = None
		self.__func_args_arr = None
		self.__func_args_dict = None
		self.__object = None

	def set_func(self, value, *args_arr, **args_dict):
		self.__func = value
		self.__func_args_arr = args_arr
		self.__func_args_dict = args_dict

	def get_object(self):
		return self.__object

	def run(self):
		self.__object = self.__func(*self.__func_args_arr, **self.__func_args_dict)
