#! /usr/bin/python3
# -*- coding: UTF-8 -*-

if __name__ == "__main__":
	raise Exception("不支持从这里调用")

__version__ = "1.0"
__all__ = ["mousechsh_test"]

from com.mousechsh.common.log.MouseChshLog import mousechsh_logging, mousechsh_logging_data

from com.mousechsh.common.util.MouseChshCodeUtil import mousechsh_code_util_type_hexstring, mousechsh_crypto_encrypt, \
	mousechsh_code_util_type_utf8string, mousechsh_code_util_padding_pkcs5, mousechsh_code_util_mode_ecb, \
	mousechsh_code_util_type_base64string, mousechsh_code_util_key_type_utf8string, \
	mousechsh_crypto_decrypt, mousechsh_code_util_method_aes_128


def mousechsh_test(*, use_assert=False):
	mousechsh_logging('开始测试【Crypto】【AES】（128位）相关代码：')

	# ----------------------------------------------------------------
	num = 1
	mousechsh_logging('开始执行测试【', num, '】……')
	source = \
		'MouseChsh加密解密指纹签名测试文本：' \
		'1234567890 ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz' \
		'〇一二三四五六七八九十零壹贰叁肆伍陆柒捌玖拾佰仟万亿'
	key = '1235678890ABCDEF'
	target = \
		'AED83FA229B2B0C5B21B9D379A497606225DAFA420A32916470AF732701EFC03' \
		'55CAA68F802B75E7CE2B71D82E36367FEB399FD39E4514089F776C41AA469010' \
		'D773C5574983E78BE40C1EF55F4570AB309AED462E2C1D2D7EDDA55C43C712A8' \
		'CFC5665425A6AE0BD356F877C20BFD74256D755699881E4B558CA80354F3003E' \
		'2CA686D77D69011078E20FFE70C1D1E37EECD75D9BD7AE6D345EB41519281290' \
		'8992ABD11DAB46DA4AC6B5D42AEA714AE6E0D6C75EF5181E8DB197BC81C9246C'
	output = mousechsh_crypto_encrypt(
		source,
		public_key=key,
		method=mousechsh_code_util_method_aes_128,
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
		'AES加密（128位），ECB模式，PKCS5填充，密钥UTF8，输入UTF8，输出HEX。'
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
		'rtg/oimysMWyG503mkl2BiJdr6QgoykWRwr3MnAe/ANVyqaPgCt1584rcdguNjZ/' \
		'6zmf055FFAifd2xBqkaQENdzxVdJg+eL5Awe9V9FcKswmu1GLiwdLX7dpVxDxxKo' \
		'z8VmVCWmrgvTVvh3wgv9dCVtdVaZiB5LVYyoA1TzAD4spobXfWkBEHjiD/5wwdHj' \
		'fuzXXZvXrm00XrQVGSgSkImSq9Edq0baSsa11CrqcUrm4NbHXvUYHo2xl7yBySRs'
	output = mousechsh_crypto_encrypt(
		source,
		public_key=key,
		method=mousechsh_code_util_method_aes_128,
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
		'AES加密（128位），ECB模式，PKCS5填充，密钥UTF8，输入UTF8，输出BASE64。'
		'原始数据【', source, '】，密钥【', key, '】，预期结果【', target, '】，运行结果【', result, '】为：'
	)
	if use_assert:
		assert result

	# ----------------------------------------------------------------
	num += 1
	mousechsh_logging('开始执行测试【', num, '】……')
	source = \
		'AED83FA229B2B0C5B21B9D379A497606225DAFA420A32916470AF732701EFC03' \
		'55CAA68F802B75E7CE2B71D82E36367FEB399FD39E4514089F776C41AA469010' \
		'D773C5574983E78BE40C1EF55F4570AB309AED462E2C1D2D7EDDA55C43C712A8' \
		'CFC5665425A6AE0BD356F877C20BFD74256D755699881E4B558CA80354F3003E' \
		'2CA686D77D69011078E20FFE70C1D1E37EECD75D9BD7AE6D345EB41519281290' \
		'8992ABD11DAB46DA4AC6B5D42AEA714AE6E0D6C75EF5181E8DB197BC81C9246C'
	key = '1235678890ABCDEF'
	target = \
		'MouseChsh加密解密指纹签名测试文本：' \
		'1234567890 ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz' \
		'〇一二三四五六七八九十零壹贰叁肆伍陆柒捌玖拾佰仟万亿'
	output = mousechsh_crypto_decrypt(
		source,
		private_key=key,
		method=mousechsh_code_util_method_aes_128,
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
		'AES解密（128位），ECB模式，PKCS5填充，密钥UTF8，输入HEX，输出UTF8。'
		'原始数据【', source, '】，密钥【', key, '】，预期结果【', target, '】，运行结果【', result, '】为：'
	)
	if use_assert:
		assert result

	# ----------------------------------------------------------------
	num += 1
	mousechsh_logging('开始执行测试【', num, '】……')
	source = \
		'rtg/oimysMWyG503mkl2BiJdr6QgoykWRwr3MnAe/ANVyqaPgCt1584rcdguNjZ/' \
		'6zmf055FFAifd2xBqkaQENdzxVdJg+eL5Awe9V9FcKswmu1GLiwdLX7dpVxDxxKo' \
		'z8VmVCWmrgvTVvh3wgv9dCVtdVaZiB5LVYyoA1TzAD4spobXfWkBEHjiD/5wwdHj' \
		'fuzXXZvXrm00XrQVGSgSkImSq9Edq0baSsa11CrqcUrm4NbHXvUYHo2xl7yBySRs'
	key = '1235678890ABCDEF'
	target = \
		'MouseChsh加密解密指纹签名测试文本：' \
		'1234567890 ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz' \
		'〇一二三四五六七八九十零壹贰叁肆伍陆柒捌玖拾佰仟万亿'
	output = mousechsh_crypto_decrypt(
		source,
		private_key=key,
		method=mousechsh_code_util_method_aes_128,
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
		'AES解密（128位），ECB模式，PKCS5填充，密钥UTF8，输入BASE64，输出UTF8。'
		'原始数据【', source, '】，密钥【', key, '】，预期结果【', target, '】，运行结果【', result, '】为：'
	)
	if use_assert:
		assert result
