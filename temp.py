import hashlib

key = hashlib.md5("HowZ".encode('ascii')).hexdigest()

print(key)