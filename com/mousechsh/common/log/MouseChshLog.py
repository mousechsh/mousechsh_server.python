#! /usr/bin/python3
# -*- coding: UTF-8 -*-

if __name__ == "__main__":
	raise Exception("不支持从这里调用")

__version__ = "1.0"
__all__ = [
	"mousechsh_logging",
	"mousechsh_logging_exception",
	"mousechsh_logging_data",
	"mousechsh_log_writer",
	"mousechsh_log_level",
	"MOUSECHSH_LOG_LEVEL_DEBUG",
	"MOUSECHSH_LOG_LEVEL_INFO",
	"MOUSECHSH_LOG_LEVEL_WARN",
	"MOUSECHSH_LOG_LEVEL_ERROR",
	"MOUSECHSH_LOG_LEVEL_FATAL",
]

import os
import threading
import time
import traceback

MOUSECHSH_LOG_LEVEL_DEBUG = 0
MOUSECHSH_LOG_LEVEL_INFO = 1
MOUSECHSH_LOG_LEVEL_WARN = 2
MOUSECHSH_LOG_LEVEL_ERROR = 3
MOUSECHSH_LOG_LEVEL_FATAL = 4

_mousechsh_log_start = time.time()
_mousechsh_log_flag = False
_mousechsh_log_content = []

_mousechsh_log_pid = str(os.getpid())


def _mousechsh_log_thread_index():
	def mousechsh_log_thread_index_gen():
		idx = 0
		while True:
			idx += 1
			yield idx

	mousechsh_log_thread_index_next = mousechsh_log_thread_index_gen()

	def mousechsh_log_thread_index_get():
		return next(mousechsh_log_thread_index_next)

	return mousechsh_log_thread_index_get


_mousechsh_log_thread_index = _mousechsh_log_thread_index()


def _mousechsh_log_index():
	def mousechsh_log_index_gen():
		idx = 0
		while True:
			idx += 1
			yield idx

	mousechsh_log_index_next = mousechsh_log_index_gen()

	def mousechsh_log_index_get():
		return next(mousechsh_log_index_next)

	return mousechsh_log_index_get


_mousechsh_log_index = _mousechsh_log_index()


class MouseChshLog:

	def write(self, index, info, time_str, time_long, level, td_name, content):
		print('')
		print(index, info)
		print(time_str, time_long, level, td_name, content)

	def write_ex(self, index, info, time_str, time_long, level, td_name, content, ex, trace):
		self.write(index, info, time_str, time_long, level, td_name, content)
		print(ex)
		print(trace)

	def write_data(self, index, info, time_str, time_long, level, td_name, content, data):
		self.write(index, info, time_str, time_long, level, td_name, content)
		print(data)


def _mousechsh_log_list_add_ex(ex, trace):
	dict_obj = _mousechsh_logging('【日志记录模块在开启记录线程时出现异常】：')
	dict_obj['type'] = 'exception'
	dict_obj['level'] = 'FATAL'
	dict_obj['ex'] = str(ex)
	dict_obj['trace'] = trace
	for log in _mousechsh_log_list:
		_mousechsh_log_list[log].write_ex(
			dict_obj['index'], dict_obj['info'],
			dict_obj['time_str'], dict_obj['time_long'], dict_obj['level'], dict_obj['td_name'],
			dict_obj['content'], dict_obj['ex'], dict_obj['trace']
		)


def _file_write(f, index, info, time_str, time_long, level, td_name, content):
	f.write('\r')
	f.write(index)
	f.write(' ')
	f.write(info)
	f.write('\r')
	f.write(time_str)
	f.write(' ')
	f.write(time_long)
	f.write(' ')
	f.write(level)
	f.write(' ')
	f.write(td_name)
	f.write(' ')
	f.write(content)
	f.write('\n')


