#! /usr/bin/python3
# -*- coding: UTF-8 -*-

if __name__ == "__main__":
	raise Exception("不支持从这里调用")

__version__ = "1.0"
__all__ = [
	"MOUSECHSH_WEBSOCKET_FRAME_FIN_PART",
	"MOUSECHSH_WEBSOCKET_FRAME_FIN_LAST",
	"MOUSECHSH_WEBSOCKET_FRAME_OPCODE_CONTINUE",
	"MOUSECHSH_WEBSOCKET_FRAME_OPCODE_TEXT",
	"MOUSECHSH_WEBSOCKET_FRAME_OPCODE_BINARY",
	"MOUSECHSH_WEBSOCKET_FRAME_OPCODE_CLOSE",
	"MOUSECHSH_WEBSOCKET_FRAME_OPCODE_PING",
	"MOUSECHSH_WEBSOCKET_FRAME_OPCODE_PONG",
	"MouseChshWebSocketFrame",
]

import struct

from com.mousechsh.common.util.MouseChshCodeUtil import mousechsh_codec, mousechsh_code_util_type_utf8string, \
	mousechsh_code_util_type_bytes
from com.mousechsh.common.util.MouseChshMath import mousechsh_math_bit_in_byte

MOUSECHSH_WEBSOCKET_FRAME_FIN_PART = 0b0
MOUSECHSH_WEBSOCKET_FRAME_FIN_LAST = 0b1
MOUSECHSH_WEBSOCKET_FRAME_OPCODE_CONTINUE = 0x0
MOUSECHSH_WEBSOCKET_FRAME_OPCODE_TEXT = 0x1
MOUSECHSH_WEBSOCKET_FRAME_OPCODE_BINARY = 0x2
MOUSECHSH_WEBSOCKET_FRAME_OPCODE_CLOSE = 0x8
MOUSECHSH_WEBSOCKET_FRAME_OPCODE_PING = 0x9
MOUSECHSH_WEBSOCKET_FRAME_OPCODE_PONG = 0xA
_MOUSECHSH_WEBSOCKET_FRAME_MASK_ENABLE = 0b1
_MOUSECHSH_WEBSOCKET_FRAME_MASK_DISABLE = 0b0


