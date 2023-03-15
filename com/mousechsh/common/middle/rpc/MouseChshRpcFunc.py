#! /usr/bin/python3
# -*- coding: UTF-8 -*-

if __name__ == "__main__":
	raise Exception("不支持从这里调用")

__version__ = "1.0"
__all__ = ["mousechsh_rpc_func_annotation", "mousechsh_rpc_func_call"]

from com.mousechsh.common.code.MouseChshAnnotation import mousechsh_annotation, mousechsh_annotation_get
from com.mousechsh.common.log.MouseChshLog import mousechsh_logging, mousechsh_logging_exception
from com.mousechsh.common.middle.err.MouseChshException import mousechsh_exception_catcher

_MouseChshRpcFunc = {}


@mousechsh_annotation
def mousechsh_rpc_func_annotation(func, name):
	try:
		attr = mousechsh_annotation_get(func)
		if attr.get('mousechsh_rpc_func_annotation', None) is None:
			return
		if name is None:
			return
		mousechsh_logging("加载RPC函数【", name, "】")
		_MouseChshRpcFunc[name] = func
	except Exception as ex:
		mousechsh_logging_exception(ex, "加载RPC函数时遇到错误：")

	def mousechsh_rpc_func_annotation_wrapper(*args_arr, **args_dict):
		return func(*args_arr, **args_dict)

	return mousechsh_rpc_func_annotation_wrapper


def mousechsh_rpc_func_call(rpc_method, data):
	try:
		if not rpc_method:
			return None
		mousechsh_logging("执行RPC函数【", rpc_method, "】")
		obj = _MouseChshRpcFunc.get(rpc_method, None)
		if obj is None:
			mousechsh_logging("RPC函数【", rpc_method, "】不存在")
			return None
		res = obj(data)
		return res
	except Exception as ex:
		return mousechsh_exception_catcher(ex, text="执行命令时遇到错误：")
