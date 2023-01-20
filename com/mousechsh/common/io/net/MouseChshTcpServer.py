#! /usr/bin/python3
# -*- coding: UTF-8 -*-

if __name__ == "__main__":
	raise Exception("不支持从这里调用")

__version__ = "1.0"
__all__ = [
	"MouseChshTcpServer",
	"mousechsh_tcp_server_listen",
]

import socket
import time

from com.mousechsh.common.log.MouseChshLog import mousechsh_logging, mousechsh_logging_data, mousechsh_logging_exception
from com.mousechsh.common.sys.MouseChshHostPort import MouseChshHostPort
from com.mousechsh.common.sys.MouseChshThread import mousechsh_thread_annotation, mousechsh_thread_sleep
from com.mousechsh.common.util.MouseChshCodeUtil import mousechsh_codec, mousechsh_code_util_type_utf8string, \
	mousechsh_code_util_type_bytes

_mousechsh_tcp_server_max_request_length = 10 * 1024
_mousechsh_tcp_server_max_blank_request_per_second = 10


class MouseChshTcpServer(MouseChshHostPort):
	"""
	TCP服务端
	"""

	def __init__(self):
		super().__init__()
		self.__socket = None
		self.__loop = False
		self.__exceptions = (BlockingIOError,)

	def set_exceptions(self, value):
		self.__exceptions = value

	def get_exceptions(self):
		return self.__exceptions

	def get_loop(self):
		return self.__loop

	def set_loop(self, value):
		self.__loop = bool(value)

	def get_socket(self):
		"""
		获取套接字对象
		"""
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
			mousechsh_logging("开始监听【", self.get_host(), "】【", self.get_port(), "】……")
			self.__socket.bind((self.get_host(), self.get_port()))
			self.__socket.listen(1)
			self.__loop = True
			mousechsh_tcp_server_listen(self)
		except Exception as ex:
			mousechsh_logging_exception(ex, "建立服务器套接字时遇到错误：")

	def proc(self, sn, net_id, request):
		return {
			'': mousechsh_codec(
				'MouseChshServer-' + str(net_id) + '#' + str(sn),
				source_type=mousechsh_code_util_type_utf8string,
				target_type=mousechsh_code_util_type_bytes
			),
			'conn': False,
			'reset': False,
		}

	def close(self):
		if not self.__socket:
			return
		try:
			self.__socket.close()
		except Exception as ex:
			mousechsh_logging_exception(ex, "关闭服务器套接字时遇到错误：")
		self.__loop = False


@mousechsh_thread_annotation(name='MouseChshTcpServerListen')
def mousechsh_tcp_server_listen(server):
	while server.get_loop():
		try:
			client_connection, client_address = server.get_socket().accept()
			client_connection.setblocking(False)
			_mousechsh_tcp_server_processing(server, client_connection, client_address)
		except Exception as ex:
			mousechsh_logging_exception(ex, "监听套接字时遇到错误：")


@mousechsh_thread_annotation(name='MouseChshTcpServerProcessing')
def _mousechsh_tcp_server_processing(server, client_connection, client_address):
	try:
		mousechsh_logging("开始接收来自【", client_address, "】的请求")
		base_timer = time.time()
		request = b''
		flag_conn = True
		count_request = 0
		while flag_conn:
			timer = time.time()
			count_request += 1
			try:
				while True:
					data = client_connection.recv(1024)
					request += data
					if len(data) < 1024:
						break
					if len(request) > _mousechsh_tcp_server_max_request_length:
						raise Exception(
							'超过可以接受的最大请求大小，阈值为：' + str(_mousechsh_tcp_server_max_request_length)
						)
				mousechsh_logging_data(request, "来自【", client_address, "】的请求内容：")
			# except BlockingIOError:
			except server.get_exceptions():
				mousechsh_thread_sleep()

			if len(request) > _mousechsh_tcp_server_max_request_length:
				mousechsh_logging(
					"来自【", client_address, "】的请求已超限：请求体大小【",
					len(request),
					"】，请求体大小阈值【",
					_mousechsh_tcp_server_max_request_length,
					"】，单次用时【",
					('%0.6f' % (time.time() - timer)),
					"】，已连接时长【",
					('%0.6f' % (time.time() - base_timer)),
					"】，循环次数【",
					count_request,
					"】，调用率【",
					(count_request + 1) / (timer - base_timer + 1),
					"】"
				)
				raise Exception('超过可以接受的最大请求大小')
			if (count_request + 1) / (timer - base_timer + 1) \
				> _mousechsh_tcp_server_max_blank_request_per_second:
				mousechsh_logging(
					"对【", client_address, "】的警报：单次用时【",
					('%0.6f' % (time.time() - timer)),
					"】，已连接时长【",
					('%0.6f' % (time.time() - base_timer)),
					"】，循环次数【",
					count_request,
					"】，调用率【",
					(count_request + 1) / (timer - base_timer + 1),
					"】"
				)
				raise Exception('过于频繁的空请求')

			res_dict = server.proc(count_request, str(client_address), request)
			if res_dict is None:
				res_dict = {
					'': None,
					'conn': False,
					'reset': False,
				}
			response = res_dict['']

			if response:
				client_connection.sendall(response)
				mousechsh_logging_data(
					res_dict, "对【", client_address, "】的响应，单次用时【",
					('%0.6f' % (time.time() - timer)),
					"】，已连接时长【",
					('%0.6f' % (time.time() - base_timer)),
					"】，循环次数【",
					count_request,
					"】，调用率【",
					(count_request + 1) / (timer - base_timer + 1),
					"】，响应内容："
				)
			flag_conn = bool(res_dict['conn'])
			if bool(res_dict['reset']):
				request = b''
	except Exception as ex:
		mousechsh_logging_exception(ex, "TCP服务端在执行处理代码时遇到错误：")
	finally:
		try:
			client_connection.close()
			mousechsh_logging("与【", client_address, "】的连接已断开")
		except Exception as ex:
			mousechsh_logging_exception(ex, "TCP服务端在断开连接时遇到错误：")
