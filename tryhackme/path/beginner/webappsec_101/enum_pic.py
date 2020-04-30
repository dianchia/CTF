#!/usr/bin/python3

import requests

url = "http://10.10.255.243/pictures/view.php?picid="

for i in range(100):
	u = url + str(i)
	print(u)
	resp = requests.get(url)
	print(resp.status_code)