# TRACEBACK

## BASIC INFO
```
export IP=10.10.10.181
```

The website mentioned about web shell. Try to search for web shell by xh4H. Seems like there's a long list of web shell. He did mentioned he left a backdoor on it. So let us try all the web shell and we found smevk.php is on the shell. Using the web shell to upload a php reverse shell.

After we got a shell, run `sudo -l` to see what we can run. It shows that we can run `/home/sysadmin/luvit` as sysadmin. Running that program gives us a lua terminal. Maybe using that to run a lua script that spawn a shell? Create a `privesc.lua`.
```
os.system('/bin/bash')
```

Then run `sudo -u sysadmin /home/sysadmin/luvit privesc.lua` and we get a shell as sysadmin.

> - **user.txt**
>> e725932bdbbb7f4b26f7c85994061e05

Since we got access to the machine, we can add in our ssh public key into the `authorized_key` file so we can log in with ssh without password. When we log in with ssh, we saw a custom message displayed. Perhaps we can exploit that? navigate to `/etc/.update-motd.d` and `00-header` is writable. Great!

`echo 'cat /root/root.txt' >> 00-header` and then log in to the machine again with ssh and the root flag is displayed in the header.
*Note: The steps needs to be perform fast since the whole directory will be replace with the original from `/var/backup` every 30 seconds*
 
> - **root.txt**
>> ffe9536bf13aefd5be4032a1bddc8342