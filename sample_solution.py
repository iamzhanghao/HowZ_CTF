import hashlib
import time
from CFB import *

alphabet = 'abcdefghijklmnopqrstuvwxyz'

f = open("ciphered.pdf", 'rb')
input = f.read()

ba = bytearray(input)

f.close()

iv = hashlib.md5("FUN".encode('utf-8')).digest()



def append(digit, word):
    if digit == 0:
        key = hashlib.md5(word.encode('utf-8')).digest()
        plain = cfb_inv(ba, bytearray(key),iv)
        text = str(plain)
        if text.find("%PDF-") != -1:
            print("Found PDF file with key: ",word)
            f = open("decrypt.pdf", 'wb')
            f.write(plain)
            f.close()

    else:
        for i in alphabet:
            append(digit - 1, word + i)


start_time = time.time()

append(1, '')
#
# print("Time taken: ", time.time() - start_time, "s")
