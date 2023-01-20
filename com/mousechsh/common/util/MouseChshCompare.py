#! /usr/bin/python3
# -*- coding: UTF-8 -*-

from inspect import isfunction

if __name__ == "__main__":
	raise Exception("不支持从这里调用")

__version__ = "1.0"
__all__ = [
	"mousechsh_compare_dict_fill",
	"mousechsh_compare_array",
]


def mousechsh_compare_dict_fill(dict_target, dict_source, field, *, ignore=None):
	if not isinstance(dict_target, dict):
		return dict_target
	if not isinstance(dict_source, dict):
		return dict_target
	if not field:
		return dict_target
	data = dict_source.get(field, ignore)
	if data != ignore:
		dict_target[field] = data
	return dict_target


def mousechsh_compare_array(array_left, array_right, *, key=None, content=None, default=None):
	if not isinstance(array_left, list):
		return None
	if not isinstance(array_right, list):
		return None
	if key is None:
		def cmp_key_fn(obj, *, default):
			return obj
	elif isfunction(key):
		cmp_key_fn = key
	else:
		key = str(key)

		def cmp_key_fn(obj, *, default):
			return obj.get(key, default)
	if content is None:
		def cmp_content_fn(left, right, *, default):
			return left == right
	elif isfunction(content):
		cmp_content_fn = content
	elif isinstance(content, list):
		def cmp_content_fn(left, right, *, default):
			for i in content:
				if left.get(i, default) != right.get(i, default):
					return False
			return True
	else:
		content = str(content)

		def cmp_content_fn(left, right, *, default):
			return left.get(content, default) == right.get(content, default)
	result = {
		'remove': [],
		'add': [],
		'modify': []
	}
	left = []
	for i in range(len(array_left)):
		left.append(True)
	right = []
	for i in range(len(array_right)):
		right.append(True)
	for left_index in range(len(array_left)):
		for right_index in range(len(array_right)):
			if left[left_index] and right[right_index]:
				item_key_left = cmp_key_fn(array_left[left_index], default=default)
				item_key_right = cmp_key_fn(array_right[right_index], default=default)
				if item_key_left == item_key_right:
					left[left_index] = False
					right[right_index] = False
					if not cmp_content_fn(array_left[left_index], array_right[right_index], default=default):
						result['modify'].append(item_key_left)
	for i in range(len(array_left)):
		if left[i]:
			result['remove'].append(cmp_key_fn(array_left[i], default=default))
	for i in range(len(array_right)):
		if right[i]:
			result['add'].append(cmp_key_fn(array_right[i], default=default))
	return result
