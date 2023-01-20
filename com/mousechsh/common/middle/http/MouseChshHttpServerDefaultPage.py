#! /usr/bin/python3
# -*- coding: UTF-8 -*-

if __name__ == "__main__":
	raise Exception("不支持从这里调用")

__version__ = "1.0"
__all__ = []

import os

from com.mousechsh.common.io.file.MouseChshFile import mousechsh_file_read_text
from com.mousechsh.common.middle.http.MouseChshHttpHeader import mousechsh_http_header_accept_language_annotation
from com.mousechsh.common.middle.router.MouseChshHttpRouter import mousechsh_http_router_annotation


@mousechsh_http_router_annotation(method='GET', path='/')
@mousechsh_http_header_accept_language_annotation()
def index(url, request, response, *argsArr, **argsDict):
	response.get_header().set_content_type__('html').set_content_type_options()
	response.set_body(
		'''<!DOCTYPE html>
<html lang="zh-CN">
	<head>
		<meta charset="UTF-8">
		<meta http-equiv="X-UA-Compatible" content="IE=edge">
		<meta name="viewport" content="width=device-width, initial-scale=1.0">
		<title>HTTP服务器</title>
	</head>
	<body>
		HTTP服务器已经启动。
		<h1>地址信息</h1>
		<pre>''' +
		url.to_string().replace('&', '&amp;').replace('<', '&lt;') +
		'''</pre>
		<h1>请求信息</h1>
		<pre>''' +
		request.get_header().to_string() +
		'''</pre>
		<h1>响应信息</h1>
		<pre>''' +
		response.get_header().to_string() +
		'''</pre>
	</body>
</html>'''
	)


@mousechsh_http_router_annotation(method='GET', path='/favicon.ico')
@mousechsh_http_header_accept_language_annotation()
def index(url, request, response, *argsArr, **argsDict):
	response.get_header().set_content_type__('svg').set_content_type_options()
	response.set_body(mousechsh_file_read_text(os.path.join(
		os.path.dirname(__file__),
		'MouseChshFavicon.ico.svg'
	)))
