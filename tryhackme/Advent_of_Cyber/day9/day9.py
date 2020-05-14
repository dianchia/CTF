#!/usr/bin/python3

import requests

url = 'http://10.10.169.100:3000'
n = "/"
flag = ""

while True:
	r = requests.get(url + n)
	n = '/'
	n += r.json()['next']
	print('next ' +  n)
	if n == '/end':
		break
	flag += r.json()['value']

print(flag)