#! /usr/bin/python3
# -*- coding: UTF-8 -*-

if __name__ == "__main__":
	raise Exception("不支持从这里调用")

__version__ = "1.0"
__all__ = [
	"MouseChshRpcClient",
	"mousechsh_rpc_caller_annotation",
]

from com.mousechsh.common.code.MouseChshAnnotation import mousechsh_annotation
from com.mousechsh.common.data.json.MouseChshJsonUtil import mousechsh_json_util_to_json, mousechsh_json_util_from_json
from com.mousechsh.common.io.net.MouseChshTcpClient import MouseChshTcpClient
from com.mousechsh.common.log.MouseChshLog import mousechsh_logging_exception


class MouseChshRpcClient(MouseChshTcpClient):

	def sync(self, data):
		text = mousechsh_json_util_to_json(data)
		res_str = super().sync(text)
		try:
			return mousechsh_json_util_from_json(res_str)
		except Exception as ex:
			mousechsh_logging_exception(ex, '处理JSON格式数据出错：')
			return {}


@mousechsh_annotation
def mousechsh_rpc_caller_annotation(func, target):
	def mousechsh_rpc_caller_annotation_wrapper(data):
		dict_data = {'target': target, 'data': data}
		client = MouseChshRpcClient()
		client.run()
		result = client.sync(dict_data)
		return func(result)

	return mousechsh_rpc_caller_annotation_wrapper
