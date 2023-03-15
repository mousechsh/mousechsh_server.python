#! /usr/bin/python3
# -*- coding: UTF-8 -*-

if __name__ == "__main__":
	raise Exception("不支持从这里调用")

__version__ = "1.0"
__all__ = ["MouseChshRedisException"]

from com.mousechsh.common.middle.err.MouseChshErrMsg import MouseChshErrMsg
from com.mousechsh.common.middle.err.MouseChshException import MouseChshException


class MouseChshRedisException(MouseChshException):

	def text(self):
		return MouseChshErrMsg.text(MouseChshErrMsg.CacheRedisError) + "："

	def error(self, *args_arr):
		return None
