import hashlib

# encode it to bytes using UTF-8 encoding
message = "3eecc85e6440899b28a9ea6d8369f01c".encode()

# hash with MD5 (not recommended)
print("MD5:", hashlib.md5(message).hexdigest())