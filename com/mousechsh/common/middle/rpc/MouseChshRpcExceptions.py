#! /usr/bin/python3
# -*- coding: UTF-8 -*-

if __name__ == "__main__":
	raise Exception("不支持从这里调用")

__version__ = "1.0"
__all__ = [
	"MouseChshRpcJsonConvertFromException",
	"MouseChshRpcRequestNeedTargetException",
	"MouseChshRpcRequestTargetFuncNoneException",
]

from com.mousechsh.common.data.json.MouseChshJsonUtil import mousechsh_json_util_to_json
from com.mousechsh.common.middle.err.MouseChshErrMsg import MouseChshErrMsg
from com.mousechsh.common.middle.err.MouseChshException import MouseChshException


class MouseChshRpcJsonConvertFromException(MouseChshException):

	def text(self):
		return MouseChshErrMsg.text(MouseChshErrMsg.JsonConvertFrom) + "："

	def error(self, *args_arr):
		return mousechsh_json_util_to_json(
			{
				'code': MouseChshErrMsg.JsonConvertFrom.value,
				'message': MouseChshErrMsg.text(MouseChshErrMsg.JsonConvertFrom),
			}
		)


class MouseChshRpcRequestNeedTargetException(MouseChshException):

	def text(self):
		return MouseChshErrMsg.text(MouseChshErrMsg.RpcRequestNeedTarget) + "："

	def error(self, *args_arr):
		return mousechsh_json_util_to_json(
			{
				'code': MouseChshErrMsg.RpcRequestNeedTarget.value,
				'message': MouseChshErrMsg.text(MouseChshErrMsg.RpcRequestNeedTarget),
			}
		)


class MouseChshRpcRequestTargetFuncNoneException(MouseChshException):

	def text(self):
		return MouseChshErrMsg.text(MouseChshErrMsg.RpcRequestTargetFuncNone) + "："

	def error(self, *args_arr):
		return mousechsh_json_util_to_json(
			{
				'code': MouseChshErrMsg.RpcRequestTargetFuncNone.value,
				'message': MouseChshErrMsg.text(MouseChshErrMsg.RpcRequestTargetFuncNone),
			}
		)


class MouseChshRpcRequestNoDataException(MouseChshException):

	def text(self):
		return MouseChshErrMsg.text(MouseChshErrMsg.RpcRequestNoData) + "："

	def error(self, *args_arr):
		return mousechsh_json_util_to_json(
			{
				'code': MouseChshErrMsg.RpcRequestNoData.value,
				'message': MouseChshErrMsg.text(MouseChshErrMsg.RpcRequestNoData),
			}
		)
