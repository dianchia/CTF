data = bytearray(open('reallyimportant.txt.enc', 'rb').read())
key = bytes('AdsipPewFlfkmll', 'utf-8')


def xor(data, key):
	l = len(key)
	return bytearray((
		(data[i] ^ key[i%l]) for i in range(0, len(data))
		))

print(xor(data, key).decode())