class MouseChshFileLog(MouseChshLog):

	def __init__(self, filename):
		self.__filename = filename
		self.__path = filename + '.log'
		self.repath()

	def repath(self):
		if self.__filename:
			self.__path = \
				self.__filename + \
				'-' + time.strftime("%Y_%m_%d-%H_%M_%S", time.localtime()) + \
				'-' + _mousechsh_log_pid + '.log'
		else:
			self.__path = \
				time.strftime("%Y_%m_%d-%H_%M_%S", time.localtime()) + \
				'-' + _mousechsh_log_pid + '.log'

	def auto_split(self):
		try:
			file_size = os.path.getsize(self.__path)
			if file_size > 10 * 1024 * 1024:
				self.repath()
		except Exception as ex:
			_mousechsh_log_list_add_ex(ex, traceback.format_exc())

	def write(self, index, info, time_str, time_long, level, td_name, content):
		with open(self.__path, 'a', encoding="utf-8") as f:
			_file_write(f, index, info, time_str, time_long, level, td_name, content)
		self.auto_split()

	def write_ex(self, index, info, time_str, time_long, level, td_name, content, ex, trace):
		with open(self.__path, 'a', encoding="utf-8") as f:
			_file_write(f, index, info, time_str, time_long, level, td_name, content)
			f.write(ex)
			f.write('\n')
			f.write(trace)
			f.write('\n')
		self.auto_split()

	def write_data(self, index, info, time_str, time_long, level, td_name, content, data):
		with open(self.__path, 'a', encoding="utf-8") as f:
			_file_write(f, index, info, time_str, time_long, level, td_name, content)
			f.write(data)
			f.write('\n')
		self.auto_split()


_mousechsh_log_list = {}
_mousechsh_log_current_level = MOUSECHSH_LOG_LEVEL_DEBUG


def mousechsh_log_writer(*, console=False, file=False, filename=''):
	if console:
		_mousechsh_log_list['console'] = MouseChshLog()
	else:
		if _mousechsh_log_list.get('console', None) is not None:
			del _mousechsh_log_list['console']
	if file:
		_mousechsh_log_list['file'] = MouseChshFileLog(filename)
	else:
		if _mousechsh_log_list.get('file', None) is not None:
			del _mousechsh_log_list['file']


def mousechsh_log_level(level):
	global _mousechsh_log_current_level
	old_level = _mousechsh_log_current_level
	if level == MOUSECHSH_LOG_LEVEL_DEBUG:
		_mousechsh_log_current_level = MOUSECHSH_LOG_LEVEL_DEBUG
	if level == MOUSECHSH_LOG_LEVEL_INFO:
		_mousechsh_log_current_level = MOUSECHSH_LOG_LEVEL_INFO
	if level == MOUSECHSH_LOG_LEVEL_WARN:
		_mousechsh_log_current_level = MOUSECHSH_LOG_LEVEL_WARN
	if level == MOUSECHSH_LOG_LEVEL_ERROR:
		_mousechsh_log_current_level = MOUSECHSH_LOG_LEVEL_ERROR
	if level == MOUSECHSH_LOG_LEVEL_FATAL:
		_mousechsh_log_current_level = MOUSECHSH_LOG_LEVEL_FATAL
	mousechsh_logging(
		'更改了日志记录等级，从【', old_level, '】到【', _mousechsh_log_current_level, '】', level=MOUSECHSH_LOG_LEVEL_FATAL
	)


def _mousechsh_log_level_get_code(level):
	if level == 'INFO ':
		return MOUSECHSH_LOG_LEVEL_INFO
	elif level == 'WARN ':
		return MOUSECHSH_LOG_LEVEL_WARN
	elif level == 'ERROR':
		return MOUSECHSH_LOG_LEVEL_ERROR
	elif level == 'FATAL':
		return MOUSECHSH_LOG_LEVEL_FATAL
	else:
		return MOUSECHSH_LOG_LEVEL_DEBUG


