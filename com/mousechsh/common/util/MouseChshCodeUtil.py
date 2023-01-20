#! /usr/bin/python3
# -*- coding: UTF-8 -*-

if __name__ == "__main__":
	raise Exception("不支持从这里调用")

__version__ = "1.0"
__all__ = [
	"mousechsh_code_util_type_utf8string",
	"mousechsh_code_util_type_bytes",
	"mousechsh_code_util_type_hexstring",
	"mousechsh_code_util_type_base64string",
	"mousechsh_code_util_type_urlstring",
	"mousechsh_code_util_hash_md5",
	"mousechsh_code_util_hash_sha1",
	"mousechsh_code_util_hash_sha2_256",
	"mousechsh_code_util_hash_sm3",
	"mousechsh_code_util_method_3des_192",
	"mousechsh_code_util_method_aes_128",
	"mousechsh_code_util_method_rsa_1024",
	"mousechsh_code_util_method_rsa_2048",
	"mousechsh_code_util_method_sm4_128",
	"mousechsh_code_util_mode_ecb",
	"mousechsh_code_util_padding_pkcs1",
	"mousechsh_code_util_padding_pkcs5",
	"mousechsh_code_util_padding_pkcs7",
	"mousechsh_code_util_key_type_bytes",
	"mousechsh_code_util_key_type_utf8string",
	"mousechsh_code_util_key_type_hexstring",
	"mousechsh_code_util_key_format_hex_list",
	"mousechsh_code_util_key_format_asn1_der_base64",
	"mousechsh_code_util_key_format_asn1_cert",
	"mousechsh_codec",
	"mousechsh_hash",
	"mousechsh_crypto_key_convert",
	"mousechsh_crypto_key_generate",
	"mousechsh_crypto_encrypt",
	"mousechsh_crypto_decrypt",
	"mousechsh_crypto_sign",
	"mousechsh_crypto_verify",
]

from com.mousechsh.common.code.MouseChshAnnotation import mousechsh_annotation
from com.mousechsh.common.util.codec.MouseChshBase64 import MouseChshBase64Bytes
from com.mousechsh.common.util.codec.MouseChshHexString import MouseChshHexStringBytes
from com.mousechsh.common.util.codec.MouseChshURLString import MouseChshURLStringBytes
from com.mousechsh.common.util.codec.MouseChshUTF8String import MouseChshUTF8StringBytes
from com.mousechsh.common.util.crypto.aes.MouseChshAES import MouseChshAESpECBpPKCS5
from com.mousechsh.common.util.crypto.rsa.MouseChshRSA import MouseChshRSApECBpPKCS1, MouseChshRSApECBpPKCS1withSHA1, \
	MouseChshRSApECBpPKCS1withSHA2p256
from com.mousechsh.common.util.crypto.sm4.MouseChshSM4 import MouseChshSM4pECBpPKCS5
from com.mousechsh.common.util.crypto.tdes.MouseChsh3DES import MouseChsh3DESpECBpPKCS5
from com.mousechsh.common.util.hash.MouseChshMD5 import MouseChshMD5Bytes
from com.mousechsh.common.util.hash.MouseChshSHA import MouseChshSHA1Bytes, MouseChshSHA2p256Bytes
from com.mousechsh.common.util.hash.MouseChshSM3 import MouseChshSM3Bytes


@mousechsh_annotation
def _mousechsh_crypto_lower_params_annotation(func, *low_params):
	def _mousechsh_crypto_lower_params_annotation_params(*args_arr, **args_dict):
		for item in args_dict:
			if item in low_params:
				if args_dict[item] is not None:
					args_dict[item] = str(args_dict[item]).lower()
		return func(*args_arr, **args_dict)

	return _mousechsh_crypto_lower_params_annotation_params


def _mousechsh_crypto_plaintext_source_check(content: any, *, source_type: str) -> bytes:
	data = None
	if source_type == mousechsh_code_util_type_bytes:
		if isinstance(content, bytes):
			data = content
	elif source_type == mousechsh_code_util_type_utf8string:
		data = MouseChshUTF8StringBytes().left__(content).right()
	return data


