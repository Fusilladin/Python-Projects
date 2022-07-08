#config utf-8

import argparse
import hashlib


#parsing
parser = argparse.ArgumentParser(description='hashing given password')
parser.add_argument('password', help='Input Password you want to hash')
parser.add_argument('-t','--type', choices=['sha256','sha512','md5'])
args = parser.parse_args()

# hashing given password
password = args.password
hashtype = args.hashtype

x = getattr(hashlib, hashtype)()
x.update(password.encode())

# Output
print("< hash-type: " + hashtype + ">")
print(x.hexdigest())













#
