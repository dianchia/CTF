# WILLOW

## BASIC INFO
```
export IP=10.10.243.72

```

Landing page is hexed. Decode it and we get a encrypted SSH Private Key
```
Hey Willow, here's your SSH Private key -- you know where the decryption key is!
```

`showmount -e $IP` shows a /var/failsafe. Let's try to mount that.\
`mount $IP:/var/failsafe mnt/` and there's a rsa_keys inside.
```
Public Key Pair: (23, 37627)
Private Key Pair: (61527, 37627)
```

With the public and private key pair we can now decrypt the message. Refer to [rsa_decrypt.py](rsa_decrypt.py) for how to do it.

After we decrypt the rsa, we need a passphrase. Running ssh2john.py and john will crack the password for us.
```
id_rsa passphrase:
wildflower
```

Now when we log in we see a `user.jpg`. Just download it using scp.

Next up we try for PrivEsc.\
Running `sudo -l` shows we can run `mount /dev/*` as sudo. Let's see is there anything we want in /dev/. Seems like there is a `hidden_backup`, mount thath to `/mnt/creds` and `cat creds.txt`
```
root:7QvbvBTvwPspUK
willow:U0ZZJLGYhNAT2s
```

Switch to root and cat out root.txt doesn't give us the flag. Instead it says that he gives us the flag awhile ago? Maybe somthing is hidden in the user.jpg? Using steghide on it and root password as passphrase gives us the root flag.

> - **User Flag:**
>> THM{beneath_the_weeping_willow_tree}

> - **Root Flag:**
>> THM{find_a_red_rose_on_the_grave}