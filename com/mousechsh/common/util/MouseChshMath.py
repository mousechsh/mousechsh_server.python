#! /usr/bin/python3
# -*- coding: UTF-8 -*-

if __name__ == "__main__":
	raise Exception("不支持从这里调用")

__version__ = "1.0"
__all__ = ["mousechsh_math_bit_in_byte"]


def mousechsh_math_bit_in_byte(source, index):
	source = int(source)
	index = int(index)
	if index == 0:
		return 1 if (source & 0b1000_0000 == 0b1000_0000) else 0
	elif index == 1:
		return 1 if (source & 0b0100_0000 == 0b0100_0000) else 0
	elif index == 2:
		return 1 if (source & 0b0010_0000 == 0b0010_0000) else 0
	elif index == 3:
		return 1 if (source & 0b0001_0000 == 0b0001_0000) else 0
	elif index == 4:
		return 1 if (source & 0b0000_1000 == 0b0000_1000) else 0
	elif index == 5:
		return 1 if (source & 0b0000_0100 == 0b0000_0100) else 0
	elif index == 6:
		return 1 if (source & 0b0000_0010 == 0b0000_0010) else 0
	elif index == 7:
		return 1 if (source & 0b0000_0001 == 0b0000_0001) else 0
