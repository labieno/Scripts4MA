#ROT13 with custom alphabet:
def decryptit(string):
    key = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ01234567890./="
    decrypted_str = ""
    for c in string:
        i = key.find(c)
        if (i + 13) < len(key):
            v8 = i + 13
        else:
            v8 = i - len(key) + 13
        decrypted_str += key[v8]
    
    print(decrypted_str)
