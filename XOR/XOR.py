#XORing stack strings
def decrypt(bytess, key):
    decrypted = ''
    for i in range(0,len(bytess),2):
        decrypted += chr(int(bytess[i:i+2], base=16) ^ key)
    print(decrypted)

# Stack strings:
#   0x7C6D1DBD1FEF1D5DDC6CCCBC5FEF891E
#   0x7CAD7CC86D1DDCAC1C4D1DEF0919FC
decrypt('7C6D1DBD1FEF1D5DDC6CCCBC5FEF891E'[::-1], 0xa2) #C:\Windows\Syste
decrypt('7CAD7CC86D1DDCAC1C4D1DEF0919FC'[::-1], 0xa2)   #m32\svchost.exe
