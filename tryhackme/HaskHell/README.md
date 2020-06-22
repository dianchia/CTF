# HASKHELL

## BASIC INFO
```
export IP=10.10.167.147


PORT     STATE SERVICE VERSION
22/tcp   open  ssh     OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 1d:f3:53:f7:6d:5b:a1:d4:84:51:0d:dd:66:40:4d:90 (RSA)
|   256 26:7c:bd:33:8f:bf:09:ac:9e:e3:d3:0a:c3:34:bc:14 (ECDSA)
|_  256 d5:fb:55:a0:fd:e8:e1:ab:9e:46:af:b8:71:90:00:26 (ED25519)
5001/tcp open  http    Gunicorn 19.7.1
|_http-server-header: gunicorn/19.7.1
|_http-title: Homepage
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel
```

Navigate to `/submit` page submit reverse shell in haskell

Using wget to upload a more stable reverse shell from attacking computer because haskell reverse shell keeps breaking.

After getting a stable reverse shell, `cd` into `/home/prof` to get user.txt. Also grab the `id_rsa` in `.ssh`.

ssh into the machine as prof with the id_rsa we just got. Remember to change permission of the id_rsa before using it.`chmod 600 id_rsa`

`sudo -l` to see what we can do. Seems like we can run `/usr/bin/flask run` without password. Let's set the FLASK_APP environment first.

Create a `rev.py` with the following content.
```
import os
os.system('/bin/bash -p')
```
... then `export FLASK_APP=rev.py`\
Then run `/usr/bin/flask run` and we get a root shell. Just go to `/root` to grab the flag.


1. Get the flag in the user.txt file.
```
flag{acedemic_dishonesty}
```


2. Obtain the flag in root.txt
```
flag{im_purely_functional}
```