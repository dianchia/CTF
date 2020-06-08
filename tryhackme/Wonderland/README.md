# WONDERLAND

## BASIC INFO
```
export IP=10.10.54.101
```

Running nmap on the IP reveals a web server on port 80.
Once we navigate to the web page we were greeted by a picture. Download it and using steghide to extract data with no password gives us a hint.txt.
```
follow the r a b b i t
```

According to the hint, we navigate to `http://$IP/r/a/b/b/i/t` and look at the source code. Then we can get the password for alice.
```
alice:HowDothTheLittleCrocodileImproveHisShiningTail
```

ssh into the machine with the credentials above. We saw a root.txt which is not readable by us. But where is the user.txt? Poking around and trying to `ls` the `/root` directory shows permission denied. But what if user.txt is inside and it is world readable?
```bash
cat /root/user.txt
```
... and we get the user flag.

1. user.txt
```
thm{"Curiouser and curiouser!"}
```



Now on our way to priv esc. First we can see a python script `walrus_and_the_carpenter.py` and running `sudo -l` give the following output.
```
(rabbit) /usr/bin/python3.6 /home/alice/walrus_and_the_carpenter.py
```
seems like we can run the python script as user rabbit. `scp` the script and by reading it we see that it imports random module. By default python will search for the module on current working directory, so we can abuse this.

Create a `random.py` on alice's home directory, then include a reverse shell in it. Set up a listener on host machine, then run
```
sudo -u rabbit /usr/bin/python3.6 /home/alice/walrus_and_the_carpenter.py
```
... and we're in as rabbit




In rabbit's home directory, there's only one thing which is `teaParty`. Running it gives us segmentation fault every single time no matter the length of the input we provide. Download it by first copy it into `/dev/shm` and then scp with alice's credentials.

Fire up ghidra and take look at the binary.
```
system("/bin/echo -n \'Probably by \' && date --date=\'next hour\' -R");
```
This line of code seems vulnerable since it did not use absolute path on the `date` command. So we can abuse that to get another reverse shell.

Go into `/tmp` and create a file named `date`. Include our reverse shell inside.
Now we modify the PATH variable.
```
export PATH=/tmp:$PATH
```
... and set up a listener on our host machine again. Then run the binary and we're now hatter.
*Note: use python3 instead of python if using python reverse shell from pentest monkey*



In hatter's home directory there's a `password.txt` which include hatter's password. Exit the reverse shell and `su` to hatter from alice's shell. 
```
hatter:WhyIsARavenLikeAWritingDesk?
```

Now we search for file that are owned by hatter or hatter group. `/usr/bin/perl` seems interesting because it can only be executed by hatter or root. Search on gtfobins shows that perl can manipulate its process UID and can be used on Linux as a backdoor to maintain elevated privileges with the `CAP_SETUID` capability set. Previously when running `linPeas.sh` on this machine shows that the `CAP_SETUID` capability is set. So we just need to run the following command.
```
perl -e 'use POSIX qw(setuid); POSIX::setuid(0); exec "/bin/sh";'
```
... and we're root.

2. root.txt
```
thm{Twinkle, twinkle, little bat! How I wonder what you’re at!}
```