#! /usr/bin/python3
# -*- coding: UTF-8 -*-

if __name__ == "__main__":
	raise Exception("不支持从这里调用")

__version__ = "1.0"
__all__ = ["mousechsh_test"]

from com.mousechsh.common.log.MouseChshLog import mousechsh_logging, mousechsh_logging_data

from com.mousechsh.common.util.MouseChshCodeUtil import mousechsh_code_util_type_hexstring, mousechsh_crypto_encrypt, \
	mousechsh_code_util_type_utf8string, mousechsh_code_util_padding_pkcs5, mousechsh_code_util_mode_ecb, \
	mousechsh_code_util_method_3des_192, mousechsh_code_util_type_base64string, mousechsh_code_util_key_type_utf8string, \
	mousechsh_crypto_decrypt


def mousechsh_test(*, use_assert=False):
	mousechsh_logging('开始测试【Crypto】【3DES】相关代码：')

	# ----------------------------------------------------------------
	num = 1
	mousechsh_logging('开始执行测试【', num, '】……')
	source = \
		'MouseChsh加密解密指纹签名测试文本：' \
		'1234567890 ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz' \
		'〇一二三四五六七八九十零壹贰叁肆伍陆柒捌玖拾佰仟万亿'
	key = '1235678890ABCDEFGhijklmn'
	target = \
		'EAA923225F8AC907AB0404D8953BF60E93F564881DFB0555C80C2F5FE9715979' \
		'2FAF87EA61E7F94E29855B1FCD238A46E2ECA4F0F478FA13D0662A09FA6C7E29' \
		'40849E20C8B968C4DDEAA0C0024ABA6897B08D2F55EB2E67366E210A0284F3D7' \
		'F358C15FFA4E669EB1E7BABA1EEE0BDA5292D8D03EB6FE395F7AB338E4C03183' \
		'F1253365BBFFD4B95C42A55CF4F423C44C2B2ED4DCA05459649444144B509B04' \
		'EA1736943EBAC6245500B185D69FB79E0B6FAF824E4ABC5EBC309091B159B7A0'
	output = mousechsh_crypto_encrypt(
		source,
		public_key=key,
		method=mousechsh_code_util_method_3des_192,
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
		'3DES加密，ECB模式，PKCS5填充，密钥UTF8，输入UTF8，输出HEX。'
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
	key = '1235678890ABCDEFGhijklmn'
	target = \
		'6qkjIl+KyQerBATYlTv2DpP1ZIgd+wVVyAwvX+lxWXkvr4fqYef5TimFWx/NI4pG' \
		'4uyk8PR4+hPQZioJ+mx+KUCEniDIuWjE3eqgwAJKumiXsI0vVesuZzZuIQoChPPX' \
		'81jBX/pOZp6x57q6Hu4L2lKS2NA+tv45X3qzOOTAMYPxJTNlu//UuVxCpVz09CPE' \
		'TCsu1NygVFlklEQUS1CbBOoXNpQ+usYkVQCxhdaft54Lb6+CTkq8XrwwkJGxWbeg'
	output = mousechsh_crypto_encrypt(
		source,
		public_key=key,
		method=mousechsh_code_util_method_3des_192,
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
		'3DES加密，ECB模式，PKCS5填充，密钥UTF8，输入UTF8，输出BASE64。'
		'原始数据【', source, '】，密钥【', key, '】，预期结果【', target, '】，运行结果【', result, '】为：'
	)
	if use_assert:
		assert result

	# ----------------------------------------------------------------
	num += 1
	mousechsh_logging('开始执行测试【', num, '】……')
	source = \
		'EAA923225F8AC907AB0404D8953BF60E93F564881DFB0555C80C2F5FE9715979' \
		'2FAF87EA61E7F94E29855B1FCD238A46E2ECA4F0F478FA13D0662A09FA6C7E29' \
		'40849E20C8B968C4DDEAA0C0024ABA6897B08D2F55EB2E67366E210A0284F3D7' \
		'F358C15FFA4E669EB1E7BABA1EEE0BDA5292D8D03EB6FE395F7AB338E4C03183' \
		'F1253365BBFFD4B95C42A55CF4F423C44C2B2ED4DCA05459649444144B509B04' \
		'EA1736943EBAC6245500B185D69FB79E0B6FAF824E4ABC5EBC309091B159B7A0'
	key = '1235678890ABCDEFGhijklmn'
	target = \
		'MouseChsh加密解密指纹签名测试文本：' \
		'1234567890 ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz' \
		'〇一二三四五六七八九十零壹贰叁肆伍陆柒捌玖拾佰仟万亿'
	output = mousechsh_crypto_decrypt(
		source,
		private_key=key,
		method=mousechsh_code_util_method_3des_192,
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
		'3DES解密，ECB模式，PKCS5填充，密钥UTF8，输入HEX，输出UTF8。'
		'原始数据【', source, '】，密钥【', key, '】，预期结果【', target, '】，运行结果【', result, '】为：'
	)
	if use_assert:
		assert result

	# ----------------------------------------------------------------
	num += 1
	mousechsh_logging('开始执行测试【', num, '】……')
	source = \
		'6qkjIl+KyQerBATYlTv2DpP1ZIgd+wVVyAwvX+lxWXkvr4fqYef5TimFWx/NI4pG' \
		'4uyk8PR4+hPQZioJ+mx+KUCEniDIuWjE3eqgwAJKumiXsI0vVesuZzZuIQoChPPX' \
		'81jBX/pOZp6x57q6Hu4L2lKS2NA+tv45X3qzOOTAMYPxJTNlu//UuVxCpVz09CPE' \
		'TCsu1NygVFlklEQUS1CbBOoXNpQ+usYkVQCxhdaft54Lb6+CTkq8XrwwkJGxWbeg'
	key = '1235678890ABCDEFGhijklmn'
	target = \
		'MouseChsh加密解密指纹签名测试文本：' \
		'1234567890 ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz' \
		'〇一二三四五六七八九十零壹贰叁肆伍陆柒捌玖拾佰仟万亿'
	output = mousechsh_crypto_decrypt(
		source,
		private_key=key,
		method=mousechsh_code_util_method_3des_192,
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
		'3DES解密，ECB模式，PKCS5填充，密钥UTF8，输入BASE64，输出UTF8。'
		'原始数据【', source, '】，密钥【', key, '】，预期结果【', target, '】，运行结果【', result, '】为：'
	)
	if use_assert:
		assert result
