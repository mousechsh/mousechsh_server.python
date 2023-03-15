# MouseChsh Server Side

* [中文版说明](./README.md "Chinese Readme")
* [English Readme](./README.en.md "英文版说明")

# Overview

MouseChsh Server Side is a comprehensive server developed from scratch.

The goal of development is to provide service capabilities based on RPC, HTTP, WebSocket and other protocols, and to be able to use databases such as PostgreSQL and cache libraries such as Redis.

Although unavoidable, this project will use as few third-party libraries as possible.

Although in this day and age, it may not make much sense to build a wheel from scratch. However, starting from scratch is indeed a programmer's romance. Moreover, you can learn a lot of low-level knowledge from scratch. Every time I think about it, it moves me.

# Information

| Key      | Value                   |
| -------- | ----------------------- |
| Project  | mousechsh_server.python |
| Language | Python 3.9              |

## Third-party code referenced

| Library      | Version     | Description                            |
| ------------ | ----------- | -------------------------------------- |
| redis        | 4.3.4       | Redis driver                           |
| psycopg2     | 2.9.3       | PostgreSQL driver                      |
| pycryptodome | 3.15.0      | Encryption and decryption library      |
| PyJWT        | 2.4.0       | JWT library                            |
| GmSSL        | 3.2.2       | Pure-Python SM2/SM3/SM4 implementation |
| SM2          | Source code | GmSSL                                  |
