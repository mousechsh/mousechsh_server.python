#! /usr/bin/python3
# -*- coding: UTF-8 -*-
from com.mousechsh.common.util.MouseChshCodeUtil import mousechsh_codec, mousechsh_code_util_type_utf8string, \
	mousechsh_code_util_type_urlstring

if __name__ == "__main__":
	raise Exception("不支持从这里调用")

__version__ = "1.0"
__all__ = ["MouseChshUrl"]

from com.mousechsh.common.log.MouseChshLog import mousechsh_logging_exception


class MouseChshUrl:

	def __init__(self):
		self.__protocol = ''
		self.__host = ''
		self.__port = 0
		self.__path = []
		self.__root = False
		self.__search = {}
		self.__hash = ''

	def clean(self):
		self.__protocol = ''
		self.__host = ''
		self.__port = 0
		self.__path.clear()
		self.__root = False
		self.__search.clear()
		self.__hash = ''

	def set_protocol(self, value):
		if value is None:
			return
		self.__protocol = str(value)
		if self.__protocol:
			self.__root = True

	def get_protocol(self):
		return self.__protocol

	def set_host(self, value):
		if value is None:
			return
		self.__host = value
		if self.__host:
			self.__root = True

	def get_host(self):
		return self.__host

	def set_port(self, value):
		try:
			p = int(value)
			if p < 0 or p > 65535:
				raise Exception('数值超过端口号允许的范围')
			self.__port = p
			if self.__port:
				self.__root = True
		except Exception as ex:
			mousechsh_logging_exception(ex, "试图将不合法的数值作为端口号使用：")

	def get_port(self):
		return self.__port

	def get_root(self):
		return self.__root

	def set_path(self, value):
		self.__path = []
		if value is None:
			return
		value = str(value).strip()
		if value.find('/') == 0 or (
			self.__protocol or self.__host or self.__port
		):
			self.__root = True
		else:
			self.__root = False
		value = value.strip('/')
		list_value = value.split('/')
		for item in list_value:
			if item:
				self.__path.append(item)

	def get_path(self, index=-1):
		if index >= len(self.__path):
			return None
		if index < 0:
			return ('/' if self.__root else '') + '/'.join(map(str, self.__path))
		return self.__path[index]

	def get_last_path(self):
		path_len = len(self.__path)
		if path_len == 0:
			return None
		return self.__path[path_len - 1]

	def get_path_depth(self):
		return len(self.__path)

	def append_path(self, value):
		if value is None:
			return
		value = str(value).strip()
		value = value.strip('/')
		list_value = value.split('/')
		for item in list_value:
			if item:
				self.__path.append(item)

	def remove_path(self, index):
		if index < 0 or index >= len(self.__path):
			return
		self.__path.pop(index)

	def pop_path(self):
		if len(self.__path) == 0:
			return None
		return self.__path.pop()

	def replace_path(self, path1, path2):
		if path1.find('/') == 0:
			is_root = True
		else:
			is_root = False
		path1s = []
		path2s = []
		path1 = path1.strip('/')
		path1 = path1.split('/')
		for item in path1:
			if item:
				path1s.append(item)
		path2 = path2.strip('/')
		path2 = path2.split('/')
		for item in path2:
			if item:
				path2s.append(item)
		i = 0
		il = len(self.__path)
		jl = len(path1s)
		kl = len(path2s)
		flag = False
		if is_root:
			for j in range(jl):
				if i + j < il and self.__path[i + j] == path1[j]:
					flag = True
				else:
					flag = False
		else:
			for i in range(il):
				for j in range(jl):
					if i + j < il and self.__path[i + j] == path1[j]:
						flag = True
					else:
						flag = False
						continue
				if flag:
					break
				else:
					flag = False
		if flag:
			x = 0
			for k in range(max(jl, kl)):
				if i + k < il + x:
					if k < jl:
						if k < kl:
							self.__path[x + i + k] = path2s[k]
						else:
							self.__path.pop(x + i + kl)
					else:
						if k < kl:
							self.__path.insert(x + i + jl, path2s[k])
							x += 1
						else:
							self.__path.pop(x + i + kl)
				else:
					self.__path.insert(x + i + k, path2s[k])
					x += 1

	def set_search(self, key, value):
		key = str(key)
		if value is None:
			self.__search.pop(key)
			return
		item = self.__search.get(key, None)
		if item is None:
			self.__search[key] = str(value)
		else:
			if isinstance(item, list):
				item.append(str(value))
			else:
				self.__search[key] = [item, str(value)]

	def parse_search(self, value):
		if value is None:
			self.__search.clear()
		value = str(value)
		list_value = value.split('&')
		for item in list_value:
			index = item.find('=')
			if index < 0:
				self.set_search(item, '')
			else:
				self.set_search(item[0: index], item[index + 1:])

	def get_search(self, key=None, *, sort=False, trim=False, encode=False):
		if key is None:
			if len(self.__search) <= 0:
				return ''
			result = ''
			items = self.__search
			if sort:
				items = sorted(items, key=lambda d: d[0])
			for k in items:
				value = self.__search[k]
				if trim and value == '':
					continue
				if value == '':
					result += '&' + str(k)
				elif isinstance(value, list):
					list_data = value
					if sort:
						list_data = sorted(list_data)
					if encode:
						for list_item in list_data:
							result += '&' + str(k) + '=' + mousechsh_codec(
								str(list_item),
								source_type=mousechsh_code_util_type_utf8string,
								target_type=mousechsh_code_util_type_urlstring
							)
					else:
						for list_item in list_data:
							result += '&' + str(k) + '=' + str(list_item)
				else:
					if encode:
						result += '&' + str(k) + '=' + mousechsh_codec(
							str(self.__search[k]),
							source_type=mousechsh_code_util_type_utf8string,
							target_type=mousechsh_code_util_type_urlstring
						)
					else:
						result += '&' + str(k) + '=' + str(self.__search[k])
			return result[1:]
		key = str(key)
		return self.__search.get(key, '')

	def get_search_data(self):
		return self.__search

	def set_hash(self, value):
		if value is None:
			return
		self.__hash = str(value)

	def get_hash(self):
		return self.__hash

	def to_string(self):
		result = ''
		if self.__protocol:
			result += self.__protocol + '://'
		if self.__host:
			result += self.__host
			if self.__port:
				result += ':' + str(self.__port)
		if self.__root:
			result += '/'
		if self.__path:
			result += '/'.join(map(str, self.__path))
		if len(self.__search) > 0:
			result += '?' + self.get_search()
		if self.__hash:
			result += '#' + self.__hash

		return result

	def parse(self, value):
		self.clean()
		if value is None:
			return
		value = str(value).strip()
		ext = ''
		index = value.find('#')
		if index >= 0:
			self.set_hash(value[index + 1:])
			value = value[0: index]
		index = value.find('?')
		if index >= 0:
			search = value[index + 1:]
			self.parse_search(search)
			value = value[0: index]
		index = value.find('://')
		if index >= 0:
			ext = '/'
			self.set_protocol(value[0: index])
			value = value[index + 1:]
		index = value.find('//')
		if index == 0:
			ext = '/'
			value = value[2:]
			index = value.find('/')
			index2 = value.find(':')
			if index < 0:
				if index2 >= 0:
					self.set_host(value[0: index2])
					self.set_port(value[index2 + 1:])
				else:
					self.set_host(value)
				value = ''
			else:
				if index2 >= 0:
					self.set_host(value[0: index2])
					self.set_port(value[index2 + 1: index])
				else:
					self.set_host(value[0: index])
				value = value[index + 1:]
		self.set_path(ext + value)
