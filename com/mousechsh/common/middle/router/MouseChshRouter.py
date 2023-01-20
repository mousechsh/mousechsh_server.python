#! /usr/bin/python3
# -*- coding: UTF-8 -*-

if __name__ == "__main__":
	raise Exception("不支持从这里调用")

__version__ = "1.0"
__all__ = [
	"MouseChshRouter",
	"mousechsh_router_register",
	"mousechsh_router_check",
	"mousechsh_router_get_call",
	"mousechsh_router_call",
	"mousechsh_router_annotation"
]

from inspect import isfunction

from com.mousechsh.common.code.MouseChshAnnotation import mousechsh_annotation
from com.mousechsh.common.log.MouseChshLog import mousechsh_logging, mousechsh_logging_data, mousechsh_logging_exception
from com.mousechsh.common.middle.url.MouseChshUrl import MouseChshUrl

_MouseChshRouter = {}


class MouseChshRouter(MouseChshUrl):

	def __init__(self):
		super().__init__()
		self.__match = None
		self.__callback = None

	def set_match(self, func):
		if isfunction(func):
			self.__match = func

	def match(self, idx, url):
		if self.__match:
			try:
				return bool(self.__match(idx, url))
			except Exception as ex:
				mousechsh_logging_exception(ex, '路由匹配时遇到错误：')
				return False
		return True

	def set_callback(self, func):
		if isfunction(func):
			self.__callback = func

	def callback(self, *args_arr, **args_dict):
		if self.__callback:
			try:
				return self.__callback(*args_arr, **args_dict)
			except Exception as ex:
				mousechsh_logging_exception(ex, '执行路由回调时遇到错误：')


def mousechsh_router_register(router):
	if router is None:
		return
	if not isinstance(router, MouseChshRouter):
		return

	data = _MouseChshRouter
	depth = router.get_path_depth()
	for i in range(0, depth + 1):
		if depth == i:
			data[''] = router
		else:
			item = router.get_path(i)
			if item not in data:
				data[item] = {}
			data = data[item]
	mousechsh_logging_data(_MouseChshRouter, '已注册一个路由，当前的路由表为：')


def mousechsh_router_check(router):
	if router is None:
		return None
	if not isinstance(router, MouseChshRouter):
		return None

	data = _MouseChshRouter
	depth = router.get_path_depth()
	for i in range(0, depth + 1):
		if depth == i:
			return data.get('', None)
		else:
			item = router.get_path(i)
			if item not in data:
				return None
			data = data[item]

	return None


def mousechsh_router_get_call(url):
	if isinstance(url, str):
		obj = MouseChshUrl()
		obj.parse(url)
		url = obj
	mousechsh_logging_data(url.get_path(), '开始匹配如下地址的路由：')
	route = None
	if isinstance(url, MouseChshUrl):
		idx = -1
		depth = url.get_path_depth()
		data = _MouseChshRouter
		while idx < depth:
			if data is None:
				break
			path_split = url.get_path(idx) if idx >= 0 else ''
			item = data.get('', None)
			mousechsh_logging_data(
				data, '正在处理层级【', (idx if idx >= 0 else '根'), '】，对应的路径片段为【', path_split, '】，对应的路由表：'
			)
			if item:
				mousechsh_logging_data(
					item, '层级【', (idx if idx >= 0 else '根'), '】，对应的路径片段为【', path_split, '】，有路由对象：'
				)
				if item.match(idx, url):
					mousechsh_logging(
						'层级【', (idx if idx >= 0 else '根'), '】，对应的路径片段为【', path_split, '】的匹配处理结果为：【成功】'
					)
					route = item
				else:
					mousechsh_logging(
						'层级【', (idx if idx >= 0 else '根'), '】，对应的路径片段为【', path_split, '】的匹配处理结果为：【失败】'
					)
			idx += 1
			path_split = url.get_path(idx)
			ndict = data.get(path_split, None)
			if ndict is None and path_split is not None:
				if not path_split.startswith('<') and not path_split.endswith('>'):
					for k in data:
						if k.startswith('<int ') and path_split.isdecimal():
							ndict = data[k]
							tk = k[5:].lstrip().rstrip().rstrip('>').rstrip()
							url.set_search(tk, path_split)
							break
						elif k.startswith('<str ') and isinstance(path_split, str):
							ndict = data[k]
							tk = k[5:].lstrip().rstrip().rstrip('>').rstrip()
							url.set_search(tk, path_split)
							break
			data = ndict
	return route


def mousechsh_router_call(url, *args_arr, **args_dict):
	route = mousechsh_router_get_call(url)
	if route is None:
		mousechsh_logging('没有匹配的路由，将不做处理')
	else:
		mousechsh_logging_data(route.get_path(), '执行如下路由对应的函数：')
		route.callback(url, *args_arr, **args_dict)


@mousechsh_annotation
def mousechsh_router_annotation(func, path):
	mousechsh_logging_data(path, '发现可用的路由：')
	router = MouseChshRouter()
	router.parse(path)
	router.set_callback(func)
	mousechsh_router_register(router)
