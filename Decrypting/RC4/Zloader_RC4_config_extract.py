# Zloader .data section RC4 decryption and config extraction
# Credit to Zero2Automated Course

from Crypto.Cipher import ARC4
import binascii
import pefile
import re

def rc4_decrypt(key, data):
	cipher = ARC4.new(key)
	decrypted = cipher.decrypt(data)
	return decrypted.decode("utf-8", 'ignore')

def locate_config_key(data):
	pattern = b"[a-z]{20}"
	match_object = re.search(pattern, data)
	print(match_object.start())

	key = data[match_object.start():match_object.end()]
	config = data[match_object.start()-751:match_object.start()]
	
	return config, key

def retrieve_config(filename):
	pe = pefile.PE(filename)

	for section in pe.sections:
		if ".data" in str(section.Name):
			data_section = section.get_data()
	
	return locate_config_key(data_section)
	

def main():
	#filename = input("Filename: ")
	filename = "zloader.bin"
	encrypted_config, key = retrieve_config(filename)
	print(encrypted_config)
	print(key)
	print(rc4_decrypt(key, encrypted_config))

if __name__ == '__main__':
	main()
