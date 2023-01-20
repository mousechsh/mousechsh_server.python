#! /usr/bin/python3
# -*- coding: UTF-8 -*-

if __name__ == "__main__":
	raise Exception("不支持从这里调用")

__version__ = "1.0"
__all__ = ["MouseChshCryptoPKCS5"]

from com.mousechsh.common.util.crypto.padding.MouseChshCryptoPKCS7 import MouseChshCryptoPKCS7


class MouseChshCryptoPKCS5(MouseChshCryptoPKCS7):

	def __init__(self):
		super().__init__()
		self.block_size()

	def block_size(self, size=0):
		super().block_size(8)
