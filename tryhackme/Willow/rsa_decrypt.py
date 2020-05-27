#!/usr/bin/python3
from Crypto.Util.number import getPrime, inverse
import binascii

'''
Public Key Pair: (23, 37627)
Private Key Pair: (61527, 37627)
'''

e = 23
n = 37627
d = 61527

p, q = 191, 197

phi = ( q - 1 ) * ( p - 1 )


cs = open('id_rsa_crypt').read().split(' ')

id_rsa = ''
for c in cs:
	if c:
		c = int(c)
		m = pow( c, d, n )
		id_rsa += chr(m)

with open('id_rsa', 'w+') as writer:
	writer.write(id_rsa)