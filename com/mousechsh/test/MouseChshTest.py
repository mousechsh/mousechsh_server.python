#! /usr/bin/python3
# -*- coding: UTF-8 -*-

if __name__ == "__main__":
	raise Exception("不支持从这里调用")

__version__ = "1.0"
__all__ = ["mousechsh_test"]

from com.mousechsh.common.log.MouseChshLog import mousechsh_logging_exception, mousechsh_log_writer, mousechsh_logging


def mousechsh_test(*, use_assert=False, test_only=True):
	if test_only:
		mousechsh_log_writer(console=True, file=False)
	mousechsh_logging('测试开始——')
	try:
		from com.mousechsh.test.MouseChshHashSM3Test import mousechsh_test as test
		test(use_assert=use_assert)
		from com.mousechsh.test.MouseChshHashMD5Test import mousechsh_test as test
		test(use_assert=use_assert)
		from com.mousechsh.test.MouseChshHashSHA1Test import mousechsh_test as test
		test(use_assert=use_assert)
		from com.mousechsh.test.MouseChshHashSHA2p256Test import mousechsh_test as test
		test(use_assert=use_assert)
		from com.mousechsh.test.MouseChshCryptoSM4Test import mousechsh_test as test
		test(use_assert=use_assert)
		from com.mousechsh.test.MouseChshCrypto3DESTest import mousechsh_test as test
		test(use_assert=use_assert)
		from com.mousechsh.test.MouseChshCryptoAES128Test import mousechsh_test as test
		test(use_assert=use_assert)
		from com.mousechsh.test.MouseChshCryptoRSATest import mousechsh_test as test
		test(use_assert=use_assert)

		return True
	except Exception as ex:
		mousechsh_logging_exception(ex, '测试没有通过：')
		return False
	finally:
		mousechsh_logging('测试结束！')
