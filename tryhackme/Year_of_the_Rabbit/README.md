# YEAR OF THE RABBIT

## BASIC INFO
```
export IP=10.10.60.194

open port:
	21	ftp
	22	ssh
	80	http
```

Using gobuster to fuzz for subdirectory. Found /assets\
In /assets/style.css found /sup3r_s3cr3t_fl4g.php.\
Navigating there leads us to a youtube video... I don't wanna talk about it...
Suspect something is going on behind. Using brup suite to check. One of the redirects leads us to /WExYY2Cv-qU.

On that directory, download Hot_Babe.png. Use zsteg to extract. Got username for ftp and some [password](password.txt).
`hydra -l ftpuser -P password.txt ftp://$IP`
```
username:ftpuser
password:5iez1wGXKfPKQ
```

mget Eli's_Cred.txt.\
Looks familiar? It is brainfuck. Using tio.run to see what it contains.
```
User: eli
Password: DSpDiM1wAEwid
```

Upon ssh log in to the machine, saw this message:\
> Gwendoline, I am not happy with you. Check our leet s3cr3t hiding place. I've left you a hidden message there.

Seems strange, just note it down. Might be useful.\
Looking for user.txt... It's not in eli's home. Using locate found it at gwendoline's home. Let's try to find s3cr3t? `find / -name s3cr3t 2>/dev/null` and found it at /usr/games/s3cr3t.

```
gwendoline
MniVCQVhQHUNI
```
Log in as gwendoline and grab the user.txt. Now on to rooting the machine.

Running `sudo -l` gives us the following result.
> (NOPASSWD, !root) /usr/bin/vi /home/gwendoline/user.txt

NOPASSWD, !root eh, sound like some sudo vulnerability it is.`sudo -u#-1 /usr/bin/vi /home/gwendoline/user.txt` to open vi as sudo, then `:!sh`. Now we're root.

> - **User.txt**
>> THM{1107174691af9ff3681d2b5bdb5740b1589bae53}

> - **Root.txt**
>> THM{8d6f163a87a1c80de27a4fd61aef0f3a0ecf9161}