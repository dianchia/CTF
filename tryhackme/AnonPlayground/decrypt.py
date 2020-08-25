import string

s = 'hEzAdCfHzA::hEzAdCfHzAhAiJzAeIaDjBcBhHgAzAfHfN'

s1 = s[::2]
s2 = s[1::2]

chars = string.ascii_lowercase
flag = ''

def index(c):
	return (ord(c) & 31)

for c1, c2 in zip(s1, s2):
	if c1 == ':':
		flag += ':'
		continue
	idx = index(c1) + index(c2)
	idx = idx % 26
	flag += chars[idx - 1]

print(flag)