# MouseChsh服务器端

* [中文版说明](./README.md "Chinese Readme")
* [English Readme](./README.en.md "英文版说明")

# 概述

MouseChsh服务器端是一个从零开发的综合服务端。

开发的目标是为了提供基于RPC、HTTP、WebSocket等协议的服务能力，并且对内能够使用PostgreSQL等数据库以及Redis等缓存库。

虽然不能避免，本项目将尽可能少地使用第三方库。

虽然在现在这个时代，从头造轮子可能没有很大的意义。但是，从零开始果然是程序员的浪漫。而且，从零开始可以学习到很多的底层的知识。每次想到这些，都让我心动不已。

# 项目基本信息

| 键名     | 值                      |
| -------- | ----------------------- |
| 项目代码 | mousechsh_server.python |
| 开发语言 | Python 3.9              |

## 引用的第三方代码

| 库名         | 版本   | 说明                     |
| ------------ | ------ | ------------------------ |
| redis        | 4.3.4  | Redis服务连接驱动        |
| psycopg2     | 2.9.3  | PostgreSQL数据库连接驱动 |
| pycryptodome | 3.15.0 | 加密解密库               |
| PyJWT        | 2.4.0  | JWT编码解码库            |
| GmSSL        | 3.2.2  | 国密算法库               |
| SM2          | 源码   | GmSSL                    |
