# IcedID .data section RC4 decryption and config extraction
# Credit to Zero2Automated Course

from Crypto.Cipher import ARC4
import binascii
import pefile

def rc4_decrypt(key, data):
	cipher = ARC4.new(key)
	decrypted = cipher.decrypt(data)
	return decrypted

def config_extract(filename):
	pe = pefile.PE(filename)
	for section in pe.sections:
		if ".data" in str(section.Name):
			return section.get_data()
	

def main():
	#filename = input("Filename: ")
	filename = "new_iced_dump.bin"
	data = config_extract(filename)

	key = data[:8]
	data = data[8:592]

	print(rc4_decrypt(key, data))



if __name__ == '__main__':
	main()
