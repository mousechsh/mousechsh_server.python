#! /usr/bin/python3
# -*- coding: UTF-8 -*-

if __name__ == "__main__":
	raise Exception("不支持从这里调用")

__version__ = "1.0"
__all__ = []

from com.mousechsh.common.sys.MouseChshLoader import mousechsh_loader

mousechsh_loader('com.mousechsh.common.cmd.MouseChshHttpClientCmd')
mousechsh_loader('com.mousechsh.common.cmd.MouseChshHttpServerCmd')
mousechsh_loader('com.mousechsh.common.cmd.MouseChshTcpClientCmd')
mousechsh_loader('com.mousechsh.common.cmd.MouseChshWebSocketServerCmd')
