#! /usr/bin/python3
# -*- coding: UTF-8 -*-

if __name__ == "__main__":
	raise Exception("不支持从这里调用")

__version__ = "1.0"
__all__ = ["MouseChshRpcServer", "mousechsh_rpc_server_runner"]

from com.mousechsh.common.data.json.MouseChshJsonUtil import mousechsh_json_util_from_json, mousechsh_json_util_to_json
from com.mousechsh.common.io.net.MouseChshTcpServer import MouseChshTcpServer
from com.mousechsh.common.middle.err.MouseChshException import mousechsh_exception_catcher
from com.mousechsh.common.middle.rpc.MouseChshRpcExceptions import \
	MouseChshRpcRequestNeedTargetException, \
	MouseChshRpcRequestTargetFuncNoneException
from com.mousechsh.common.middle.rpc.MouseChshRpcFunc import mousechsh_rpc_func_call
from com.mousechsh.common.sys.MouseChshThread import mousechsh_thread_annotation
from com.mousechsh.common.util.MouseChshCodeUtil import mousechsh_codec, mousechsh_code_util_type_bytes, \
	mousechsh_code_util_type_utf8string


class MouseChshRpcServer(MouseChshTcpServer):

	def proc(self, sn, net_id, request):
		try:
			content = mousechsh_codec(
				request,
				source_type=mousechsh_code_util_type_bytes,
				target_type=mousechsh_code_util_type_utf8string
			)
			data = mousechsh_json_util_from_json(content)
			target = data.get('target', None)
			if target is None:
				raise MouseChshRpcRequestNeedTargetException()
			res_dict = mousechsh_rpc_func_call(target, data)
			if res_dict is None:
				raise MouseChshRpcRequestTargetFuncNoneException()
			return {
				'': mousechsh_json_util_to_json(res_dict),
				'conn': False,
				'reset': False,
			}
		except Exception as ex:
			return {
				'': mousechsh_exception_catcher(ex, text='处理RPC请求数据出错：'),
				'conn': False,
				'reset': False,
			}


@mousechsh_thread_annotation(name='MouseChshRpcServer')
def mousechsh_rpc_server_runner(host=None, port=None):
	server = MouseChshRpcServer()
	if host is not None:
		server.set_host(host)
	if port is not None:
		server.set_port(port)
	server.run()
	return server
