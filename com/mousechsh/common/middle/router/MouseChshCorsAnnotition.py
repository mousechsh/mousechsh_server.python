#! /usr/bin/python3
# -*- coding: UTF-8 -*-

if __name__ == "__main__":
	raise Exception("不支持从这里调用")

__version__ = "1.0"
__all__ = ["mousechsh_cors_annotation"]

from com.mousechsh.common.code.MouseChshAnnotation import mousechsh_annotation
from com.mousechsh.common.middle.http.MouseChshHttpConst import MOUSECHSH_HTTP_METHOD_OPTIONS


@mousechsh_annotation
def mousechsh_cors_annotation(func, host='*'):
	def mousechsh_cors_annotation_wrapper(url, request, response, *args_arr, **args_dict):
		if request.get_method() == MOUSECHSH_HTTP_METHOD_OPTIONS:
			response.get_header().set_content_type()
			response.get_header().set('Access-Control-Allow-Origin', request.get_header().get('Origin'))
			response.get_header().set('Access-Control-Allow-Headers', '*')
			response.get_header().set('Access-Control-Allow-Methods', 'POST, GET, PUT, DELETE, OPTIONS')
			response.get_header().set('Access-Control-Max-Age', '86400')
			response.set_body('')
			return
		else:
			response.get_header().set('Access-Control-Allow-Origin', host)
		func(url, request, response, *args_arr, **args_dict)

	return mousechsh_cors_annotation_wrapper