def _mousechsh_crypto_ciphertext_source_check(content: any, *, source_type: str) -> bytes:
	data = None
	if source_type == mousechsh_code_util_type_bytes:
		if isinstance(content, bytes):
			data = content
	elif source_type == mousechsh_code_util_type_hexstring:
		data = MouseChshHexStringBytes().left__(content).right()
	elif source_type == mousechsh_code_util_type_base64string:
		data = MouseChshBase64Bytes().left__(content).right()
	return data


def _mousechsh_crypto_plaintext_target_check(data: bytes, *, target_type: str) -> any:
	if target_type == mousechsh_code_util_type_bytes:
		return data
	elif target_type == mousechsh_code_util_type_utf8string:
		return MouseChshUTF8StringBytes().right__(data).left()
	else:
		return None


def _mousechsh_crypto_ciphertext_target_check(data: bytes, *, target_type: str) -> any:
	if target_type == mousechsh_code_util_type_bytes:
		return data
	elif target_type == mousechsh_code_util_type_hexstring:
		return MouseChshHexStringBytes().right__(data).left()
	elif target_type == mousechsh_code_util_type_base64string:
		return MouseChshBase64Bytes().right__(data).left()
	else:
		return None


mousechsh_code_util_type_utf8string = 'mousechsh:type-utf8string'
mousechsh_code_util_type_bytes = 'mousechsh:type-bytes'
mousechsh_code_util_type_hexstring = 'mousechsh:type-hexstring'
mousechsh_code_util_type_base64string = 'mousechsh:type-base64string'
mousechsh_code_util_type_urlstring = 'mousechsh:type-urlstring'


@_mousechsh_crypto_lower_params_annotation('source_type', 'target_type')
def mousechsh_codec(
	content,
	*,
	source_type=mousechsh_code_util_type_bytes,
	target_type=mousechsh_code_util_type_bytes
):
	source_type = str(source_type).lower()
	target_type = str(target_type).lower()

	if source_type == mousechsh_code_util_type_utf8string and target_type == mousechsh_code_util_type_bytes:
		return MouseChshUTF8StringBytes().left__(content).right()
	if source_type == mousechsh_code_util_type_bytes and target_type == mousechsh_code_util_type_utf8string:
		return MouseChshUTF8StringBytes().right__(content).left()

	if source_type == mousechsh_code_util_type_base64string and target_type == mousechsh_code_util_type_bytes:
		return MouseChshBase64Bytes().left__(content).right()
	if source_type == mousechsh_code_util_type_bytes and target_type == mousechsh_code_util_type_base64string:
		return MouseChshBase64Bytes().right__(content).left()

	if source_type == mousechsh_code_util_type_hexstring and target_type == mousechsh_code_util_type_bytes:
		return MouseChshHexStringBytes().left__(content).right()
	if source_type == mousechsh_code_util_type_bytes and target_type == mousechsh_code_util_type_hexstring:
		return MouseChshHexStringBytes().right__(content).left()

	if source_type == mousechsh_code_util_type_urlstring and target_type == mousechsh_code_util_type_bytes:
		return MouseChshURLStringBytes().left__(content).right()
	if source_type == mousechsh_code_util_type_bytes and target_type == mousechsh_code_util_type_urlstring:
		return MouseChshURLStringBytes().right__(content).left()

	if source_type == mousechsh_code_util_type_utf8string and target_type == mousechsh_code_util_type_urlstring:
		data = MouseChshUTF8StringBytes().left__(content).right()
		return MouseChshURLStringBytes().right__(data).left()
	if source_type == mousechsh_code_util_type_urlstring and target_type == mousechsh_code_util_type_utf8string:
		data = MouseChshURLStringBytes().left__(content).right()
		return MouseChshUTF8StringBytes().right__(data).left()

	if source_type == mousechsh_code_util_type_utf8string and target_type == mousechsh_code_util_type_base64string:
		data = MouseChshUTF8StringBytes().left__(content).right()
		return MouseChshBase64Bytes().right__(data).left()
	if source_type == mousechsh_code_util_type_base64string and target_type == mousechsh_code_util_type_utf8string:
		data = MouseChshBase64Bytes().left__(content).right()
		return MouseChshUTF8StringBytes().right__(data).left()

	if source_type == mousechsh_code_util_type_utf8string and target_type == mousechsh_code_util_type_hexstring:
		data = MouseChshUTF8StringBytes().left__(content).right()
		return MouseChshHexStringBytes().right__(data).left()
	if source_type == mousechsh_code_util_type_hexstring and target_type == mousechsh_code_util_type_utf8string:
		data = MouseChshHexStringBytes().left__(content).right()
		return MouseChshUTF8StringBytes().right__(data).left()

	if source_type == mousechsh_code_util_type_hexstring and target_type == mousechsh_code_util_type_base64string:
		data = MouseChshHexStringBytes().left__(content).right()
		return MouseChshBase64Bytes().right__(data).left()
	if source_type == mousechsh_code_util_type_base64string and target_type == mousechsh_code_util_type_hexstring:
		data = MouseChshBase64Bytes().left__(content).right()
		return MouseChshHexStringBytes().right__(data).left()

	return None


