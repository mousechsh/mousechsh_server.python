#! /usr/bin/python3
# -*- coding: UTF-8 -*-

if __name__ == "__main__":
	raise Exception("不支持从这里调用")

__version__ = "1.0"
__all__ = [
	"MouseChshFastCgiServer",
	"mousechsh_fastcgi_server_runner"
]

import struct

from com.mousechsh.common.io.net.MouseChshTcpServer import MouseChshTcpServer
from com.mousechsh.common.log.MouseChshLog import mousechsh_logging_data
from com.mousechsh.common.middle.err.MouseChshException import mousechsh_exception_catcher
from com.mousechsh.common.middle.http.MouseChshHttpConst import MOUSECHSH_HTTP_METHOD_GET
from com.mousechsh.common.middle.http.MouseChshHttpRequest import MouseChshHttpRequest
from com.mousechsh.common.middle.http.MouseChshHttpResponse import MouseChshHttpResponse
from com.mousechsh.common.middle.http.MouseChshHttpServerFramework import MouseChshHttpServerFramework
from com.mousechsh.common.sys.MouseChshThread import mousechsh_thread_annotation
from com.mousechsh.common.util.MouseChshCodeUtil import mousechsh_codec, mousechsh_code_util_type_bytes, \
	mousechsh_code_util_type_utf8string


class MouseChshFastCgiServer(MouseChshHttpServerFramework, MouseChshTcpServer):

	def __init__(self):
		super().__init__()
		super(MouseChshHttpServerFramework, self).__init__()

	def proc(self, sn, net_id, request):
		content = request
		fast_cgi_data = {}
		param_data = {}
		content_data = ''
		while True:
			data = content[0: 8]
			content = content[8:]
			if not content:
				break

			(
				fast_cgi_data['version'],
				fast_cgi_data['type'],
				fast_cgi_data['request'],
				fast_cgi_data['contentLength'],
				fast_cgi_data['paddingLength'],
				fast_cgi_data['reserved']
			) = struct.unpack('!BBHHBB', data)

			data = content[0: fast_cgi_data['contentLength'] + fast_cgi_data['paddingLength']]
			content = content[fast_cgi_data['contentLength'] + fast_cgi_data['paddingLength']:]

			data = data[0: fast_cgi_data['contentLength']]

			if not content:
				break

			if fast_cgi_data['type'] == 1:  # FCGI_BEGIN_REQUEST
				(
					fast_cgi_data['role'],
					fast_cgi_data['flags'],
					fast_cgi_data['reserved']
				) = struct.unpack('!HB5s', data)
			elif fast_cgi_data['type'] == 2:  # FCGI_ABORT_REQUEST
				return {
					'': b'',
					'conn': False,
					'reset': False,
				}
			elif fast_cgi_data['type'] == 3:  # FCGI_END_REQUEST
				(
					fast_cgi_data['appStatus'],
					fast_cgi_data['protocolStatus'],
					fast_cgi_data['reserved']
				) = struct.unpack('!IB3s', data)
				break
			elif fast_cgi_data['type'] == 4:  # FCGI_PARAMS
				def mousechsh_fastcgi_server_proc(data_string):
					param_temp = data_string[0]
					if param_temp & 0x80 != 0:
						param_temp = data_string[0: 4]
						data_string = data_string[4:]
						param_temp = \
							((param_temp[0] & 0x7f) << 24) + \
							(param_temp[1] << 16) + \
							(param_temp[2] << 8) + \
							param_temp[3]
					else:
						data_string = data_string[1:]
					return param_temp, data_string

				while data:
					(param_key, data) = mousechsh_fastcgi_server_proc(data)
					(param_value, data) = mousechsh_fastcgi_server_proc(data)
					param_data_key = data[0: param_key]
					data = data[param_key:]
					param_data_value = data[0: param_value]
					data = data[param_value:]
					param_data[
						mousechsh_codec(
							param_data_key,
							source_type=mousechsh_code_util_type_bytes,
							target_type=mousechsh_code_util_type_utf8string
						)
					] = mousechsh_codec(
						param_data_value,
						source_type=mousechsh_code_util_type_bytes,
						target_type=mousechsh_code_util_type_utf8string
					)
			elif fast_cgi_data['type'] == 5:  # FCGI_STDIN
				content_data = mousechsh_codec(
					data,
					source_type=mousechsh_code_util_type_bytes,
					target_type=mousechsh_code_util_type_utf8string
				)
			elif fast_cgi_data['type'] == 6:  # FCGI_STDOUT
				pass
			elif fast_cgi_data['type'] == 7:  # FCGI_STDERR
				pass
			elif fast_cgi_data['type'] == 8:  # FCGI_DATA
				pass
			elif fast_cgi_data['type'] == 9:  # FCGI_GET_VALUES
				pass
			elif fast_cgi_data['type'] == 10:  # FCGI_GET_VALUES_RESULT
				pass
			elif fast_cgi_data['type'] == 11:  # FCGI_UNKNOWN_TYPE
				break
			else:  # FCGI_MAX_TYPE ( FCGI_UNKNOWN_TYPE )
				break

		try:
			req = MouseChshHttpRequest()
			header = req.get_header()

			search = param_data.get('QUERY_STRING', None)

			req.set_method(param_data.get('REQUEST_METHOD', MOUSECHSH_HTTP_METHOD_GET))
			if search is None:
				req.set_path(param_data.get('SCRIPT_NAME', '/'))
			else:
				req.set_path(param_data.get('SCRIPT_NAME', '/') + '?' + search)
			req.set_body(content_data)

			for param_item in param_data:
				if param_item.startswith('HTTP_'):
					header.set(param_item[5:], param_data[param_item])

			response = MouseChshHttpResponse()
			response.set_status_code(200)
			response.get_header().set_content_type('html')

			mousechsh_logging_data(req.to_string(), "请求内容展开：")

			self.render(req, response)

			result = response.to_string()
			mousechsh_logging_data(result, "响应内容展开：")

			output = b''

			output += struct.pack('!BBHHBB', *[
				fast_cgi_data['version'],
				6,
				fast_cgi_data['request'],
				len(result),
				0,
				0
			])
			output += mousechsh_codec(
				result,
				source_type=mousechsh_code_util_type_utf8string,
				target_type=mousechsh_code_util_type_bytes
			)
			output += struct.pack('!BBHHBB', *[
				fast_cgi_data['version'],
				3,
				fast_cgi_data['request'],
				8,
				0,
				0
			])
			output += struct.pack('!IB3s', *[
				0,
				0,
				b'\0\0\0'
			])

			return {
				'': output,
				'conn': False,
				'reset': False,
			}
		except Exception as ex:
			return {
				'': mousechsh_exception_catcher(ex, text='处理传入数据出错：'),
				'conn': False,
				'reset': False,
			}


@mousechsh_thread_annotation(name='MouseChshFastCgiServer')
def mousechsh_fastcgi_server_runner(host=None, port=None):
	server = MouseChshFastCgiServer()
	if host is not None:
		server.set_host(host)
	if port is not None:
		server.set_port(port)
	server.run()
	return server
