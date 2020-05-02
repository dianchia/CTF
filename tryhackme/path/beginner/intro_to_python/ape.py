#!/usr/bin/python3

from base64 import *

with open('encodedflag.txt') as handler:
	data = handler.read()


for i in range(5):
	print("Decoding with b16 {} time".format(i + 1))
	data = b16decode(data)

print(data)

for i in range(5):
	print("Decoding with b32 {} time".format(i + 1))
	data = b32decode(data)

print(data)

for i in range(5):
	print("Decoding with b64 {} time".format(i + 1))
	data = b64decode(data)
	print(data)

print(data)