mousechsh_code_util_hash_md5 = 'mousechsh:hash-md5'
mousechsh_code_util_hash_sha1 = 'mousechsh:hash-sha1'
mousechsh_code_util_hash_sha2_256 = 'mousechsh:hash-sha2-256'
mousechsh_code_util_hash_sm3 = 'mousechsh:hash-sm3'


@_mousechsh_crypto_lower_params_annotation('method', 'source_type', 'target_type')
def mousechsh_hash(
	content,
	*,
	method,
	source_type=mousechsh_code_util_type_bytes,
	target_type=mousechsh_code_util_type_bytes
):
	data = _mousechsh_crypto_plaintext_source_check(content, source_type=source_type)
	if data is None:
		return None

	if method == mousechsh_code_util_hash_md5:
		data = MouseChshMD5Bytes().content__(data).data()
	elif method == mousechsh_code_util_hash_sha1:
		data = MouseChshSHA1Bytes().content__(data).data()
	elif method == mousechsh_code_util_hash_sha2_256:
		data = MouseChshSHA2p256Bytes().content__(data).data()
	elif method == mousechsh_code_util_hash_sm3:
		data = MouseChshSM3Bytes().content__(data).data()
	else:
		return None

	return _mousechsh_crypto_ciphertext_target_check(data, target_type=target_type)


mousechsh_code_util_method_3des_192 = 'mousechsh:method-3des(192)'
mousechsh_code_util_method_aes_128 = 'mousechsh:method-aes(128)'
mousechsh_code_util_method_rsa_1024 = 'mousechsh:method-rsa(1024)'
mousechsh_code_util_method_rsa_2048 = 'mousechsh:method-rsa(2048)'
mousechsh_code_util_method_sm4_128 = 'mousechsh:method-sm4(128)'

mousechsh_code_util_mode_ecb = 'mousechsh:mode-ecb'

mousechsh_code_util_padding_pkcs1 = 'mousechsh:padding-pkcs1'
mousechsh_code_util_padding_pkcs5 = 'mousechsh:padding-pkcs5'
mousechsh_code_util_padding_pkcs7 = 'mousechsh:padding-pkcs7'

mousechsh_code_util_key_type_bytes = 'mousechsh:key-type-bytes'
mousechsh_code_util_key_type_utf8string = 'mousechsh:key-type-utf8string'
mousechsh_code_util_key_type_hexstring = 'mousechsh:key-type-hexstring'

