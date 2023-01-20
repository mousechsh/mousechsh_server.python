#! /usr/bin/python3
# -*- coding: UTF-8 -*-

if __name__ == "__main__":
	raise Exception("不支持从这里调用")

__version__ = "1.0"
__all__ = ["mousechsh_run"]

import os
import sys

sys.path.insert(
	0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
)

from com.mousechsh.common.sys.MouseChshThread import mousechsh_thread_sleep
from com.mousechsh.common.cmd.MouseChshCmd import mousechsh_cmd_call_from_cli
from com.mousechsh.common.sys.MouseChshLoader import mousechsh_loader
from com.mousechsh.common.log.MouseChshLog import \
	MOUSECHSH_LOG_LEVEL_FATAL, \
	MOUSECHSH_LOG_LEVEL_INFO, \
	mousechsh_logging, \
	mousechsh_logging_data, \
	mousechsh_logging_exception


# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# from com.mousechsh.run.MouseChshLogConfig import *
# from com.mousechsh.run.MouseChshRunConfig import *
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


def mousechsh_run():
	mousechsh_loader('com.mousechsh.run.MouseChshLogConfig')
	mousechsh_logging("开始运行……", level=MOUSECHSH_LOG_LEVEL_FATAL)
	mousechsh_logging_data(sys.path, "环境变量【sys.path】：", level=MOUSECHSH_LOG_LEVEL_INFO)
	mousechsh_logging("传入参数数量：", len(sys.argv), level=MOUSECHSH_LOG_LEVEL_INFO)
	for i in range(0, len(sys.argv)):
		mousechsh_logging(i, ")", sys.argv[i], level=MOUSECHSH_LOG_LEVEL_INFO)

	obj = None
	try:
		mousechsh_loader('com.mousechsh.run.MouseChshRunConfig')
		obj = mousechsh_cmd_call_from_cli(sys.argv)

		flag = True

		if obj is None:
			mousechsh_logging("没有可执行的命令", level=MOUSECHSH_LOG_LEVEL_FATAL)
			flag = False

		while flag:
			mousechsh_thread_sleep()

	except KeyboardInterrupt as ex:
		mousechsh_logging_exception(ex, "被键盘快捷键打断：", level=MOUSECHSH_LOG_LEVEL_FATAL)
	except Exception as ex:
		mousechsh_logging_exception(ex, "遇到无法恢复的错误：", level=MOUSECHSH_LOG_LEVEL_FATAL)
	finally:
		if obj is not None:
			obj.interrupt()

	mousechsh_logging("主线程结束运行。", level=MOUSECHSH_LOG_LEVEL_FATAL)
	sys.exit(0)
