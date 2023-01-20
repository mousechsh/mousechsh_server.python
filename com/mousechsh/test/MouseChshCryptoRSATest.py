#! /usr/bin/python3
# -*- coding: UTF-8 -*-

if __name__ == "__main__":
	raise Exception("不支持从这里调用")

__version__ = "1.0"
__all__ = ["mousechsh_test"]

from com.mousechsh.common.log.MouseChshLog import mousechsh_logging, mousechsh_logging_data

from com.mousechsh.common.util.MouseChshCodeUtil import mousechsh_code_util_type_hexstring, mousechsh_crypto_encrypt, \
	mousechsh_code_util_type_utf8string, mousechsh_code_util_padding_pkcs1, mousechsh_code_util_mode_ecb, \
	mousechsh_code_util_key_type_utf8string, \
	mousechsh_code_util_method_rsa_1024, mousechsh_crypto_key_generate, mousechsh_crypto_decrypt, \
	mousechsh_code_util_key_format_asn1_der_base64, mousechsh_crypto_sign, mousechsh_code_util_hash_sha1, \
	mousechsh_crypto_verify, mousechsh_code_util_hash_sha2_256, mousechsh_code_util_type_base64string


def mousechsh_test(*, use_assert=False):
	mousechsh_logging('开始测试【Crypto】【RSA】相关代码：')

	# ----------------------------------------------------------------
	num = 1
	mousechsh_logging('开始执行测试【', num, '】……')
	keys = mousechsh_crypto_key_generate(method=mousechsh_code_util_method_rsa_1024)
	mousechsh_logging_data(keys, '【RSA算法】自动生成的密钥（1024位）为：')
	result = bool(keys)
	mousechsh_logging(
		'测试【', num,
		'】：'
		'RSA密钥生成，运行结果【', result, '】'
	)
	if use_assert:
		assert result

	# ----------------------------------------------------------------
	keys['public'] = \
		'MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCVRUBu0aSQWRuda39fGViHjrJU' \
		'Hw1/u18fpSsovjzMOZ06t/HXJsk0rfPwckv2C1rs0NTpz5kCAEcvj1i1tSw0bf3h' \
		'VAapc+JaO3Fnqkbt9a3HAMmspe47REx7Kh3kVqE3OGFx161IPAOzHguy0GLIZ9yf' \
		'9nsDLV20m77zgVyf0QIDAQAB'
	keys['private'] = \
		'MIICXQIBAAKBgQCVRUBu0aSQWRuda39fGViHjrJUHw1/u18fpSsovjzMOZ06t/HX' \
		'Jsk0rfPwckv2C1rs0NTpz5kCAEcvj1i1tSw0bf3hVAapc+JaO3Fnqkbt9a3HAMms' \
		'pe47REx7Kh3kVqE3OGFx161IPAOzHguy0GLIZ9yf9nsDLV20m77zgVyf0QIDAQAB' \
		'AoGAKgDaMDTi21GPwTzSEycVL9P6H0y7pjFKA6QdIHJjtk4SDcdcEKBT5vR6G7N1' \
		'547rb48WEpL9qb/9SAdMvZj1Dn+ZvA2+EMRhnVgJNP6W+tD73HGOJ+Cujqm7a4H/' \
		'JjQHceVSahE1ly63y7QFPVadQVm7fxwjoGvPc0tS2v5oH68CQQC30U0JlJWkJQFM' \
		'0rdfRRdmjVJxkBqMuyUkRTLCjCA4ZAynLbys9+u4k6ESjpbr/1OCn+qsuodqSBkS' \
		'qebEaWmLAkEAz+MGViVxccvw31699Jf/hkuoAZ905L3LfGc+chGZpsODxkK3IuXU' \
		'uZc5mnpyFDPtEd55ZLpOI/6ca4v4XO2vkwJBALVLy42NbOHOVa/tjEp8nI3bCNtU' \
		'47q1wfY6Acx75DN6CjjBFXwLsgQEJzNkS1pMI5OMIitmdbTPk1sjE6XYye0CQQCD' \
		'we7lMKwbJNgQqpqYaLHiKxdbl/XdeFF9Em6om3EYGfjt8qDh9GsECc3Pk+Wz2kla' \
		'NvgXmGEoPRpkq30JYPgTAkAiCNR/QQaPrUJ/Hm9o00332BGAV3Q99/KuyLkeY8xY' \
		'QPBVkOSEbR+T1bmBUHsMXFkFTQNPkd57Yzi9xQtVAOOW'

	# ----------------------------------------------------------------
	num += 1
	mousechsh_logging('开始执行测试【', num, '】……')
	source = \
		'MouseChsh加密解密指纹签名测试文本：' \
		'1234567890 ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz' \
		'〇一二三四五六七八九十零壹贰叁肆伍陆柒捌玖拾佰仟万亿'
	key = keys['public']
	output = mousechsh_crypto_encrypt(
		source,
		public_key=key,
		method=mousechsh_code_util_method_rsa_1024,
		mode=mousechsh_code_util_mode_ecb,
		padding=mousechsh_code_util_padding_pkcs1,
		source_type=mousechsh_code_util_type_utf8string,
		target_type=mousechsh_code_util_type_hexstring,
		key_type=mousechsh_code_util_key_type_utf8string,
		key_format=mousechsh_code_util_key_format_asn1_der_base64
	)
	mousechsh_logging_data(
		output,
		'测试【', num,
		'】：'
		'RSA加密（1024位），ECB模式，PKCS1填充，密钥UTF8+ASN1.BASE64，输入UTF8，输出HEX。'
		'原始数据【', source, '】，公钥【', key, '】，运行结果为：'
	)
	mousechsh_logging('继续执行测试【', num, '】……')
	key = keys['private']
	output2 = mousechsh_crypto_decrypt(
		output,
		private_key=key,
		method=mousechsh_code_util_method_rsa_1024,
		mode=mousechsh_code_util_mode_ecb,
		padding=mousechsh_code_util_padding_pkcs1,
		source_type=mousechsh_code_util_type_hexstring,
		target_type=mousechsh_code_util_type_utf8string,
		key_type=mousechsh_code_util_key_type_utf8string,
		key_format=mousechsh_code_util_key_format_asn1_der_base64
	)
	result = (output2 == source)
	mousechsh_logging_data(
		output2,
		'测试【', num,
		'】：'
		'RSA解密（1024位），ECB模式，PKCS1填充，密钥UTF8+ASN1.BASE64，输入HEX，输出UTF8。'
		'输入数据【', output, '】，私钥【', key, '】，运行结果【', result, '】为：'
	)
	if use_assert:
		assert result

	# ----------------------------------------------------------------
	num += 1
	mousechsh_logging('开始执行测试【', num, '】……')
	source = \
		'535FD84B2FDEE7025CD76B064A1F54F2528242F4629C3BEE0883F5E6208D16EA' \
		'ECDF5F0A6F43644B2FCBE684D530D75DC30F82834F683867EAD7A7B95B50ADB3' \
		'302DD3F0FAC3C10CA10DA77A8EA78BED174DDC0510B2AE4E12562911D924A571' \
		'D183D63193886E4B444B837CFA840C61F7DBA35F857E3838C4ED5B83464B6AAD' \
		'1247FE0456687C534B629D2021F165C1257E434A4255BE73DC04D97E92CA73EF' \
		'A5C47BBA78DCC258890781D4099A90E10AF01BAED5DB88A22ED7E557F8350A1C' \
		'79501E9B866750FE86B76173BF2D3C6A943EA74A2E85B8BE21FA406C53FDC341' \
		'90277836BE5A64AB8FEE85133AB14B171D5185811A073537B1495CD96BC27F2E'
	key = keys['private']
	target = \
		'MouseChsh加密解密指纹签名测试文本：' \
		'1234567890 ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz' \
		'〇一二三四五六七八九十零壹贰叁肆伍陆柒捌玖拾佰仟万亿'
	output = mousechsh_crypto_decrypt(
		source,
		private_key=key,
		method=mousechsh_code_util_method_rsa_1024,
		mode=mousechsh_code_util_mode_ecb,
		padding=mousechsh_code_util_padding_pkcs1,
		source_type=mousechsh_code_util_type_hexstring,
		target_type=mousechsh_code_util_type_utf8string,
		key_type=mousechsh_code_util_key_type_utf8string,
		key_format=mousechsh_code_util_key_format_asn1_der_base64
	)
	result = (output == target)
	mousechsh_logging_data(
		output,
		'测试【', num,
		'】：'
		'RSA解密（1024位），ECB模式，PKCS1填充，密钥UTF8+ASN1.BASE64，输入HEX，输出UTF8。'
		'输入数据【', source, '】，私钥【', key, '】，预期结果【', target, '】，运行结果【', result, '】为：'
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
	key = keys['private']
	sign = mousechsh_crypto_sign(
		source,
		private_key=key,
		method=mousechsh_code_util_method_rsa_1024,
		hash_method=mousechsh_code_util_hash_sha1,
		mode=mousechsh_code_util_mode_ecb,
		padding=mousechsh_code_util_padding_pkcs1,
		source_type=mousechsh_code_util_type_utf8string,
		target_type=mousechsh_code_util_type_hexstring,
		key_type=mousechsh_code_util_key_type_utf8string,
		key_format=mousechsh_code_util_key_format_asn1_der_base64
	)
	mousechsh_logging_data(
		sign,
		'测试【', num,
		'】：'
		'RSA签名（1024位），SHA1指纹，ECB模式，PKCS1填充，密钥UTF8+ASN1.BASE64，输入UTF8，输出HEX。'
		'原始数据【', source, '】，私钥【', key, '】，运行结果为：'
	)
	mousechsh_logging('继续执行测试【', num, '】……')
	key = keys['public']
	result = mousechsh_crypto_verify(
		source,
		sign,
		public_key=key,
		method=mousechsh_code_util_method_rsa_1024,
		hash_method=mousechsh_code_util_hash_sha1,
		mode=mousechsh_code_util_mode_ecb,
		padding=mousechsh_code_util_padding_pkcs1,
		source_type=mousechsh_code_util_type_utf8string,
		sign_type=mousechsh_code_util_type_hexstring,
		key_type=mousechsh_code_util_key_type_utf8string,
		key_format=mousechsh_code_util_key_format_asn1_der_base64
	)
	mousechsh_logging(
		'测试【', num,
		'】：'
		'RSA验签（1024位），SHA1指纹，ECB模式，PKCS1填充，密钥UTF8+ASN1.BASE64，输入UTF8，输入签名HEX，输出BOOLEAN。'
		'输入数据【', source, '】，输入签名【', sign, '】，公钥【', key, '】，运行结果【', result, '】'
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
	key = keys['private']
	sign = mousechsh_crypto_sign(
		source,
		private_key=key,
		method=mousechsh_code_util_method_rsa_1024,
		hash_method=mousechsh_code_util_hash_sha2_256,
		mode=mousechsh_code_util_mode_ecb,
		padding=mousechsh_code_util_padding_pkcs1,
		source_type=mousechsh_code_util_type_utf8string,
		target_type=mousechsh_code_util_type_base64string,
		key_type=mousechsh_code_util_key_type_utf8string,
		key_format=mousechsh_code_util_key_format_asn1_der_base64
	)
	mousechsh_logging_data(
		sign,
		'测试【', num,
		'】：'
		'RSA签名（1024位），SHA2-256指纹，ECB模式，PKCS1填充，密钥UTF8+ASN1.BASE64，输入UTF8，输出BASE64。'
		'原始数据【', source, '】，私钥【', key, '】，运行结果为：'
	)
	mousechsh_logging('继续执行测试【', num, '】……')
	key = keys['public']
	result = mousechsh_crypto_verify(
		source,
		sign,
		public_key=key,
		method=mousechsh_code_util_method_rsa_1024,
		hash_method=mousechsh_code_util_hash_sha2_256,
		mode=mousechsh_code_util_mode_ecb,
		padding=mousechsh_code_util_padding_pkcs1,
		source_type=mousechsh_code_util_type_utf8string,
		sign_type=mousechsh_code_util_type_base64string,
		key_type=mousechsh_code_util_key_type_utf8string,
		key_format=mousechsh_code_util_key_format_asn1_der_base64
	)
	mousechsh_logging(
		'测试【', num,
		'】：'
		'RSA验签（1024位），SHA2-256指纹，ECB模式，PKCS1填充，密钥UTF8+ASN1.BASE64，输入UTF8，输入签名BASE64，输出BOOLEAN。'
		'输入数据【', source, '】，输入签名【', sign, '】，公钥【', key, '】，运行结果【', result, '】'
	)
	if use_assert:
		assert result
