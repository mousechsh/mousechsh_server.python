#! /usr/bin/python3
# -*- coding: UTF-8 -*-

if __name__ == "__main__":
	raise Exception("不支持从这里调用")

__version__ = "1.0"
__all__ = ["MouseChshCmd", "mousechsh_cmd_annotation", "mousechsh_cmd_call_from_cli", "mousechsh_cmd_call"]

from com.mousechsh.common.code.MouseChshAnnotation import mousechsh_annotation, mousechsh_annotation_get
from com.mousechsh.common.log.MouseChshLog import mousechsh_logging, mousechsh_logging_exception
from com.mousechsh.common.sys.MouseChshLoader import mousechsh_loader

_MouseChshCmd = {}


class MouseChshCmd:

	def __init__(self):
		self.__object = None
		self.__content = {}

	def command(self):
		return 'cmd'

	def reference(self):
		return None

	def set_param(self, key, value):
		self.__content[key] = value

	def parse(self, *params):
		pass

	def run(self):
		pass

	def get_object(self):
		return self.__object

	def set_object(self, obj):
		self.__object = obj

	def interrupt(self):
		pass

	def call(self, *args_arr, **args_dict):
		pass


@mousechsh_annotation
def mousechsh_cmd_annotation(cmd):
	c = None
	try:
		c = cmd()
		attr = mousechsh_annotation_get(c)
		if attr.get('mousechsh_cmd_annotation', None) is None:
			return
		cname = c.command()
		mousechsh_logging("加载命令【", cname, "】")
		_MouseChshCmd[cname] = c
	except Exception as ex:
		mousechsh_logging_exception(ex, "加载命令时遇到错误：")
	return c


def mousechsh_cmd_call(cmd, *params):
	try:
		if not cmd:
			return None
		mousechsh_logging("执行命令【", cmd, "】")
		o = _MouseChshCmd.get(cmd, None)
		if o is None:
			mousechsh_logging("命令【", cmd, "】不存在")
			return None
		mousechsh_loader(o.reference())
		o.parse(*params)
		o.run()
		return o
	except Exception as ex:
		mousechsh_logging_exception(ex, "执行命令时遇到错误：")


def mousechsh_cmd_call_from_cli(argv):
	return mousechsh_cmd_call(
		argv[1] if len(argv) > 1 else '',
		*argv[2:] if len(argv) > 2 else ()
	)
