#!/usr/bin/python3

from base64 import *

crest1 = 'S0pXRkVVS0pKQkxIVVdTWUpFM0VTUlk9'
crest2 = 'GVFWK5KHK5WTGTCILE4DKY3DNN4GQQRTM5AVCTKE'
crest3 = 'MDAxMTAxMTAgMDAxMTAwMTEgMDAxMDAwMDAgMDAxMTAwMTEgMDAxMTAwMTEgMDAxMDAwMDAgMDAxMTAxMDAgMDExMDAxMDAgMDAxMDAwMDAgMDAxMTAwMTEgMDAxMTAxMTAgMDAxMDAwMDAgMDAxMTAxMDAgMDAxMTEwMDEgMDAxMDAwMDAgMDAxMTAxMDAgMDAxMTEwMDAgMDAxMDAwMDAgMDAxMTAxMTAgMDExMDAwMTEgMDAxMDAwMDAgMDAxMTAxMTEgMDAxMTAxMTAgMDAxMDAwMDAgMDAxMTAxMTAgMDAxMTAxMDAgMDAxMDAwMDAgMDAxMTAxMDEgMDAxMTAxMTAgMDAxMDAwMDAgMDAxMTAwMTEgMDAxMTEwMDEgMDAxMDAwMDAgMDAxMTAxMTAgMDExMDAwMDEgMDAxMDAwMDAgMDAxMTAxMDEgMDAxMTEwMDEgMDAxMDAwMDAgMDAxMTAxMDEgMDAxMTAxMTEgMDAxMDAwMDAgMDAxMTAwMTEgMDAxMTAxMDEgMDAxMDAwMDAgMDAxMTAwMTEgMDAxMTAwMDAgMDAxMDAwMDAgMDAxMTAxMDEgMDAxMTEwMDAgMDAxMDAwMDAgMDAxMTAwMTEgMDAxMTAwMTAgMDAxMDAwMDAgMDAxMTAxMTAgMDAxMTEwMDA='
crest4 = 'gSUERauVpvKzRpyPpuYz66JDmRTbJubaoArM6CAQsnVwte6zF9J4GGYyun3k5qM9ma4s'

crest1 = b64decode(crest1)
crest2 = b32decode(crest2)
crest3 = b64decode(crest3)
crest4 = '705a4756665a6d39795a585a6c63673d3d' #b58decode
# print(crest2)

crest3 = crest3.split(' ')
# print(crest3)
crest3 = [chr(int(x, 2)) for x in crest3]
crest3 = ''.join(crest3)
crest3 = crest3.split(' ')
crest3 = [x.decode('hex') for x in crest3]
crest3 = ''.join(crest3)

crest1 = b32decode(crest1)
crest2 = 'h1bnRlciwgRlRQIHBh' # b58decode
crest4 = crest4.decode('hex')
crests = ''.join([crest1, crest2, crest3, crest4])
print(b64decode(crests))