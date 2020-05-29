#!/usr/bin/python3

from base64 import *
import codecs

q2 = '01101100 01100101 01110100 01110011 00100000 01110100 01110010 01111001 00100000 01110011 01101111 01101101 01100101 00100000 01100010 01101001 01101110 01100001 01110010 01111001 00100000 01101111 01110101 01110100 00100001'

q2 = q2.split(' ')
a2 = ''
for bit in q2:
	a2 += chr(int(bit, 2))

print(a2)

q3 = 'MJQXGZJTGIQGS4ZAON2XAZLSEBRW63LNN5XCA2LOEBBVIRRHOM======'
a3 = b32decode(q3)
print(a3)

q4 = 'RWFjaCBCYXNlNjQgZGlnaXQgcmVwcmVzZW50cyBleGFjdGx5IDYgYml0cyBvZiBkYXRhLg=='
a4 = b64decode(q4)
print(a4)

q5 = '68 65 78 61 64 65 63 69 6d 61 6c 20 6f 72 20 62 61 73 65 31 36 3f'.replace(' ', '')
hex_decoder = codecs.getdecoder('hex_codec')
a5 = hex_decoder(q5)
print(a5[0])

q9 = '76 101 116 39 115 32 109 97 107 101 32 116 104 105 115 32 97 32 98 105 116 32 116 114 105 99 107 105 101 114 46 46 46'.split(' ')
a9 = ''
for q in q9:
	a9 += chr(int(q))
print(a9)