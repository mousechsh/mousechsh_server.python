#! /usr/bin/python3
# -*- coding: UTF-8 -*-

if __name__ == "__main__":
	raise Exception("不支持从这里调用")

__version__ = "1.0"
__all__ = ["MouseChshCryptoPadding"]


class MouseChshCryptoPadding:

	@staticmethod
	def default_data():
		return b''

	def content(self, content=None):
		pass

	def content__(self, content=None):
		self.content(content)
		return self

	def data(self, data=None):
		pass

	def data__(self, data=None):
		self.data(data)
		return self

	def pad(self):
		pass

	def dis_pad(self):
		pass
