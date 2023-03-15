#! /usr/bin/python3
# -*- coding: UTF-8 -*-

if __name__ == "__main__":
	raise Exception("不支持从这里调用")

__version__ = "1.0"
__all__ = ["MouseChshInnerHttpWrapper"]

from com.mousechsh.common.io.inner.MouseChshInnerWrapper import MouseChshInnerWrapper
from com.mousechsh.common.middle.http.MouseChshHttpServerFramework import MouseChshHttpServerFramework


class MouseChshInnerHttpWrapper(MouseChshHttpServerFramework, MouseChshInnerWrapper):

	def __init__(self):
		super().__init__(protocol='https')
		super(MouseChshHttpServerFramework, self).__init__()
