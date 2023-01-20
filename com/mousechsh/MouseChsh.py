#! /usr/bin/python3
# -*- coding: UTF-8 -*-

__version__ = "1.0"
__all__ = ["mousechsh"]

import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from com.mousechsh.run.MouseChshRun import mousechsh_run


def mousechsh():
	mousechsh_run()


if __name__ == "__main__":
	mousechsh()
