#! /usr/bin/python3
# -*- coding: UTF-8 -*-

if __name__ == "__main__":
	raise Exception("不支持从这里调用")

__version__ = "1.0"
__all__ = ["mousechsh_test"]

from com.mousechsh.common.log.MouseChshLog import mousechsh_logging, mousechsh_logging_data

from com.mousechsh.common.util.MouseChshCodeUtil import mousechsh_hash, mousechsh_code_util_type_utf8string, \
	mousechsh_code_util_type_hexstring, mousechsh_code_util_type_base64string, \
	mousechsh_code_util_hash_sha2_256


def mousechsh_test(*, use_assert=False):
	mousechsh_logging('开始测试【Hash】【SHA2-256】相关代码：')

	# ----------------------------------------------------------------
	num = 1
	mousechsh_logging('开始执行测试【', num, '】……')
	source = \
		'MouseChsh加密解密指纹签名测试文本：' \
		'1234567890 ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz' \
		'〇一二三四五六七八九十零壹贰叁肆伍陆柒捌玖拾佰仟万亿'
	target = '53BDA309B1F1ABE61CAC5ACFD2DE556F44ED278AC3151F85897B3CFA9821D898'
	output = mousechsh_hash(
		source,
		method=mousechsh_code_util_hash_sha2_256,
		source_type=mousechsh_code_util_type_utf8string,
		target_type=mousechsh_code_util_type_hexstring
	)
	result = (target == output)
	mousechsh_logging_data(
		output,
		'测试【', num,
		'】：'
		'SHA2-256散列生成，输入UTF8，输出HEX。'
		'原始数据【', source, '】，预期结果【', target, '】，运行结果【', result, '】为：'
	)
	if use_assert:
		assert result

	# ----------------------------------------------------------------
	num += 1
	mousechsh_logging('开始执行测试【', num, '】……')
	source = \
		'MouseChsh加密解密指纹签名测试文本：' \
		'1234567890 ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz' \
		'〇一二三四五六七八九十零壹贰叁肆伍陆柒捌玖拾佰仟万亿'
	target = 'U72jCbHxq+YcrFrP0t5Vb0TtJ4rDFR+FiXs8+pgh2Jg='
	output = mousechsh_hash(
		source,
		method=mousechsh_code_util_hash_sha2_256,
		source_type=mousechsh_code_util_type_utf8string,
		target_type=mousechsh_code_util_type_base64string
	)
	result = (target == output)
	mousechsh_logging_data(
		output,
		'测试【', num,
		'】：'
		'SHA2-256散列生成，输入UTF8，输出BASE64。'
		'原始数据【', source, '】，预期结果【', target, '】，运行结果【', result, '】为：'
	)
	if use_assert:
		assert result
