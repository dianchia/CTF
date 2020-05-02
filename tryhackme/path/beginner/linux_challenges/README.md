# BASIC INFO

```
ip_addr = 10.10.65.202

```

# BASICS

>> flag1 = f40dc0cff080ad38a6ba9a1c2c038b2c

>> flag2 = 8e255dfa51c9cce67420d2386cede596

> flag3 `cat bash_history`
>> flag3 = 9daf3281745c2d75fc6e992ccfdedfcd

> flag4 `crontab -l`
>> flag4 = dcd5d1dcfac0578c99b7e7a6437827f3

> flag5 `locate flag5.txt`
>> flag5 = bd8f33216075e5ba07c9ed41261d1703

> flag6 `cat /home/flag6.txt | grep c9`
>> flag6 = c9e142a1e25b24a837b98db589b08be5

> flag7 `ps -aef`
>> flag7 = 274adb75b337307bd57807c005ee6358

> flag8 Simple uncompress
>> flag8 = 75f5edb76fe98dd5fc9f577a3f5de9bc

> flag9 in `cat /etc/hosts`
>> flag9 = dcf50ad844f9fe06339041ccc0d6e280

> flag10 `cat /etc/passwd | grep /bin/bash`
>> flag10 = 5e23deecfe3a7292970ee48ff1b6d00c

> flag11 `cat .bashrc | grep flag11`
>> flag11 = b4ba05d85801f62c4c0d05d3a76432e0

> flag12 `cat /etc/update-motd.d/00-header`
>> flag12 = 01687f0c5e63382f1c9cc783ad44ff7f

> flag13 `diff script1 script2`
>> flag13 = 3383f3771ba86b1ed9ab7fbf8abab531

> flag14 `cat /var/log/flagfourteen.txt`
>> flag14 = 71c3a8ad9752666275dadf62a93ef393

> flag15 `cat /etc/*release`
>> flag15 = a914945a4b2b5e934ae06ad6f9c6be45

>flag16 `ls /media/f/l/a/g/1/6/is`
>> flag 16 = cab4b7cae33c87794d82efa1e7f834e6

> flag17 `su alice with password TryHackMe123`
>> flag17 = 89d7bce9d0bab49e11e194b54a601362

> flag18 `cat .flag18`
>> flag18 = c6522bb26600d30254549b6574d2cef2

> flag19 `sed -n 2345p flag19`
>> flag19 = 490e69bd1bf3fc736cce9ff300653a3b

> flag20 `cat flag20 | base64 -d`
>> flag20 = 02b9aab8a29970db08ec77ae425f6e68

> flag21 `nano /home/bob/flag21.php`
>> flag21 = g00djob

> flag22 `cat flag22 | xxd -r -p`
>> flag22  = 9d1ae8d569c83e03d8a8f61568a0fa7d

> flag23 `cat flag23 | rev`
>> flag23 = ea52970566f4c090a7348b033852bff5

> flag24 `strings flag24`
>> flag24 = hidd3nStr1ng

> flag25 not exists

> flag26 `find / -xdev -type f -print0 2>/dev/null | xargs -0 grep -E '^[a-z0-9]{32}$' 2>/dev/null`
>> flag26 = 4bceb76f490b24ed577d704c24d6955d

> flag27 `sudo cat flag27`
>> flag27 = 6fc0c805702baebb0ecc01ae9e5a0db5

> flag28 `uname -a`
>> flag28 = 4.4.0-1075-aws

> flag29
```
cat flag29 | tr -d ' ' > flag29_noS
cat flag29_noS | tr -d '\n' > flag29_noSN
cat flag29_noSN
```
>> flag29 = fastidiisuscipitmeaei.

> flag30 `curl localhost`
>> flag30 = fe74bb12fe03c5d8dfc245bdd1eae13f

> flag31 
```
mysql -u root -p
SHOW DATABASES;
```
>> flag31 = 2fb1cab13bf5f4d61de3555430c917f4

> flag31_bonus 
```
use database_2fb1cab13bf5f4d61de3555430c917f4
SHOW TABLES;
SELECT * FROM flags;
```
>> flag31 = ee5954ee1d4d94d61c2f823d7b9d733c

> flag32 `scp alice@$IP:flag32.mp3 .`
>> flag32 = tryhackme1337

> flag33 `cat /home/bob/.profile`
>> flag33 = 547b6ceee3c5b997b625de99b044f5cf

> flag34 `printenv`
>> flag34 = 7a88306309fe05070a7c5bb26a6b2def

> flag35 `getent group`
>> flag35 = 769afb6

> flag36 `cat /etc/flag36`
>> flag36 = 83d233f2ffa388e5f0b053848caed1eb

```