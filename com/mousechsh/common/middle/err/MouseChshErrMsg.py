#! /usr/bin/python3
# -*- coding: UTF-8 -*-

if __name__ == "__main__":
	raise Exception("不支持从这里调用")

__version__ = "1.0"
__all__ = ["MouseChshErrMsg"]

import enum
from enum import unique


@unique
class MouseChshErrMsg(enum.IntEnum):
	CacheRedisError = 1501
	RpcCallSuccess = 5000
	RpcRequestNeedTarget = 5001
	RpcRequestTargetFuncNone = 5002
	RpcRequestNoData = 5003
	JsonConvertFrom = 9999

	@staticmethod
	def text(item):
		if item == MouseChshErrMsg.CacheRedisError:
			return 'Redis调用失败'
		if item == MouseChshErrMsg.RpcCallSuccess:
			return 'RPC调用成功'
		if item == MouseChshErrMsg.RpcRequestNeedTarget:
			return 'RPC调用请求需要一个target参数'
		if item == MouseChshErrMsg.RpcRequestTargetFuncNone:
			return 'RPC调用请求的方法不存在'
		if item == MouseChshErrMsg.RpcRequestNoData:
			return 'RPC请求中不包含数据'
		if item == MouseChshErrMsg.JsonConvertFrom:
			return '处理JSON格式数据出错'
