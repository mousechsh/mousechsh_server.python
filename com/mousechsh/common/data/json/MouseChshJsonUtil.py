#! /usr/bin/python3
# -*- coding: UTF-8 -*-

if __name__ == "__main__":
	raise Exception("不支持从这里调用")

__version__ = "1.0"
__all__ = [
	"mousechsh_json_util_to_json",
	"mousechsh_json_util_from_json"
]

import json

from com.mousechsh.common.data.MouseChshModel import MouseChshModel
from com.mousechsh.common.log.MouseChshLog import mousechsh_logging_exception


class _MouseChshJsonUtilEncoder(json.JSONEncoder):

	def default(self, obj):
		if isinstance(obj, MouseChshModel):
			return obj.data()
		elif isinstance(obj, bytes):
			return str(obj, encoding='UTF-8')
		return super().default(obj)


def mousechsh_json_util_to_json(obj):
	result = json.dumps(obj, cls=_MouseChshJsonUtilEncoder, ensure_ascii=False)
	return result


def mousechsh_json_util_from_json(json_obj, fallback=None):
	if json_obj is None:
		return fallback
	json_obj = str(json_obj).strip()
	if not json_obj:
		return fallback
	try:
		result = json.loads(json_obj)
		return result
	except Exception as ex:
		mousechsh_logging_exception(ex, "数据【", json_obj, "】转换JSON对象时遇到错误：")
		return fallback