mousechsh_code_util_key_format_hex_list = 'mousechsh:key-format-hex-list'
mousechsh_code_util_key_format_asn1_der_base64 = 'mousechsh:key-format-asn1-base64'
mousechsh_code_util_key_format_asn1_der_binary = 'mousechsh:key-format-asn1-binary'
mousechsh_code_util_key_format_asn1_cert = 'mousechsh:key-format-asn1-cert'


def _mousechsh_crypto_key_check(key, *, key_type):
	if key_type == mousechsh_code_util_key_type_bytes:
		if isinstance(key, bytes):
			key = key
		else:
			key = None
	elif key_type == mousechsh_code_util_key_type_utf8string:
		key = MouseChshUTF8StringBytes().left__(key).right()
	else:
		key = None
	return key


@_mousechsh_crypto_lower_params_annotation('source_type', 'source_format', 'target_type', 'target_format')
def mousechsh_crypto_key_convert(
	key: bytes,
	*,
	source_format,
	target_format,
	prefix: str = ''
):
	if not isinstance(key, bytes):
		return None
	if source_format == mousechsh_code_util_key_format_asn1_der_base64 \
		and target_format == mousechsh_code_util_key_format_asn1_cert:
		prefix = ''.join(
			list(filter(lambda ch: ch in '0123456789 ABCDEFGHIJKLMNOPQRSTUVWXYZ', str(prefix).upper()))
		).strip()
		result = bytes('-----BEGIN ' + prefix + '-----\n', 'utf-8')
		key_len = len(key)
		for i in range(0, key_len, 64):
			if key_len - i > 64:
				result += key[i: i + 64] + b'\n'
			else:
				result += key[i:]
		result += bytes('\n-----END ' + prefix + '-----', 'utf-8')
		key = result
	elif source_format == mousechsh_code_util_key_format_asn1_der_base64 \
		and target_format == mousechsh_code_util_key_format_asn1_der_binary:
		result = MouseChshUTF8StringBytes().right__(key).left()
		key = MouseChshBase64Bytes().left__(result).right()
	return key


@_mousechsh_crypto_lower_params_annotation('method')
def mousechsh_crypto_key_generate(
	*,
	method
):
	if method == mousechsh_code_util_method_rsa_1024:
		cryptor = MouseChshRSApECBpPKCS1().bit_len__(bit_len=1024).key_generate__()
		return {
			'public': cryptor.public_key(),
			'private': cryptor.private_key()
		}
	elif method == mousechsh_code_util_method_rsa_2048:
		cryptor = MouseChshRSApECBpPKCS1().bit_len__(bit_len=2048).key_generate__()
		return {
			'public': cryptor.public_key(),
			'private': cryptor.private_key()
		}

	return None


