#! /usr/bin/python3
# -*- coding: UTF-8 -*-

if __name__ == "__main__":
	raise Exception("不支持从这里调用")

__version__ = "1.0"
__all__ = [
	"mousechsh_file_write_text",
	"mousechsh_file_read_text",
	"mousechsh_file_write_binary",
	"mousechsh_file_read_binary",
]

from com.mousechsh.common.log.MouseChshLog import mousechsh_logging_exception


def mousechsh_file_write_text(path, content):
	if not isinstance(content, str):
		return False
	try:
		with open(path, 'w', encoding='UTF-8') as f:
			f.write(content)
			return True
	except Exception as ex:
		mousechsh_logging_exception(ex, '向文本文件【', path, '】写入内容时遇到错误：')
	return False


def mousechsh_file_read_text(path, *, size=-1):
	try:
		with open(path, 'r', encoding='UTF-8') as f:
			return str(f.read(size))
	except Exception as ex:
		mousechsh_logging_exception(ex, '从文本文件【', path, '】读取内容时遇到错误：')
	return None


def mousechsh_file_write_binary(path, content):
	if not isinstance(content, bytes):
		return False
	try:
		with open(path, 'wb') as f:
			f.write(content)
			return True
	except Exception as ex:
		mousechsh_logging_exception(ex, '向二进制文件【', path, '】写入内容时遇到错误：')
	return False


def mousechsh_file_read_binary(path, *, size=-1):
	try:
		with open(path, 'rb') as f:
			return bytes(f.read(size))
	except Exception as ex:
		mousechsh_logging_exception(ex, '从二进制文件【', path, '】读取内容时遇到错误：')
	return None
