#! /usr/bin/python3
# -*- coding: UTF-8 -*-

__version__ = "1.0"
__all__ = ["mousechsh"]

import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from com.mousechsh.test.MouseChshTest import *


def mousechsh():
	if mousechsh_test(use_assert=True, test_only=False):
		from com.mousechsh.run.MouseChshRun import mousechsh_run
		mousechsh_run()


if __name__ == "__main__":
	mousechsh()
