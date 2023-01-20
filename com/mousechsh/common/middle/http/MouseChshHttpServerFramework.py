#! /usr/bin/python3
# -*- coding: UTF-8 -*-

if __name__ == "__main__":
	raise Exception("不支持从这里调用")

__version__ = "1.0"
__all__ = [
	"MouseChshHttpServerFramework",
]

from com.mousechsh.common.data.json.MouseChshJsonUtil import mousechsh_json_util_from_json
from com.mousechsh.common.log.MouseChshLog import mousechsh_logging_data
from com.mousechsh.common.middle.http.MouseChshHttpConst import MOUSECHSH_HTTP_METHOD_POST
from com.mousechsh.common.middle.http.MouseChshHttpRequest import MouseChshHttpRequest
from com.mousechsh.common.middle.http.MouseChshHttpResponse import mousechsh_http_response_200
from com.mousechsh.common.middle.router.MouseChshHttpRouter import mousechsh_http_router_call
from com.mousechsh.common.middle.url.MouseChshUrl import MouseChshUrl
from com.mousechsh.common.util.MouseChshCodeUtil import mousechsh_codec, mousechsh_code_util_type_bytes, \
	mousechsh_code_util_type_utf8string


class MouseChshHttpServerFramework:

	def __init__(self, *, protocol='http'):
		self.__path_prefix = ''
		self.__enable_handler = True
		if protocol == 'http':
			self.__protocol = 'http'
		elif protocol == 'https':
			self.__protocol = 'https'

	def enable_handler(self):
		self.__enable_handler = True

	def disable_handler(self):
		self.__enable_handler = False

	def set_path_prefix(self, pre):
		if not pre:
			return
		self.__path_prefix = str(pre)

	def proc(self, sn, net_id, request):
		if len(request) == 0:
			return {
				'': None,
				'conn': True,
				'reset': True,
			}
		request = mousechsh_codec(
			request,
			source_type=mousechsh_code_util_type_bytes,
			target_type=mousechsh_code_util_type_utf8string
		)
		mousechsh_logging_data(request, "请求内容展开：")
		req = MouseChshHttpRequest()
		if self.__enable_handler:
			req.parse(request)
		else:
			tmp = mousechsh_json_util_from_json(request, {})
			req.set_method(tmp.get('method', MOUSECHSH_HTTP_METHOD_POST))
			req.set_path(tmp.get('path', '/'))
			req.get_header().append(tmp.get('headers', {}))
			req.set_body(tmp.get('body', ''))

		response = mousechsh_http_response_200()
		response.get_header().set_content_type('html')

		self.render(req, response)

		if self.__enable_handler:
			result = response.to_string()
		else:
			result = response.get_body()
		mousechsh_logging_data(result, "响应内容展开：")
		return {
			'': mousechsh_codec(
				result,
				source_type=mousechsh_code_util_type_utf8string,
				target_type=mousechsh_code_util_type_bytes
			),
			'conn': False,
			'reset': False,
		}

	def render(self, request, response):
		url = MouseChshUrl()
		url.parse(self.__protocol + '://' + request.get_header().get('Host') + request.get_path())
		url.replace_path(self.__path_prefix, '')
		url.append_path('<' + request.get_method() + '>')
		mousechsh_logging_data(url.to_string(), '解析出的资源地址：')
		mousechsh_http_router_call(url, request, response)
