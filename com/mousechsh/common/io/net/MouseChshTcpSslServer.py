#! /usr/bin/python3
# -*- coding: UTF-8 -*-

if __name__ == "__main__":
	raise Exception("不支持从这里调用")

__version__ = "1.0"
__all__ = ["MouseChshTcpSslServer"]

import socket
import ssl

from com.mousechsh.common.io.net.MouseChshTcpServer import MouseChshTcpServer, mousechsh_tcp_server_listen
from com.mousechsh.common.log.MouseChshLog import mousechsh_logging_exception, mousechsh_logging


class MouseChshTcpSslServer(MouseChshTcpServer):

	def __init__(self):
		super().__init__()
		self.__pk_path = ''
		self.__key_path = ''
		self.__ssl_context = None
		self.__origin_socket = None
		self.set_exceptions((BlockingIOError, ssl.SSLWantReadError))

	def set_pk_path(self, value):
		if value:
			self.__pk_path = str(value)

	def set_key_path(self, value):
		if value:
			self.__key_path = str(value)

	def run(self):
		if self.get_socket() or self.__ssl_context or self.__origin_socket:
			return
		try:
			self.__ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
			self.__ssl_context.load_cert_chain(self.__pk_path, self.__key_path)

			self.__origin_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			self.__origin_socket.setsockopt(socket.SOL_SOCKET, socket.SO_KEEPALIVE, 1)
			self.__origin_socket.ioctl(
				socket.SIO_KEEPALIVE_VALS, (
					1,
					60 * 1000,
					30 * 1000
				)
			)
			mousechsh_logging("开始用证书加密监听【", self.get_host(), "】【", self.get_port(), "】……")
			self.__origin_socket.bind((self.get_host(), self.get_port()))
			self.__origin_socket.listen(1)

			self.set_socket(self.__ssl_context.wrap_socket(self.__origin_socket, server_side=True))
			self.set_loop(True)
			mousechsh_tcp_server_listen(self)
		except Exception as ex:
			mousechsh_logging_exception(ex, "建立证书加密的服务器套接字时遇到错误：")

	def close(self):
		super().close()
		if not self.__origin_socket:
			return
		try:
			self.__origin_socket.close()
		except Exception as ex:
			mousechsh_logging_exception(ex, "关闭证书加密的服务器的外层套接字时遇到错误：")