@_mousechsh_crypto_lower_params_annotation(
	'method', 'mode', 'padding', 'source_type', 'target_type', 'key_type', 'key_format'
)
def mousechsh_crypto_encrypt(
	content,
	*,
	method,
	mode,
	padding,
	source_type=mousechsh_code_util_type_bytes,
	target_type=mousechsh_code_util_type_bytes,
	public_key,
	key_type=mousechsh_code_util_key_type_bytes,
	key_format=mousechsh_code_util_key_format_hex_list
):
	key = _mousechsh_crypto_key_check(public_key, key_type=key_type)
	if key is None:
		return None

	data = _mousechsh_crypto_plaintext_source_check(content, source_type=source_type)
	if data is None:
		return None

	if method == mousechsh_code_util_method_3des_192:
		if mode == mousechsh_code_util_mode_ecb:
			if padding == mousechsh_code_util_padding_pkcs5:
				cryptor = MouseChsh3DESpECBpPKCS5().bit_len__(192)
				cryptor.key(key)
				data = cryptor.plaintext__(data).encrypt__().ciphertext()
			else:
				data = b''
		else:
			data = b''
	elif method == mousechsh_code_util_method_aes_128:
		if mode == mousechsh_code_util_mode_ecb:
			if padding == mousechsh_code_util_padding_pkcs5:
				cryptor = MouseChshAESpECBpPKCS5().bit_len__(128)
				cryptor.key(key)
				data = cryptor.plaintext__(data).encrypt__().ciphertext()
			else:
				data = b''
		else:
			data = b''
	elif method == mousechsh_code_util_method_sm4_128:
		if mode == mousechsh_code_util_mode_ecb:
			if padding == mousechsh_code_util_padding_pkcs5:
				cryptor = MouseChshSM4pECBpPKCS5().bit_len__(128)
				cryptor.key(key)
				data = cryptor.plaintext__(data).encrypt__().ciphertext()
			else:
				data = b''
		else:
			data = b''
	elif method == mousechsh_code_util_method_rsa_1024:
		if mode == mousechsh_code_util_mode_ecb:
			if padding == mousechsh_code_util_padding_pkcs1:
				if key_format == mousechsh_code_util_key_format_asn1_der_base64:
					key = mousechsh_crypto_key_convert(
						key,
						source_format=mousechsh_code_util_key_format_asn1_der_base64,
						target_format=mousechsh_code_util_key_format_asn1_der_binary,
						prefix='PUBLIC KEY'
					)
				cryptor = MouseChshRSApECBpPKCS1().bit_len__(1024)
				cryptor.public_key(key)
				data = cryptor.plaintext__(data).encrypt__().ciphertext()
			else:
				data = b''
		else:
			data = b''
	elif method == mousechsh_code_util_method_rsa_2048:
		if mode == mousechsh_code_util_mode_ecb:
			if padding == mousechsh_code_util_padding_pkcs1:
				if key_format == mousechsh_code_util_key_format_asn1_der_base64:
					key = mousechsh_crypto_key_convert(
						key,
						source_format=mousechsh_code_util_key_format_asn1_der_base64,
						target_format=mousechsh_code_util_key_format_asn1_der_binary,
						prefix='PUBLIC KEY'
					)
				cryptor = MouseChshRSApECBpPKCS1().bit_len__(2048)
				cryptor.public_key(key)
				data = cryptor.plaintext__(data).encrypt__().ciphertext()
			else:
				data = b''
		else:
			data = b''
	else:
		data = b''

	return _mousechsh_crypto_ciphertext_target_check(data, target_type=target_type)


@_mousechsh_crypto_lower_params_annotation(
	'method', 'mode', 'padding', 'source_type', 'target_type', 'key_type', 'key_format'
)
def mousechsh_crypto_decrypt(
	content,
	*,
	method,
	mode,
	padding,
	source_type=mousechsh_code_util_type_bytes,
	target_type=mousechsh_code_util_type_bytes,
	private_key,
	key_type=mousechsh_code_util_key_type_bytes,
	key_format=mousechsh_code_util_key_format_hex_list
):
	key = _mousechsh_crypto_key_check(private_key, key_type=key_type)
	if key is None:
		return None

	data = _mousechsh_crypto_ciphertext_source_check(content, source_type=source_type)
	if data is None:
		return None

	if method == mousechsh_code_util_method_3des_192:
		if mode == mousechsh_code_util_mode_ecb:
			if padding == mousechsh_code_util_padding_pkcs5:
				cryptor = MouseChsh3DESpECBpPKCS5().bit_len__(192)
				cryptor.key(key)
				data = cryptor.ciphertext__(data).decrypt__().plaintext()
			else:
				data = b''
		else:
			data = b''
	elif method == mousechsh_code_util_method_aes_128:
		if mode == mousechsh_code_util_mode_ecb:
			if padding == mousechsh_code_util_padding_pkcs5:
				cryptor = MouseChshAESpECBpPKCS5().bit_len__(128)
				cryptor.key(key)
				data = cryptor.ciphertext__(data).decrypt__().plaintext()
			else:
				data = b''
		else:
			data = b''
	elif method == mousechsh_code_util_method_sm4_128:
		if mode == mousechsh_code_util_mode_ecb:
			if padding == mousechsh_code_util_padding_pkcs5:
				cryptor = MouseChshSM4pECBpPKCS5().bit_len__(128)
				cryptor.key(key)
				data = cryptor.ciphertext__(data).decrypt__().plaintext()
			else:
				data = b''
		else:
			data = b''
	elif method == mousechsh_code_util_method_rsa_1024:
		if mode == mousechsh_code_util_mode_ecb:
			if padding == mousechsh_code_util_padding_pkcs1:
				if key_format == mousechsh_code_util_key_format_asn1_der_base64:
					key = mousechsh_crypto_key_convert(
						key,
						source_format=mousechsh_code_util_key_format_asn1_der_base64,
						target_format=mousechsh_code_util_key_format_asn1_der_binary,
						prefix='RSA PRIVATE KEY'
					)
				cryptor = MouseChshRSApECBpPKCS1().bit_len__(1024)
				cryptor.private_key(key)
				data = cryptor.ciphertext__(data).decrypt__().plaintext()
			else:
				data = b''
		else:
			data = b''
	elif method == mousechsh_code_util_method_rsa_2048:
		if mode == mousechsh_code_util_mode_ecb:
			if padding == mousechsh_code_util_padding_pkcs1:
				if key_format == mousechsh_code_util_key_format_asn1_der_base64:
					key = mousechsh_crypto_key_convert(
						key,
						source_format=mousechsh_code_util_key_format_asn1_der_base64,
						target_format=mousechsh_code_util_key_format_asn1_der_binary,
						prefix='RSA PRIVATE KEY'
					)
				cryptor = MouseChshRSApECBpPKCS1().bit_len__(2048)
				cryptor.private_key(key)
				data = cryptor.ciphertext__(data).decrypt__().plaintext()
			else:
				data = b''
		else:
			data = b''
	else:
		data = b''

	return _mousechsh_crypto_plaintext_target_check(data, target_type=target_type)


