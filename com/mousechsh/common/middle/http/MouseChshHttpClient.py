#! /usr/bin/python3
# -*- coding: UTF-8 -*-

if __name__ == "__main__":
	raise Exception("不支持从这里调用")

__version__ = "1.0"
__all__ = ["MouseChshHttpClient"]

from com.mousechsh.common.io.net.MouseChshTcpClient import MouseChshTcpClient
from com.mousechsh.common.middle.http.MouseChshHttpRequest import MouseChshHttpRequest
from com.mousechsh.common.middle.http.MouseChshHttpResponse import MouseChshHttpResponse


class MouseChshHttpClient(MouseChshTcpClient):

	def __init__(self):
		super().__init__()
		self.__request = MouseChshHttpRequest()

	def set_method(self, value):
		self.__request.set_method(value)

	def set_path(self, value):
		self.__request.set_path(value)

	def set_version(self, value):
		self.__request.set_version(value)

	def set_header(self, key, value):
		self.__request.get_header().set(key, value)

	def sync(self, text):
		self.__request.set_body(text)
		res_str = super().sync(self.__request.to_string())
		response = MouseChshHttpResponse()
		response.parse(res_str)
		return response

	def forgery_header(self):
		self.__request.get_header().set_content_type('txt')
		self.__request.get_header().set('Accept', '*/*')
		self.__request.get_header().set('Accept-Language', 'zh-CN')
		self.__request.get_header().set('Origin', 'http' + '://' + self.get_host() + ':' + str(self.get_port()))
		self.__request.get_header().set('Referer', 'http://127.0.0.1/')
		self.__request.get_header().set(
			'User-Agent',
			'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
			'AppleWebKit (KHTML, like Gecko) Chrome Safari Edg '
			'Python(MouseChshHttpClient)'
		)
