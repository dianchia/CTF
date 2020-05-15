#!/usr/bin/python3

import requests
import string


url = 'http://10.10.58.24'

for c in string.ascii_uppercase:
	headers = {
	'User-Agent': c
	}
	resp = requests.get(url, headers=headers)
	if not 'Use your own' in resp.text:
		print("User-Agent is " + c)
		print(resp.text)
		break