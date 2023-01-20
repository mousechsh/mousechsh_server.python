#! /usr/bin/python3
# -*- coding: UTF-8 -*-

if __name__ == "__main__":
	raise Exception("不支持从这里调用")

__version__ = "1.0"
__all__ = ["mousechsh_loader"]

import importlib

from com.mousechsh.common.log.MouseChshLog import mousechsh_logging


def mousechsh_loader(module):
	if module is None:
		return
	if isinstance(module, str):
		mousechsh_logging('动态导入单个模块【', module, '】')
		importlib.import_module(module)
		return
	if isinstance(module, list):
		for item in module:
			mousechsh_logging('动态导入一组模块【', item, '】')
			importlib.import_module(item)
		return
