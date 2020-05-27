#!/usr/bin/python3

import codecs
import binascii

hexes = open('hexes').read()
decoded = binascii.unhexlify(hexes).decode()
decoded = decoded.split('\n')[1]
print(decoded)
# with open('id_rsa_crypt', 'w+') as writer:
# 	writer.write(decoded)