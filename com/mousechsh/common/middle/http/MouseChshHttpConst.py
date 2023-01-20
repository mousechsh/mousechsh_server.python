#! /usr/bin/python3
# -*- coding: UTF-8 -*-

if __name__ == "__main__":
	raise Exception("不支持从这里调用")

__version__ = "1.0"
__all__ = [
	"MOUSECHSH_HTTP_STATUS",
	"MOUSECHSH_HTTP_METHOD_GET",
	"MOUSECHSH_HTTP_METHOD_POST",
	"MOUSECHSH_HTTP_METHOD_PUT",
	"MOUSECHSH_HTTP_METHOD_DELETE",
	"MOUSECHSH_HTTP_METHOD_OPTIONS",
	"mousechsh_http_method_check",
	"MOUSECHSH_HTTP_VERSION_1_0",
	"MOUSECHSH_HTTP_VERSION_1_1",
	"MOUSECHSH_HTTP_VERSION_2_0",
	"mousechsh_http_version_check",
]

MOUSECHSH_HTTP_STATUS = {
	100: 'Continue',
	101: 'Switching Protocols',
	102: 'Processing',
	103: 'Early Hints',
	200: 'OK',
	201: 'Created',
	202: 'Accepted',
	203: 'Non-Authoritative Information',
	204: 'No Content',
	400: 'Bad Request',
	401: 'Unauthorized',
	402: 'Payment Required Experimental',
	403: 'Forbidden',
	404: 'Not Found',
	405: 'Method Not Allowed',
	500: 'Internal Server Error',
}

MOUSECHSH_HTTP_METHOD_GET = 'GET'
MOUSECHSH_HTTP_METHOD_POST = 'POST'
MOUSECHSH_HTTP_METHOD_PUT = 'PUT'
MOUSECHSH_HTTP_METHOD_DELETE = 'DELETE'
MOUSECHSH_HTTP_METHOD_OPTIONS = 'OPTIONS'


def mousechsh_http_method_check(data, *, default_post=False):
	if data == MOUSECHSH_HTTP_METHOD_GET:
		return MOUSECHSH_HTTP_METHOD_GET
	if data == MOUSECHSH_HTTP_METHOD_POST:
		return MOUSECHSH_HTTP_METHOD_POST
	if data == MOUSECHSH_HTTP_METHOD_PUT:
		return MOUSECHSH_HTTP_METHOD_PUT
	if data == MOUSECHSH_HTTP_METHOD_DELETE:
		return MOUSECHSH_HTTP_METHOD_DELETE
	if data == MOUSECHSH_HTTP_METHOD_OPTIONS:
		return MOUSECHSH_HTTP_METHOD_OPTIONS
	if default_post:
		return MOUSECHSH_HTTP_METHOD_POST
	return MOUSECHSH_HTTP_METHOD_GET


MOUSECHSH_HTTP_VERSION_1_0 = 'HTTP/1.0'
MOUSECHSH_HTTP_VERSION_1_1 = 'HTTP/1.1'
MOUSECHSH_HTTP_VERSION_2_0 = 'HTTP/2.0'


def mousechsh_http_version_check(data):
	if data == MOUSECHSH_HTTP_VERSION_1_0:
		return MOUSECHSH_HTTP_VERSION_1_0
	if data == MOUSECHSH_HTTP_VERSION_1_1:
		return MOUSECHSH_HTTP_VERSION_1_1
	if data == MOUSECHSH_HTTP_VERSION_2_0:
		return MOUSECHSH_HTTP_VERSION_2_0
	return MOUSECHSH_HTTP_VERSION_1_1
