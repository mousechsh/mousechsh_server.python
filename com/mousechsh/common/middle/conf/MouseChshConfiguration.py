#! /usr/bin/python3
# -*- coding: UTF-8 -*-

if __name__ == "__main__":
	raise Exception("不支持从这里调用")

__version__ = "1.0"
__all__ = [
	"mousechsh_configuration_set",
	"mousechsh_configuration_get"
]

from com.mousechsh.common.log.MouseChshLog import mousechsh_logging
from com.mousechsh.common.middle.url.MouseChshUrl import MouseChshUrl

_MouseChshConfiguration = {}


def mousechsh_configuration_set(path, value):
	mousechsh_logging('设置配置【', path, '】为【', value, '】')
	url = MouseChshUrl()
	url.parse(path.replace('.', '/'))
	url.set_protocol('config')
	depth = url.get_path_depth()
	value_dict = _MouseChshConfiguration
	for i in range(0, depth + 1):
		if depth == i:
			value_dict[''] = value
		else:
			item = url.get_path(i)
			if item not in value_dict:
				value_dict[item] = {}
			value_dict = value_dict[item]


def mousechsh_configuration_get(path=None, default=None):
	mousechsh_logging('获取配置【', path, '】')
	if path is None:
		if default is None:
			return str(_MouseChshConfiguration)
		else:
			return default
	url = MouseChshUrl()
	url.parse(path.replace('.', '/'))
	url.set_protocol('config')
	depth = url.get_path_depth()
	dict_value = _MouseChshConfiguration
	for i in range(0, depth + 1):
		if depth == i:
			v = dict_value.get('', None)
			if v is None:
				if default is None:
					return None
				else:
					return default
			else:
				return v
		else:
			item = url.get_path(i)
			if item not in dict_value:
				dict_value[item] = {}
			dict_value = dict_value[item]
	if default is None:
		return None
	else:
		return default
