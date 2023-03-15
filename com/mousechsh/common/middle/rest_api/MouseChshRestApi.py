#! /usr/bin/python3
# -*- coding: UTF-8 -*-

if __name__ == "__main__":
	raise Exception("不支持从这里调用")

__version__ = "1.0"
__all__ = [
	"mousechsh_rest_api_annotation",
	"MouseChshRestApiException"
]

from com.mousechsh.common.code.MouseChshAnnotation import mousechsh_annotation
from com.mousechsh.common.data.json.MouseChshJsonUtil import mousechsh_json_util_from_json, mousechsh_json_util_to_json
from com.mousechsh.common.log.MouseChshLog import mousechsh_logging_exception
from com.mousechsh.common.middle.err.MouseChshException import MouseChshException


@mousechsh_annotation
def mousechsh_rest_api_annotation(func):
	def mousechsh_rest_api_annotation_wrapper(url, request, response, **args_dict):
		d = mousechsh_rest_api_request(url, request, **args_dict)
		try:
			result = func(d)
			mousechsh_rest_api_response(0, result, response)
		except Exception as ex:
			mousechsh_logging_exception(ex, 'REST API 处理函数中出现异常：')
			mousechsh_rest_api_response(-1, None, response)

	return mousechsh_rest_api_annotation_wrapper


class MouseChshRestApiException(MouseChshException):
	pass


def mousechsh_rest_api_request(url, request, **args_dict):
	d = dict(url.get_search_data(), **args_dict)
	body = mousechsh_json_util_from_json(request.get_body(), {})
	d = dict(d, **body)
	return d


def mousechsh_rest_api_response(code, result, response):
	response.get_header().set_content_type('json')
	response.set_body(
		mousechsh_json_util_to_json(
			{
				'code': code,
				'data': result
			}
		)
	)
