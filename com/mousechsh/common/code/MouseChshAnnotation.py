#! /usr/bin/python3
# -*- coding: UTF-8 -*-

if __name__ == "__main__":
	raise Exception("不支持从这里调用")

__version__ = "1.0"
__all__ = ["mousechsh_annotation", "mousechsh_annotation_get"]

'''
【基础装饰器】
要加在其他装饰器的上面，用于实现Java注解的效果。
'''


def mousechsh_annotation(annotation):
	def _mousechsh_annotation_params(*args_arr, **args_dict):
		mouse_chsh_annotation_func = None
		if len(args_arr) > 0 and callable(args_arr[0]):
			mouse_chsh_annotation_func = args_arr[0]
			args_arr = args_arr[1:]

		def _mousechsh_annotation_func(mousechsh_func=None):
			if mousechsh_func is None:
				mousechsh_func = mouse_chsh_annotation_func
			if mousechsh_func is None:
				return

			arr = args_arr

			anno_name = annotation.__name__
			if getattr(mousechsh_func, '__mousechsh_annotations__', None) is None:
				mousechsh_func.__mousechsh_annotations__ = {}
			if mousechsh_func.__mousechsh_annotations__.get(anno_name) is None:
				mousechsh_func.__mousechsh_annotations__[anno_name] = {}
			mousechsh_func.__mousechsh_annotations__[anno_name]['value'] = arr
			for itemKey in args_dict:
				mousechsh_func.__mousechsh_annotations__[anno_name][itemKey] = args_dict[itemKey]

			mousechsh_func.__mousechsh_annotations__ = dict(
				args_dict.get('__mousechsh_annotations__', {}), **mousechsh_func.__mousechsh_annotations__
			)

			arr = (mousechsh_func,) + arr

			return annotation(*arr, **args_dict)

		return _mousechsh_annotation_func

	return _mousechsh_annotation_params


def mousechsh_annotation_get(obj):
	if obj is None:
		return None
	return getattr(obj, '__mousechsh_annotations__', None)
