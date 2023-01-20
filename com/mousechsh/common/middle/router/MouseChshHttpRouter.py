#! /usr/bin/python3
# -*- coding: UTF-8 -*-

if __name__ == "__main__":
	raise Exception("不支持从这里调用")

__version__ = "1.0"
__all__ = [
	"MouseChshHttpRouter",
	"mousechsh_http_router_call",
	"mousechsh_http_router_annotation",
	"mousechsh_http_router_scan_files",
]

import os

from com.mousechsh.common.code.MouseChshAnnotation import mousechsh_annotation
from com.mousechsh.common.io.file.MouseChshFile import mousechsh_file_read_text
from com.mousechsh.common.log.MouseChshLog import (
	mousechsh_logging,
	mousechsh_logging_data,
)
from com.mousechsh.common.middle.http.MouseChshHttpConst import MOUSECHSH_HTTP_METHOD_POST, mousechsh_http_method_check
from com.mousechsh.common.middle.http.MouseChshHttpRequest import MouseChshHttpRequest
from com.mousechsh.common.middle.http.MouseChshHttpResponse import MouseChshHttpResponse
from com.mousechsh.common.middle.router.MouseChshRouter import (
	MouseChshRouter,
	mousechsh_router_get_call,
	mousechsh_router_register,
)
from com.mousechsh.common.middle.url.MouseChshUrl import MouseChshUrl


def _mousechsh_http_router_default_method(*, return_bool=False):
	if return_bool:
		return True
	return MOUSECHSH_HTTP_METHOD_POST


class MouseChshHttpRouter(MouseChshRouter):

	def __init__(self):
		super().__init__()
		self.__method = _mousechsh_http_router_default_method()

	def is_default_method(self):
		return self.__method == _mousechsh_http_router_default_method()

	def set_method(self, data):
		self.__method = mousechsh_http_method_check(
			data, default_post=_mousechsh_http_router_default_method(return_bool=True)
		)

	def get_method(self):
		return self.__method

	def get_path_depth(self):
		if self.is_default_method():
			return super().get_path_depth()
		return super().get_path_depth() + 1

	def get_path_with_default(self, index=-1):
		path_len = super().get_path_depth()
		if index >= path_len + 1:
			return None
		if index >= path_len:
			return '<' + self.__method + '>'
		if index < 0:
			if path_len == 0:
				return ('/' if self.get_root() else '') + '<' + self.__method + '>'
			else:
				return super().get_path() + ('/<%s>' % self.__method)
		return super().get_path(index)

	def get_path(self, index=-1):
		if self.is_default_method():
			return super().get_path(index)
		return self.get_path_with_default(index)

	def callback(self, *args_arr, **args_dict):
		if len(args_arr) < 3:
			mousechsh_logging('执行路由回调前，参数的数量不合规')
			return None
		url = args_arr[0]
		if url is None:
			mousechsh_logging('执行路由回调前，第一个应有的参数获取不到')
			return None
		if not isinstance(url, MouseChshUrl):
			mousechsh_logging('执行路由回调前，第一个参数不是所需的类型')
			return None
		last = url.get_last_path()
		if last and str(last).startswith('<') and str(last).endswith('>'):
			url.pop_path()
		request = args_arr[1]
		if request is None:
			mousechsh_logging('执行路由回调前，第二个应有的参数获取不到')
			return None
		if not isinstance(request, MouseChshHttpRequest):
			mousechsh_logging('执行路由回调前，第二个参数不是所需的类型')
			return None
		response = args_arr[2]
		if response is None:
			mousechsh_logging('执行路由回调前，第三个应有的参数获取不到')
			return None
		if not isinstance(response, MouseChshHttpResponse):
			mousechsh_logging('执行路由回调前，第三个参数不是所需的类型')
			return None
		return super().callback(*args_arr, **args_dict)


def mousechsh_http_router_register(func, method, path):
	mousechsh_logging_data(path, '发现可用的HTTP路由：')
	if isinstance(method, list):
		for item in method:
			router = MouseChshHttpRouter()
			router.set_method(item)
			router.parse(path)
			router.set_callback(func)
			mousechsh_router_register(router)
	else:
		router = MouseChshHttpRouter()
		router.set_method(method)
		router.parse(path)
		router.set_callback(func)
		mousechsh_router_register(router)


def mousechsh_http_router_call(url, *args_arr, **args_dict):
	route = mousechsh_router_get_call(url)
	if route is None:
		mousechsh_logging('没有匹配的HTTP路由，将不做处理')
	else:
		if isinstance(route, MouseChshHttpRouter):
			mousechsh_logging_data(route.get_path(), '执行如下路由对应的函数：')
			route.callback(url, *args_arr, **args_dict)
		# mousechsh_logging('【错误测试】1：', route.get_path_with_default())
		# mousechsh_logging('【错误测试】2：', url.get_path())
		# if route.get_path_with_default() == url.get_path():
		# 	mousechsh_logging_data(route.get_path(), '执行如下路由对应的函数：')
		# 	route.callback(url, *args_arr, **args_dict)
		# else:
		# 	mousechsh_logging('所找到HTTP路由的方法【' + route.get_method() + '】与请求不一致，将不做处理')
		else:
			mousechsh_logging('所找到的路由不是HTTP路由，将不做处理')


@mousechsh_annotation
def mousechsh_http_router_annotation(func, method, path):
	mousechsh_http_router_register(func, method, path)


def mousechsh_http_router_register_static_http(path, os_path):
	def _mousechsh_http_router_register_static_http(url, request, response, *argsArr, **argsDict):
		response.get_header().set_content_type__('html').set_content_type_options()
		response.set_body(mousechsh_file_read_text(os_path))

	mousechsh_http_router_register(_mousechsh_http_router_register_static_http, 'GET', path)


def mousechsh_http_router_register_static_js(path, os_path):
	def _mousechsh_http_router_register_static_js(url, request, response, *argsArr, **argsDict):
		response.get_header().set_content_type__('js').set_content_type_options()
		response.set_body(mousechsh_file_read_text(os_path))

	mousechsh_http_router_register(_mousechsh_http_router_register_static_js, 'GET', path)


def mousechsh_http_router_register_static_css(path, os_path):
	def _mousechsh_http_router_register_static_css(url, request, response, *argsArr, **argsDict):
		response.get_header().set_content_type__('css').set_content_type_options()
		response.set_body(mousechsh_file_read_text(os_path))

	mousechsh_http_router_register(_mousechsh_http_router_register_static_css, 'GET', path)


def mousechsh_http_router_scan_files(path):
	for root, dirs, files in os.walk(path):
		for name in files:
			os_path = os.path.join(root, name)
			mousechsh_logging_data(os_path, '正在扫描文件以判断是否可以注册为静态文件：')
			if str(name).endswith('.html'):
				mousechsh_http_router_register_static_http(
					os.path.relpath(os_path, path).replace('\\', '/'),
					os_path
				)
			elif str(name).endswith('.js'):
				mousechsh_http_router_register_static_js(
					os.path.relpath(os_path, path).replace('\\', '/'),
					os_path
				)
			elif str(name).endswith('.css'):
				mousechsh_http_router_register_static_css(
					os.path.relpath(os_path, path).replace('\\', '/'),
					os_path
				)
		for name in dirs:
			mousechsh_logging_data(os.path.join(root, name), '正在扫描文件夹以查找静态文件：')
