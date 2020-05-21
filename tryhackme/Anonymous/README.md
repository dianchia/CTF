# ANONYMOUS

## BASIC INFO
```
export IP=10.10.14.100

```

> - **Enumerate the machine.  How many ports are open?**
>> 4

> - **What service is running on port 21?**
>> ftp

> - **What service is running on ports 139 and 445?**
>> smb

> - **There's a share on the user's computer.  What's it called?**
>> pics

> - **user.txt**
>> 90d6f992585815ff991e68748c414740

> - **root.txt**
>> 4d930091c31a622a7ed10f27999af363

Using anonymous to log on to ftp. clean.sh seems interesting... It should be executed by the machine periodically. Since it's writable as well maybe we can inject a reverse shell into it. On our local machine create a file name clean.sh which contains our reverse shell and mput it onto the remote machine. Set up a listener and wait for awhile.

After we got in to the machine and acquired the user.txt, let's start to priv esc. Try looking for binaries with SUID set. `/usr/bin/env` seems like one that we can exploit. `env -p /bin/bash` and we're root.