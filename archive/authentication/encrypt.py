#Fernet version:

# from cryptography.fernet import Fernet
# 
# 
# def encrypt(string):
    # key = "b'3nDjF_3SHlR2MmLB8YKMnpNVHFehNcePiaHvoPTUa5M='".encode('utf-8')
    # 
    # fernet = Fernet(key)
    # 
    # encString = fernet.encrypt(string.encode('utf-8'))
    # encString = encString.decode('utf-8')
    # return encString

import base64

def encrypt(string):
    encryptBytes = string.encode("ascii")
    encryptString = base64.b64encode(encryptBytes)
    encryptString = encryptString.decode("ascii")
    return encryptString

