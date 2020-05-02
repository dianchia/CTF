#!/usr/bin/python3

from base64 import *

with open('b64.txt') as handle:
	data = handle.read()

for _ in range(50):
	data = b64decode(data)

print(data)