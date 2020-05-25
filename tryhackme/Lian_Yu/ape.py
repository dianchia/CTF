#!/usr/bin/python3

import requests

url = "http://10.10.183.167/island/2100"

# for i in range(1000):
# 	resp = requests.get(url + str(i).zfill(4))
# 	if resp.status_code == 200:
# 		print("Found the directory!")
# 		print(i)
# 		break
# 	else:
# 		print(str(i).zfill(4) + " doesn't exists", end="\r")

data = {
	"ticket": "vigilante"
}

resp = requests.get(url, data=data)
print(resp.content)