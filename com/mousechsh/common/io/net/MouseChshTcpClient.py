#! /usr/bin/python3
# -*- coding: UTF-8 -*-

if __name__ == "__main__":
	raise Exception("不支持从这里调用")

__version__ = "1.0"
__all__ = ["MouseChshTcpClient"]

import socket

from com.mousechsh.common.log.MouseChshLog import mousechsh_logging, mousechsh_logging_data, mousechsh_logging_exception
from com.mousechsh.common.sys.MouseChshHostPort import MouseChshHostPort


class MouseChshTcpClient(MouseChshHostPort):
	"""
	TCP客户端
	"""

	def __init__(self):
		super().__init__()
		self.__socket = None

	def get_socket(self):
		return self.__socket

	def set_socket(self, value):
		self.__socket = value

	def run(self):
		if self.__socket:
			return
		try:
			self.__socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			self.__socket.setsockopt(socket.SOL_SOCKET, socket.SO_KEEPALIVE, 1)
			self.__socket.ioctl(
				socket.SIO_KEEPALIVE_VALS, (
					1,
					60 * 1000,
					30 * 1000
				)
			)
			mousechsh_logging("开始连接【", self.get_host(), "】【", self.get_port(), "】……")
			self.__socket.connect((self.get_host(), self.get_port()))
		except Exception as ex:
			mousechsh_logging_exception(ex, "建立客户端套接字时遇到错误：")

	def sync(self, text):
		mousechsh_logging_data(text, '发送并接收数据，发送的数据：')
		if self.__socket:
			data = text.encode("utf-8") if text else None
			self.__socket.sendall(data)
			response = b''
			while True:
				data = self.__socket.recv(1024)
				response += data
				if len(data) < 1024:
					break
			res_str = response.decode("utf-8 ")
			mousechsh_logging_data(res_str, '发送并接收数据，接收的数据：')
			return res_str

	def close(self):
		if not self.__socket:
			return
		try:
			self.__socket.close()
		except Exception as ex:
			mousechsh_logging_exception(ex, "关闭客户端套接字时遇到错误：")
