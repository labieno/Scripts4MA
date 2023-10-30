# RC4 decryption to dumped .rsrc

from Crypto.Cipher import ARC4
import binascii
import pefile

def rc4_decrypt(key, data):
	cipher = ARC4.new(key)
	decrypted = cipher.decrypt(data)
	return decrypted
	

def main():
	with open("rcdata.bin", "rb") as data:
		content = data.read()
		
		key = content[12:27]
		data = content[28:]
		
		with open("newbin.bin", "wb") as f:
			f.write(rc4_decrypt(key, data))


if __name__ == '__main__':
	main()