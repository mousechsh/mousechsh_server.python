#! /usr/bin/python3
# -*- coding: UTF-8 -*-

if __name__ == "__main__":
	raise Exception("不支持从这里调用")

__version__ = "1.0"
__all__ = [
	"MouseChshHttpResponse",
	"mousechsh_http_response_200",
	"mousechsh_http_response_403",
	"mousechsh_http_response_404",
]

from com.mousechsh.common.middle.http.MouseChshHttpConst import MOUSECHSH_HTTP_STATUS, MOUSECHSH_HTTP_VERSION_1_1
from com.mousechsh.common.middle.http.MouseChshHttpHeader import MouseChshHttpHeader
from com.mousechsh.common.util.MouseChshCodeUtil import mousechsh_codec, mousechsh_code_util_type_utf8string, \
	mousechsh_code_util_type_bytes


class MouseChshHttpResponse:

	def __init__(self):
		self.__version = MOUSECHSH_HTTP_VERSION_1_1
		self.__status_code = 0
		self.__status_display = ''
		self.__header = MouseChshHttpHeader()
		self.__body = ''
		pass

	def get_version(self):
		return str(self.__version)

	def set_version(self, value):
		self.__version = value

	def get_status_code(self):
		return str(self.__status_code)

	def set_status_code(self, value):
		self.__status_code = int(value)
		self.__status_display = MOUSECHSH_HTTP_STATUS.get(self.__status_code, 'Unknown')

	def get_status_display(self):
		return str(self.__status_display)

	def get_header(self):
		return self.__header

	def get_body(self):
		return str(self.__body)

	def set_body(self, value):
		if isinstance(value, bytes):
			value_len = len(value)
			self.__body = mousechsh_codec(
				value,
				source_type=mousechsh_code_util_type_bytes,
				target_type=mousechsh_code_util_type_utf8string
			)
			self.get_header().set('Content-Length', value_len)
		else:
			self.__body = str(value).strip()
			bin_string = mousechsh_codec(
				self.__body,
				source_type=mousechsh_code_util_type_utf8string,
				target_type=mousechsh_code_util_type_bytes
			)
			self.get_header().set('Content-Length', len(bin_string))

	def to_string(self):
		result = ''
		result += self.get_version()
		result += ' '
		result += self.get_status_code()
		result += ' '
		result += self.get_status_display()
		result += '\r\n'
		result += self.get_header().to_string()
		result += '\r\n'
		if len(self.__body) > 0:
			result += self.get_body()
			result += '\r\n\r\n'
		return result

	def parse(self, text):
		idx = text.find(' ')
		if idx < 0:
			return
		self.set_version(text[0: idx])
		text = text[idx + 1:]
		idx = text.find(' ')
		if idx < 0:
			return
		self.set_status_code(text[0: idx])
		text = text[idx + 1:]
		idx = text.find('\r\n')
		if idx < 0:
			return
		text = text[idx + 2:]

		idx = text.find('\r\n\r\n')
		if idx < 0:
			return
		self.get_header().parse(text[0: idx])

		self.set_body(text[idx + 4:])


def mousechsh_http_response_200(*, string=False):
	response = MouseChshHttpResponse()
	response.set_status_code(200)
	if string:
		return response.to_string()
	return response


def mousechsh_http_response_403(*, string=False):
	response = MouseChshHttpResponse()
	response.set_status_code(403)
	if string:
		return response.to_string()
	return response


def mousechsh_http_response_404(*, string=False):
	response = MouseChshHttpResponse()
	response.set_status_code(404)
	if string:
		return response.to_string()
	return response
