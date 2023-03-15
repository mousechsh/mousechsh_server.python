#! /usr/bin/python3
# -*- coding: UTF-8 -*-

if __name__ == "__main__":
	raise Exception("不支持从这里调用")

__version__ = "1.0"
__all__ = [
	"mousechsh_websocket_client_item_get",
	"mousechsh_websocket_client_item_new",
	"mousechsh_websocket_client_item_join",
	"mousechsh_websocket_client_item_remove",
	"mousechsh_websocket_client_item_send",
	"mousechsh_websocket_client_item_group_send",
	"mousechsh_websocket_client_item_all_send",
	"mousechsh_websocket_client_item_print_all",
	"MouseChshWebSocketClientItem",
]


class MouseChshWebSocketClientItem:

	def __init__(self, client_id):
		self.__id = client_id
		self.__gid = ''
		self.__url = ''
		self.__opened = False
		self.__header_string = ''
		self.__data_list = []

	def get_id(self):
		return self.__id

	def get_group_id(self):
		return self.__gid

	def set_group_id(self, gid):
		self.__gid = gid

	def set_url(self, url):
		self.__url = url

	def get_url(self):
		return self.__url

	def set_opened(self, value):
		self.__opened = bool(value)

	def is_opened(self):
		return self.__opened

	def set_header(self, value):
		self.__header_string = str(value)

	def get_header(self):
		return self.__header_string

	def push_data(self, data):
		self.__data_list.append(data)

	def pop_data(self):
		if len(self.__data_list) == 0:
			return None
		return self.__data_list.pop(0)


_mousechsh_websocket_client_items = {}
_mousechsh_websocket_client_item_groups = {}


def mousechsh_websocket_client_item_get(client_id) -> MouseChshWebSocketClientItem:
	return _mousechsh_websocket_client_items.get(client_id, None)


def mousechsh_websocket_client_item_new(client_id):
	client = MouseChshWebSocketClientItem(client_id)
	_mousechsh_websocket_client_items[client_id] = client
	return client


def mousechsh_websocket_client_item_join(client_id, group_id):
	if group_id is None:
		return
	client = mousechsh_websocket_client_item_get(client_id)
	if client is None:
		return
	client.set_group_id(group_id)
	group = _mousechsh_websocket_client_item_groups.get(group_id, None)
	if group is None:
		group = []
		_mousechsh_websocket_client_item_groups[group_id] = group
	if client_id not in group:
		group.append(client_id)


def mousechsh_websocket_client_item_remove(client_id):
	if client_id in _mousechsh_websocket_client_items:
		del _mousechsh_websocket_client_items[client_id]
		delete_list = []
		for group_item in _mousechsh_websocket_client_item_groups:
			group = _mousechsh_websocket_client_item_groups[group_item]
			if client_id in group:
				group.remove(client_id)
			if len(group) == 0:
				delete_list.append(group_item)
		for group_item in delete_list:
			del _mousechsh_websocket_client_item_groups[group_item]


def mousechsh_websocket_client_item_send(client_id, msg):
	if client_id in _mousechsh_websocket_client_items:
		client = _mousechsh_websocket_client_items[client_id]
		client.push_data(msg)


def mousechsh_websocket_client_item_group_send(group_id, msg):
	if group_id in _mousechsh_websocket_client_item_groups:
		group = _mousechsh_websocket_client_item_groups[group_id]
		for client_id in group:
			mousechsh_websocket_client_item_send(client_id, msg)


def mousechsh_websocket_client_item_all_send(msg):
	for client_id in _mousechsh_websocket_client_items:
		mousechsh_websocket_client_item_send(client_id, msg)


def mousechsh_websocket_client_item_print_all():
	return {
		'items': list(_mousechsh_websocket_client_items.keys()),
		'groups': _mousechsh_websocket_client_item_groups
	}
