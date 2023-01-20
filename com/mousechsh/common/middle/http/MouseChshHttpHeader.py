#! /usr/bin/python3
# -*- coding: UTF-8 -*-

if __name__ == "__main__":
	raise Exception("不支持从这里调用")

__version__ = "1.0"
__all__ = [
	"MouseChshHttpHeader",
	"mousechsh_http_header_accept_language_single",
	"mousechsh_http_header_accept_language_annotation",
	"mousechsh_http_header_authorization",
	"mousechsh_http_header_authorization_annotation"
]

from com.mousechsh.common.code.MouseChshAnnotation import mousechsh_annotation
from com.mousechsh.common.middle.auth.MouseChshJwt import mousechsh_jwt_decode_string
from com.mousechsh.common.middle.conf.MouseChshConfiguration import mousechsh_configuration_get


class MouseChshHttpHeader:
	__enable_capitalize = True

	def __init__(self):
		self.__data = {}

	def enable_capitalize(self):
		self.__enable_capitalize = True

	def enable_capitalize__(self):
		self.enable_capitalize()
		return self

	def disable_capitalize(self):
		self.__enable_capitalize = True

	def disable_capitalize__(self):
		self.disable_capitalize()
		return self

	def append(self, data):
		if isinstance(data, dict):
			for item in data:
				self.set(item, data[item])

	def append__(self, data):
		self.append(data)
		return self

	def set(self, key, value=None):
		key = str(key).lower().replace('_', '-')
		if value is not None:
			self.__data[key] = value
		else:
			del self.__data[key]

	def set__(self, key, value=None):
		self.set(key, value)
		return self

	def get(self, key):
		key = str(key).lower()
		return str(self.__data.get(key, ''))

	def to_string(self):
		result = ''
		if self.__enable_capitalize:
			for key, value in self.__data.items():
				result += '-'.join(map(lambda x: x.capitalize(), str(key).split('-'))) + ': ' + str(value) + '\r\n'
		else:
			for key, value in self.__data.items():
				result += str(key) + ': ' + str(value) + '\r\n'
		return result

	def parse(self, text):
		tts = text.split('\r\n')
		for line in tts:
			idx = line.find(': ')
			if idx >= 0:
				self.set(line[0: idx], line[idx + 2:])

	def get_accept_language(self, *, first_only=False):
		result = []
		d = self.get('Accept-Language')
		if d:
			ls = d.split(',')
			for item in ls:
				lss = item.split(';')
				if lss[0]:
					result.append(lss[0])
			if len(result) == 0:
				result.append(mousechsh_configuration_get('default.language', 'zh-cn'))
		else:
			result.append(mousechsh_configuration_get('default.language', 'zh-cn'))
		if first_only:
			return result[0]
		return result

	def set_target_type(self, value):
		if value == 'all':
			self.set('WebSocket-Target-Type', 'all')
		if value == 'group':
			self.set('WebSocket-Target-Type', 'group')
		if value == 'client':
			self.set('WebSocket-Target-Type', 'client')

	def set_target_type__(self, value):
		self.set_target_type(value)
		return self

	def get_target_type(self):
		d = self.get('WebSocket-Target-Type')
		if d == 'all':
			return 'all'
		if d == 'group':
			return 'group'
		return 'client'

	def set_target_id(self, value):
		self.set('WebSocket-Target-Id', str(value))

	def set_target_id__(self, value):
		self.set_target_id(value)
		return self

	def get_target_id(self, default=''):
		result = self.get('WebSocket-Target-Id')
		if result:
			return result
		return default

	def get_content_type(self):
		d = self.get('Content-Type')
		if d == 'application/json':
			return 'json'
		if d == 'application/x-www-form-urlencoded':
			return 'search'
		if d == 'multipart/form-data':
			return 'form'
		return 'text'

	def set_content_type(self, value='none'):
		value = str(value).lower()
		if value == 'html':
			self.set('Content-Type', 'text/html; charset=UTF-8')
		elif value == 'js':
			self.set('Content-Type', 'application/javascript; charset=UTF-8')
		elif value == 'css':
			self.set('Content-Type', 'text/css; charset=UTF-8')
		elif value == 'json':
			self.set('Content-Type', 'application/json; charset=UTF-8')
		elif value == 'txt':
			self.set('Content-Type', 'text/plain; charset=UTF-8')
		elif value == 'svg':
			self.set('Content-Type', 'image/svg+xml; charset=UTF-8')
		elif value == 'none':
			self.set('Content-Type')
		else:
			self.set('Content-Type')

	def set_content_type__(self, value='none'):
		self.set_content_type(value)
		return self

	def set_content_type_options(self, flag=True):
		if flag:
			self.set('X-Content-Type-Options', 'nosniff')
		else:
			self.set('X-Content-Type-Options')

	def set_content_type_options__(self, flag=True):
		self.set_content_type_options(flag)
		return self


def mousechsh_http_header_accept_language_single(url, request):
	lang = url.get_search('lang')
	if not lang:
		lang = request.get_header().get_accept_language(first_only=True)
	if not lang:
		lang = 'zh-cn'
	return lang


@mousechsh_annotation
def mousechsh_http_header_accept_language_annotation(func):
	def mousechsh_http_header_accept_language_annotation_wrapper(url, request, response, *args_arr, **args_dict):
		lang = mousechsh_http_header_accept_language_single(url, request)
		func(url, request, response, lang=lang, *args_arr, **args_dict)

	return mousechsh_http_header_accept_language_annotation_wrapper


def mousechsh_http_header_authorization(request):
	auth_str = request.get_header().get('Authorization')
	if not auth_str:
		return {
			'type': '',
			'origin': '',
			'verify': False,
			'data': {}
		}
	index = auth_str.find(' ')
	if index >= 0:
		type_str = auth_str[0: index]
		auth_str = auth_str[index + 1:]
	else:
		type_str = ''
	auth = mousechsh_jwt_decode_string(auth_str, check=False)
	auth = dict(
		auth, **{
			'type': type_str,
			'origin': auth_str
		}
	)
	return auth


@mousechsh_annotation
def mousechsh_http_header_authorization_annotation(func):
	def mousechsh_http_header_authorization_annotation_wrapper(url, request, response, *args_arr, **args_dict):
		auth = mousechsh_http_header_authorization(request)
		func(url, request, response, auth=auth, *args_arr, **args_dict)

	return mousechsh_http_header_authorization_annotation_wrapper
