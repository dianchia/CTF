# MADNESS

## BASIC INFO
```
export IP=10.10.98.59

open port:
	22	ssh
	80	http
```

On the main page, look into the source code. There is a thm.jpg. Download it with wget and examine why is it broken.\
Seems like the reason is because it starts wwith png forma file header instead of jpg. Let's change it to jpg format.
```
hidden directory
/th1s_1s_h1dd3n
```

Now on that directory, it wants a secret from us. The source code state that it is from 0-99.\
Brute-force it and we get the secret is 73.
```
y2RPJ4QaPF!B
```	

So what does this do...? Remeber the thm.jpg just now? Try steghide on it?
Got a username from it.
```
wbxre
```

Looks weird... ROT13?
```
joker
```
Now what about the password? He's a madman...\
The password is hidden on the image on THM. Yes the image on top of the question. Using steghide on it with no password gives us the password.
```
*axA&GF8dP
```

Now we can ssh into the machine.

> - **user.txt**
>> THM{d5781e53b130efe2f94f9b0354a5e4ea}

> - **root.txt**
>> THM{5ecd98aa66a6abb670184d7547c8124a}

Running `find / -prem /4000 2>/dev/null` shows us some binaries with SUID bit set. Screen seems like a good one to use huh. Refer to [screenroot.sh](screenroot.sh). Using this we get a root shell.