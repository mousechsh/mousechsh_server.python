#! /usr/bin/python3
# -*- coding: UTF-8 -*-

if __name__ == "__main__":
	raise Exception("不支持从这里调用")

__version__ = "1.0"
__all__ = ["mousechsh_test"]

from com.mousechsh.common.log.MouseChshLog import mousechsh_logging, mousechsh_logging_data

from com.mousechsh.common.util.MouseChshCodeUtil import mousechsh_code_util_type_hexstring, mousechsh_crypto_encrypt, \
	mousechsh_code_util_type_utf8string, mousechsh_code_util_padding_pkcs5, mousechsh_code_util_mode_ecb, \
	mousechsh_code_util_method_sm4_128, mousechsh_code_util_type_base64string, mousechsh_code_util_key_type_utf8string, \
	mousechsh_crypto_decrypt


def mousechsh_test(*, use_assert=False):
	mousechsh_logging('开始测试【Crypto】【SM4】相关代码：')

	# ----------------------------------------------------------------
	num = 1
	mousechsh_logging('开始执行测试【', num, '】……')
	source = \
		'MouseChsh加密解密指纹签名测试文本：' \
		'1234567890 ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz' \
		'〇一二三四五六七八九十零壹贰叁肆伍陆柒捌玖拾佰仟万亿'
	key = '1235678890ABCDEF'
	target = \
		'807A6C46C729B2747014D1338509DDB569D84629FC771186135FC47901EB9129' \
		'04E2585FEED1EF9A1016B16015F5CD232E15F97358E98795DFB99B4C6C057DA0' \
		'616DCEE75C01B245FDCBD7332802B4819B4062CF0CBD4152E0C734916E7177E6' \
		'D32E5A5F06987C87F56876BC54318628C2E4B09DD303B56AEA643A686137438B' \
		'526FB97CC8EDA7911FA30434CF94555B295A1DDB9678C51590DD16D6EE376671' \
		'A27BA902F5CD4E5DD88E8657D1E94AE5AC680CD87EE6600FEB41F2CB5FEDB664'
	output = mousechsh_crypto_encrypt(
		source,
		public_key=key,
		method=mousechsh_code_util_method_sm4_128,
		mode=mousechsh_code_util_mode_ecb,
		padding=mousechsh_code_util_padding_pkcs5,
		source_type=mousechsh_code_util_type_utf8string,
		target_type=mousechsh_code_util_type_hexstring,
		key_type=mousechsh_code_util_key_type_utf8string
	)
	result = (target == output)
	mousechsh_logging_data(
		output,
		'测试【', num,
		'】：'
		'SM4加密，ECB模式，PKCS5填充，密钥UTF8，输入UTF8，输出HEX。'
		'原始数据【', source, '】，密钥【', key, '】，预期结果【', target, '】，运行结果【', result, '】为：'
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
	key = '1235678890ABCDEF'
	target = \
		'gHpsRscpsnRwFNEzhQndtWnYRin8dxGGE1/EeQHrkSkE4lhf7tHvmhAWsWAV9c0j' \
		'LhX5c1jph5XfuZtMbAV9oGFtzudcAbJF/cvXMygCtIGbQGLPDL1BUuDHNJFucXfm' \
		'0y5aXwaYfIf1aHa8VDGGKMLksJ3TA7Vq6mQ6aGE3Q4tSb7l8yO2nkR+jBDTPlFVb' \
		'KVod25Z4xRWQ3RbW7jdmcaJ7qQL1zU5d2I6GV9HpSuWsaAzYfuZgD+tB8stf7bZk'
	output = mousechsh_crypto_encrypt(
		source,
		public_key=key,
		method=mousechsh_code_util_method_sm4_128,
		mode=mousechsh_code_util_mode_ecb,
		padding=mousechsh_code_util_padding_pkcs5,
		source_type=mousechsh_code_util_type_utf8string,
		target_type=mousechsh_code_util_type_base64string,
		key_type=mousechsh_code_util_key_type_utf8string
	)
	result = (target == output)
	mousechsh_logging_data(
		output,
		'测试【', num,
		'】：'
		'SM4加密，ECB模式，PKCS5填充，密钥UTF8，输入UTF8，输出BASE64。'
		'原始数据【', source, '】，密钥【', key, '】，预期结果【', target, '】，运行结果【', result, '】为：'
	)
	if use_assert:
		assert result

	# ----------------------------------------------------------------
	num += 1
	mousechsh_logging('开始执行测试【', num, '】……')
	source = \
		'807A6C46C729B2747014D1338509DDB569D84629FC771186135FC47901EB9129' \
		'04E2585FEED1EF9A1016B16015F5CD232E15F97358E98795DFB99B4C6C057DA0' \
		'616DCEE75C01B245FDCBD7332802B4819B4062CF0CBD4152E0C734916E7177E6' \
		'D32E5A5F06987C87F56876BC54318628C2E4B09DD303B56AEA643A686137438B' \
		'526FB97CC8EDA7911FA30434CF94555B295A1DDB9678C51590DD16D6EE376671' \
		'A27BA902F5CD4E5DD88E8657D1E94AE5AC680CD87EE6600FEB41F2CB5FEDB664'
	key = '1235678890ABCDEF'
	target = \
		'MouseChsh加密解密指纹签名测试文本：' \
		'1234567890 ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz' \
		'〇一二三四五六七八九十零壹贰叁肆伍陆柒捌玖拾佰仟万亿'
	output = mousechsh_crypto_decrypt(
		source,
		private_key=key,
		method=mousechsh_code_util_method_sm4_128,
		mode=mousechsh_code_util_mode_ecb,
		padding=mousechsh_code_util_padding_pkcs5,
		source_type=mousechsh_code_util_type_hexstring,
		target_type=mousechsh_code_util_type_utf8string,
		key_type=mousechsh_code_util_key_type_utf8string
	)
	result = (target == output)
	mousechsh_logging_data(
		output,
		'测试【', num,
		'】：'
		'SM4解密，ECB模式，PKCS5填充，密钥UTF8，输入HEX，输出UTF8。'
		'原始数据【', source, '】，密钥【', key, '】，预期结果【', target, '】，运行结果【', result, '】为：'
	)
	if use_assert:
		assert result

	# ----------------------------------------------------------------
	num += 1
	mousechsh_logging('开始执行测试【', num, '】……')
	source = \
		'gHpsRscpsnRwFNEzhQndtWnYRin8dxGGE1/EeQHrkSkE4lhf7tHvmhAWsWAV9c0j' \
		'LhX5c1jph5XfuZtMbAV9oGFtzudcAbJF/cvXMygCtIGbQGLPDL1BUuDHNJFucXfm' \
		'0y5aXwaYfIf1aHa8VDGGKMLksJ3TA7Vq6mQ6aGE3Q4tSb7l8yO2nkR+jBDTPlFVb' \
		'KVod25Z4xRWQ3RbW7jdmcaJ7qQL1zU5d2I6GV9HpSuWsaAzYfuZgD+tB8stf7bZk'
	key = '1235678890ABCDEF'
	target = \
		'MouseChsh加密解密指纹签名测试文本：' \
		'1234567890 ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz' \
		'〇一二三四五六七八九十零壹贰叁肆伍陆柒捌玖拾佰仟万亿'
	output = mousechsh_crypto_decrypt(
		source,
		private_key=key,
		method=mousechsh_code_util_method_sm4_128,
		mode=mousechsh_code_util_mode_ecb,
		padding=mousechsh_code_util_padding_pkcs5,
		source_type=mousechsh_code_util_type_base64string,
		target_type=mousechsh_code_util_type_utf8string,
		key_type=mousechsh_code_util_key_type_utf8string
	)
	result = (target == output)
	mousechsh_logging_data(
		output,
		'测试【', num,
		'】：'
		'SM4解密，ECB模式，PKCS5填充，密钥UTF8，输入BASE64，输出UTF8。'
		'原始数据【', source, '】，密钥【', key, '】，预期结果【', target, '】，运行结果【', result, '】为：'
	)
	if use_assert:
		assert result
