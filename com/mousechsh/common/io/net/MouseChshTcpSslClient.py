#! /usr/bin/python3
# -*- coding: UTF-8 -*-

if __name__ == "__main__":
	raise Exception("不支持从这里调用")

__version__ = "1.0"
__all__ = ["MouseChshTcpSslClient"]

import socket
import ssl

from com.mousechsh.common.io.net.MouseChshTcpClient import MouseChshTcpClient
from com.mousechsh.common.log.MouseChshLog import mousechsh_logging, mousechsh_logging_exception


class MouseChshTcpSslClient(MouseChshTcpClient):

	def __init__(self):
		super().__init__()
		self.__ca_path = ''
		self.__hostname = ''
		self.__ssl_context = None
		self.__origin_socket = None

	def set_hostname(self, value):
		if value:
			self.__hostname = str(value)

	def set_ca_path(self, value):
		if value:
			self.__ca_path = str(value)

	def run(self):
		if self.get_socket() or self.__ssl_context or self.__origin_socket:
			return
		try:
			self.__ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
			self.__ssl_context.load_verify_locations(self.__ca_path)

			self.__origin_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			self.__origin_socket.setsockopt(socket.SOL_SOCKET, socket.SO_KEEPALIVE, 1)
			self.__origin_socket.ioctl(
				socket.SIO_KEEPALIVE_VALS, (
					1,
					60 * 1000,
					30 * 1000
				)
			)
			mousechsh_logging("开始用证书加密连接【", self.get_host(), "】【", self.get_port(), "】……")
			self.__origin_socket.connect((self.get_host(), self.get_port()))
			self.set_socket(self.__ssl_context.wrap_socket(self.__origin_socket, server_hostname=self.__hostname))
		except Exception as ex:
			mousechsh_logging_exception(ex, "建立证书加密的客户端套接字时遇到错误：")

	def close(self):
		super().close()
		if not self.__origin_socket:
			return
		try:
			self.__origin_socket.close()
		except Exception as ex:
			mousechsh_logging_exception(ex, "关闭证书加密的客户端的外层套接字时遇到错误：")