@_mousechsh_crypto_lower_params_annotation(
	'method', 'hash_method', 'mode', 'padding', 'source_type', 'target_type', 'key_type', 'key_format'
)
def mousechsh_crypto_sign(
	content,
	*,
	method,
	hash_method,
	mode,
	padding,
	source_type=mousechsh_code_util_type_bytes,
	target_type=mousechsh_code_util_type_bytes,
	private_key,
	key_type=mousechsh_code_util_key_type_bytes,
	key_format=mousechsh_code_util_key_format_hex_list
):
	key = _mousechsh_crypto_key_check(private_key, key_type=key_type)
	if key is None:
		return None

	data = _mousechsh_crypto_plaintext_source_check(content, source_type=source_type)
	if data is None:
		return None

	if method == mousechsh_code_util_method_rsa_1024:
		if mode == mousechsh_code_util_mode_ecb:
			if padding == mousechsh_code_util_padding_pkcs1:
				if key_format == mousechsh_code_util_key_format_asn1_der_base64:
					key = mousechsh_crypto_key_convert(
						key,
						source_format=mousechsh_code_util_key_format_asn1_der_base64,
						target_format=mousechsh_code_util_key_format_asn1_der_binary,
						prefix='RSA PRIVATE KEY'
					)
				if hash_method == mousechsh_code_util_hash_sha1:
					cryptor = MouseChshRSApECBpPKCS1withSHA1().bit_len__(1024)
					cryptor.private_key(key)
					data = cryptor.plaintext__(data).sign__().sign_text()
				elif hash_method == mousechsh_code_util_hash_sha2_256:
					cryptor = MouseChshRSApECBpPKCS1withSHA2p256().bit_len__(1024)
					cryptor.private_key(key)
					data = cryptor.plaintext__(data).sign__().sign_text()
				else:
					data = b''
			else:
				data = b''
		else:
			data = b''
	elif method == mousechsh_code_util_method_rsa_2048:
		if mode == mousechsh_code_util_mode_ecb:
			if padding == mousechsh_code_util_padding_pkcs1:
				if key_format == mousechsh_code_util_key_format_asn1_der_base64:
					key = mousechsh_crypto_key_convert(
						key,
						source_format=mousechsh_code_util_key_format_asn1_der_base64,
						target_format=mousechsh_code_util_key_format_asn1_der_binary,
						prefix='RSA PRIVATE KEY'
					)
				if hash_method == mousechsh_code_util_hash_sha1:
					cryptor = MouseChshRSApECBpPKCS1withSHA1().bit_len__(2048)
					cryptor.private_key(key)
					data = cryptor.plaintext__(data).sign__().sign_text()
				elif hash_method == mousechsh_code_util_hash_sha2_256:
					cryptor = MouseChshRSApECBpPKCS1withSHA2p256().bit_len__(2048)
					cryptor.private_key(key)
					data = cryptor.plaintext__(data).sign__().sign_text()
				else:
					data = b''
			else:
				data = b''
		else:
			data = b''
	else:
		data = b''

	return _mousechsh_crypto_ciphertext_target_check(data, target_type=target_type)


