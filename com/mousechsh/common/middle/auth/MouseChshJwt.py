#! /usr/bin/python3
# -*- coding: UTF-8 -*-

if __name__ == "__main__":
	raise Exception("不支持从这里调用")

__version__ = "1.0"
__all__ = [
	"mousechsh_jwt_encode_string",
	"mousechsh_jwt_decode_string"
]

from datetime import datetime

import jwt

from com.mousechsh.common.data.MouseChshModel import MouseChshModel
from com.mousechsh.common.log.MouseChshLog import mousechsh_logging_exception


def mousechsh_jwt_encode_string(
	token, salt='12345678', *, alg='HS256', start=datetime.now().timestamp(), exp=3600
):
	headers = {
		# 'typ': 'JWT',
		# 'alg': 'HS256'
	}
	if isinstance(token, MouseChshModel):
		payload = dict(
			token.data(), **{
				"exp": int(start) + int(exp)
			}
		)
	elif isinstance(token, dict):
		payload = dict(
			token, **{
				"exp": int(start) + int(exp)
			}
		)
	else:
		payload = {
			"name": token,
			"exp": int(start) + int(exp)
		}
	jwt_token = jwt.encode(payload=payload, key=salt, algorithm=alg, headers=headers)
	return jwt_token


def mousechsh_jwt_decode_string(token, salt='12345678', *, alg='HS256', check=True):
	if check:
		try:
			obj = jwt.decode(token, salt, algorithms=alg)
			return {
				'verify': True,
				'data': obj
			}
		except Exception as ex:
			mousechsh_logging_exception(ex, '解码JWT TOKEN时遇到错误：')
	try:
		obj = jwt.decode(token, salt, algorithms=alg, options={'verify_signature': False, 'verify_exp': False})
		return {
			'verify': False,
			'data': obj
		}
	except Exception as ex:
		mousechsh_logging_exception(ex, '单解码JWT TOKEN时遇到错误：')
		return {
			'verify': False,
			'data': {}
		}