def _mousechsh_logging(*items, level=MOUSECHSH_LOG_LEVEL_DEBUG):
	t = time.time() - _mousechsh_log_start
	if level == MOUSECHSH_LOG_LEVEL_INFO:
		level = 'INFO '
	elif level == MOUSECHSH_LOG_LEVEL_WARN:
		level = 'WARN '
	elif level == MOUSECHSH_LOG_LEVEL_ERROR:
		level = 'ERROR'
	elif level == MOUSECHSH_LOG_LEVEL_FATAL:
		level = 'FATAL'
	else:
		level = 'DEBUG'
	return {
		'index': '%020d' % _mousechsh_log_index(),
		# PID={ProcessId};TS={ThreadsCount};
		'info': 'PID=' + _mousechsh_log_pid + ';' + 'TS=' + str(len(threading.enumerate())) + ';',
		'time_str': time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),
		'time_long': '%020.6f' % t,
		'level': level,
		'td_name': threading.currentThread().getName(),
		'content': ''.join(map(str, items))
	}


def mousechsh_logging(*items, level=MOUSECHSH_LOG_LEVEL_DEBUG):
	dict_obj = _mousechsh_logging(*items, level=level)
	dict_obj['type'] = 'normal'
	level = _mousechsh_log_level_get_code(dict_obj['level'])
	if level < _mousechsh_log_current_level:
		return
	_mousechsh_log_content.append(dict_obj)
	_mousechsh_log_run()


def mousechsh_logging_exception(ex, *items, level=MOUSECHSH_LOG_LEVEL_DEBUG):
	dict_obj = _mousechsh_logging(*items, level=level)
	dict_obj['type'] = 'exception'
	dict_obj['ex'] = str(ex)
	dict_obj['trace'] = traceback.format_exc()
	level = _mousechsh_log_level_get_code(dict_obj['level'])
	if level < _mousechsh_log_current_level:
		return
	_mousechsh_log_content.append(dict_obj)
	_mousechsh_log_run()


def mousechsh_logging_data(data, *items, level=MOUSECHSH_LOG_LEVEL_DEBUG):
	dict_obj = _mousechsh_logging(*items, level=level)
	dict_obj['type'] = 'data'
	dict_obj['data'] = str(data)
	level = _mousechsh_log_level_get_code(dict_obj['level'])
	if level < _mousechsh_log_current_level:
		return
	_mousechsh_log_content.append(dict_obj)
	_mousechsh_log_run()


def _mousechsh_log_run():
	global _mousechsh_log_flag
	if _mousechsh_log_flag:
		return
	_mousechsh_log_flag = True
	try:
		thd = _MouseChshLog()
		thd.setName('MouseChshLogThread-' + str(_mousechsh_log_thread_index()))
		thd.start()
	except Exception as ex:
		_mousechsh_log_list_add_ex(ex, traceback.format_exc())
		_mousechsh_log_flag = False


class _MouseChshLog(threading.Thread):

	def run(self):
		global _mousechsh_log_flag
		try:
			while len(_mousechsh_log_content) > 0:
				dict_obj = _mousechsh_log_content.pop(0)
				# [PID={ProcessId};TS={ThreadsCount};]LB={LogBuffer};
				dict_obj['info'] = \
					dict_obj['info'] \
					+ 'LB=' + str(len(_mousechsh_log_content)) + ';'
				if dict_obj['type'] == 'normal':
					for log in _mousechsh_log_list:
						_mousechsh_log_list[log].write(
							dict_obj['index'], dict_obj['info'],
							dict_obj['time_str'], dict_obj['time_long'], dict_obj['level'], dict_obj['td_name'],
							dict_obj['content']
						)
				elif dict_obj['type'] == 'exception':
					for log in _mousechsh_log_list:
						_mousechsh_log_list[log].write_ex(
							dict_obj['index'], dict_obj['info'],
							dict_obj['time_str'], dict_obj['time_long'], dict_obj['level'], dict_obj['td_name'],
							dict_obj['content'], dict_obj['ex'], dict_obj['trace']
						)
				elif dict_obj['type'] == 'data':
					for log in _mousechsh_log_list:
						_mousechsh_log_list[log].write_data(
							dict_obj['index'], dict_obj['info'],
							dict_obj['time_str'], dict_obj['time_long'], dict_obj['level'], dict_obj['td_name'],
							dict_obj['content'], dict_obj['data']
						)
				if len(_mousechsh_log_content) < 10:
					time.sleep(0.01)
		except Exception as ex:
			_mousechsh_log_list_add_ex(ex, traceback.format_exc())
		_mousechsh_log_flag = False
