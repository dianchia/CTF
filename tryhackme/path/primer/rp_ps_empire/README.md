# RP: PS EMPIRE

## BASIC INFO 
```
export IP=10.10.29.216
open port:
	135/tcp   open  msrpc
	139/tcp   open  netbios-ssn
	445/tcp   open  microsoft-ds
	3389/tcp  open  ms-wbt-server
	49152/tcp open  unknown
	49153/tcp open  unknown
	49154/tcp open  unknown
	49158/tcp open  unknown
	49160/tcp open  unknown


```

# DEPLOY!
> - **Deploy this machine and learn what exploitation this box is susceptible to!**
>> No answer needed
- RCE in Microsoft SMBv1 servers (ms17-010)
	- CVE-2017-0143
The host is vulnerable to eternal blue.

> - **Exploit the vulnerability to spawn a reverse shell!**
>> No answer needed

# **Empire is currently broken**