class MouseChshWebSocketFrame:

	def __init__(self):
		self.__fin = MOUSECHSH_WEBSOCKET_FRAME_FIN_LAST
		self.__rsv1 = 0
		self.__rsv2 = 0
		self.__rsv3 = 0
		self.__opcode = 0
		self.__mask = _MOUSECHSH_WEBSOCKET_FRAME_MASK_DISABLE
		self.__payload_len = 0
		self.__masking_key = b''
		self.__payload_data = b''

	def parse(self, data: bytes):
		one_byte = data[0:1]
		data = data[1:]
		one, = struct.unpack('!B', one_byte)
		self.__fin = mousechsh_math_bit_in_byte(one, 0)
		self.__rsv1 = mousechsh_math_bit_in_byte(one, 1)
		self.__rsv2 = mousechsh_math_bit_in_byte(one, 2)
		self.__rsv3 = mousechsh_math_bit_in_byte(one, 3)
		self.__opcode = one & 0b1111
		one_byte = data[0:1]
		data = data[1:]
		one, = struct.unpack('!B', one_byte)
		self.__mask = mousechsh_math_bit_in_byte(one, 0)
		payload_len = one & 0b111_1111
		if payload_len < 126:
			self.__payload_len = payload_len
		elif payload_len == 126:
			two_byte = data[0:2]
			data = data[2:]
			self.__payload_len, = struct.unpack('!H', two_byte)
		else:
			four_byte = data[0:4]
			data = data[4:]
			self.__payload_len, = struct.unpack('!L', four_byte)
		if self.__mask == _MOUSECHSH_WEBSOCKET_FRAME_MASK_ENABLE:
			self.__masking_key = data[0:4]
			data = data[4:]
		if self.__payload_len <= len(data):
			self.__payload_data = data[0:self.__payload_len]
		else:
			self.__payload_data = data + '\0' * (self.__payload_data - len(data))
		if self.__mask == _MOUSECHSH_WEBSOCKET_FRAME_MASK_ENABLE:
			content = bytearray()
			for i in range(self.__payload_len):
				content.append(self.__payload_data[i] ^ self.__masking_key[i % 4])
			self.__payload_data = bytes(content)

	def get_fin(self):
		return self.__fin

	def set_fin(self, value):
		if value == MOUSECHSH_WEBSOCKET_FRAME_FIN_PART:
			self.__fin = MOUSECHSH_WEBSOCKET_FRAME_FIN_PART
		elif value == MOUSECHSH_WEBSOCKET_FRAME_FIN_LAST:
			self.__fin = MOUSECHSH_WEBSOCKET_FRAME_FIN_LAST

	def get_opcode(self):
		return self.__opcode

	def set_opcode(self, value):
		if value == MOUSECHSH_WEBSOCKET_FRAME_OPCODE_CONTINUE:
			self.__opcode = MOUSECHSH_WEBSOCKET_FRAME_OPCODE_CONTINUE
		elif value == MOUSECHSH_WEBSOCKET_FRAME_OPCODE_TEXT:
			self.__opcode = MOUSECHSH_WEBSOCKET_FRAME_OPCODE_TEXT
		elif value == MOUSECHSH_WEBSOCKET_FRAME_OPCODE_BINARY:
			self.__opcode = MOUSECHSH_WEBSOCKET_FRAME_OPCODE_BINARY
		elif value == MOUSECHSH_WEBSOCKET_FRAME_OPCODE_CLOSE:
			self.__opcode = MOUSECHSH_WEBSOCKET_FRAME_OPCODE_CLOSE
		elif value == MOUSECHSH_WEBSOCKET_FRAME_OPCODE_PING:
			self.__opcode = MOUSECHSH_WEBSOCKET_FRAME_OPCODE_PING
		elif value == MOUSECHSH_WEBSOCKET_FRAME_OPCODE_PONG:
			self.__opcode = MOUSECHSH_WEBSOCKET_FRAME_OPCODE_PONG

	def get_mask(self):
		return self.__mask

	def set_mask(self, value):
		if value == _MOUSECHSH_WEBSOCKET_FRAME_MASK_ENABLE:
			self.__mask = _MOUSECHSH_WEBSOCKET_FRAME_MASK_ENABLE
		elif value == _MOUSECHSH_WEBSOCKET_FRAME_MASK_DISABLE:
			self.__mask = _MOUSECHSH_WEBSOCKET_FRAME_MASK_DISABLE

	def get_data(self):
		return self.__payload_data

	def set_data(self, value):
		if isinstance(value, str):
			data = mousechsh_codec(
				value,
				source_type=mousechsh_code_util_type_utf8string,
				target_type=mousechsh_code_util_type_bytes
			)
		elif isinstance(value, bytes):
			data = value
		else:
			data = b''
		self.__payload_len = len(data)
		self.__payload_data = data

	def to_bytes(self):
		result = b''
		one = struct.pack(
			'!B',
			self.__fin * 0b1000_0000 + self.__rsv1 * 0b100_0000 +
			self.__rsv2 * 0b10_0000 + self.__rsv3 * 0b1_0000 +
			self.__opcode
		)
		result += one
		if self.__payload_len < 126:
			one = struct.pack('!B', self.__mask * 0b1000_0000 + self.__payload_len)
			result += one
		elif self.__payload_len <= 0b1111_1111_1111_1111:
			one = struct.pack(
				'!B',
				self.__mask * 0b1000_0000 + 126
			)
			result += one
			result += struct.pack('!H', self.__payload_len)
		else:
			one = struct.pack('!B', self.__mask * 0b1000_0000 + 127)
			result += one
			result += struct.pack('!L', self.__payload_len)
		if self.__mask == _MOUSECHSH_WEBSOCKET_FRAME_MASK_ENABLE:
			result += self.__masking_key[0:4]
			data = bytearray()
			for i in range(self.__payload_len):
				data.append(self.__payload_data[i] ^ self.__masking_key[i % 4])
		else:
			data = self.__payload_data
		result += data[0:self.__payload_len]
		return result
