#! /usr/bin/python3
# -*- coding: UTF-8 -*-

if __name__ == "__main__":
	raise Exception("不支持从这里调用")

__version__ = "1.0"
__all__ = []

# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# import sys
#
# from com.mousechsh.common.log.MouseChshLog import \
# 	mousechsh_log_writer, \
# 	mousechsh_log_level, \
# 	MOUSECHSH_LOG_LEVEL_FATAL, \
# 	MOUSECHSH_LOG_LEVEL_ERROR, \
# 	MOUSECHSH_LOG_LEVEL_WARN, \
# 	MOUSECHSH_LOG_LEVEL_INFO, \
# 	MOUSECHSH_LOG_LEVEL_DEBUG
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

from com.mousechsh.common.log.MouseChshLog import mousechsh_log_writer

# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# LOG LEVEL CHOOSE, DEFAULT IS DEBUG
# mousechsh_log_level( MOUSECHSH_LOG_LEVEL_FATAL )
# mousechsh_log_level( MOUSECHSH_LOG_LEVEL_ERROR )
# mousechsh_log_level( MOUSECHSH_LOG_LEVEL_WARN )
# mousechsh_log_level( MOUSECHSH_LOG_LEVEL_INFO )
# mousechsh_log_level( MOUSECHSH_LOG_LEVEL_DEBUG )
# LOG WRITER CHOOSE, DEFAULT IS NONE
mousechsh_log_writer(console=True, file=False)
# mousechsh_log_writer( console = False, file = True )
# mousechsh_log_writer( console = True, file = True )
# mousechsh_log_writer( console = True, file = True, filename = (sys.argv[1] if len( sys.argv ) > 1 else '') )
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
