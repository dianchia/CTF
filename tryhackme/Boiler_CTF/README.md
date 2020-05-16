# BOILER CTF

## BASIC INFO
```
export IP=10.10.25.92

open port:
	21 ftp
	80 http
	10000 ???
```

> - **File extension after anon login**
>> txt

Anonymous login is allowed on ftp.

> - **What is on the highest port?**
>> ssh

Running `nmap -p- $IP` shows that ssh is running on port 55007

> - **What's running on port 10000?**
>> webmin

It is shown in our nmap scan.

> - **Can you exploit the service running on that port? (yay/nay answer)**
>> nay

It is updated to the newest version. So, no.
> - **What's CMS can you access?**
>> Joomla

Enumerating with gobuster shows us there is a path named joomla.

> - **The interesting file name in the folder?**
>> log.txt

Further enumerating on /joomla leads us to a path `_test`. Sar2html? Searchsploit show that it is vulnerable to RCE.\
Using the path `/joomla/_test/index.php?plot=;<command here>` we first execute `ls` to see is there any interesting file. Seems like there is a log.txt. `cat log.txt` and we get the username and password we can use for ssh.
```
basterd : superduperp@$$
```

> - **Where was the other users pass stored(no extension, just the name)?**
>> backup

When we log in we saw a backup.sh. Reading it gives us the user and password.
```
USER=stoner
#superduperp@$$no1knows
```

> - **user.txt**
>> You made it till here, well done.

Log in with the credential we found before. `ls -la` and there is a .secret file. Read it.

> - **What did you exploit to get the privileged user?**
>> find

Running `find / -perm /4000 2>/dev/null` shows us `/usr/bib/find` has the SUID bit set. GTFOBins has just what we need to exploit it.

> - **root.txt**
>> It wasn't that hard, was it?