@_mousechsh_crypto_lower_params_annotation(
	'method', 'hash_method', 'mode', 'padding', 'source_type', 'sign_type', 'key_type', 'key_format'
)
def mousechsh_crypto_verify(
	content,
	sign,
	*,
	method,
	hash_method,
	mode,
	padding,
	source_type=mousechsh_code_util_type_bytes,
	sign_type=mousechsh_code_util_type_bytes,
	public_key,
	key_type=mousechsh_code_util_key_type_bytes,
	key_format=mousechsh_code_util_key_format_hex_list
):
	key = _mousechsh_crypto_key_check(public_key, key_type=key_type)
	if key is None:
		return False

	data = _mousechsh_crypto_plaintext_source_check(content, source_type=source_type)
	if data is None:
		return None

	data2 = _mousechsh_crypto_ciphertext_source_check(sign, source_type=sign_type)
	if data2 is None:
		return None

	if method == mousechsh_code_util_method_rsa_1024:
		if mode == mousechsh_code_util_mode_ecb:
			if padding == mousechsh_code_util_padding_pkcs1:
				if key_format == mousechsh_code_util_key_format_asn1_der_base64:
					key = mousechsh_crypto_key_convert(
						key,
						source_format=mousechsh_code_util_key_format_asn1_der_base64,
						target_format=mousechsh_code_util_key_format_asn1_der_binary,
						prefix='PUBLIC KEY'
					)
				if hash_method == mousechsh_code_util_hash_sha1:
					cryptor = MouseChshRSApECBpPKCS1withSHA1().bit_len__(1024)
					cryptor.public_key(key)
					return cryptor.plaintext__(data).sign_text__(data2).verify__().verity_result()
				elif hash_method == mousechsh_code_util_hash_sha2_256:
					cryptor = MouseChshRSApECBpPKCS1withSHA2p256().bit_len__(1024)
					cryptor.public_key(key)
					return cryptor.plaintext__(data).sign_text__(data2).verify__().verity_result()
	elif method == mousechsh_code_util_method_rsa_2048:
		if mode == mousechsh_code_util_mode_ecb:
			if padding == mousechsh_code_util_padding_pkcs1:
				if key_format == mousechsh_code_util_key_format_asn1_der_base64:
					key = mousechsh_crypto_key_convert(
						key,
						source_format=mousechsh_code_util_key_format_asn1_der_base64,
						target_format=mousechsh_code_util_key_format_asn1_der_binary,
						prefix='PUBLIC KEY'
					)
				if hash_method == mousechsh_code_util_hash_sha1:
					cryptor = MouseChshRSApECBpPKCS1withSHA1().bit_len__(2048)
					cryptor.public_key(key)
					return cryptor.plaintext__(data).sign_text__(data2).verify__().verity_result()
				elif hash_method == mousechsh_code_util_hash_sha2_256:
					cryptor = MouseChshRSApECBpPKCS1withSHA2p256().bit_len__(2048)
					cryptor.public_key(key)
					return cryptor.plaintext__(data).sign_text__(data2).verify__().verity_result()

	return False
