# RETRO CTF

## BASIC INFO
```
export IP=10.10.178.233
open port:
	80 http
	3389 rdesktop
```

Found hidden directory /retro and it is a wordpress.\
Found the user wade. Click on his name to view all his activities.\
Commented on one of the post... with his password?
```
wade:parzival
```

xfreerdp into the machine with the credentials above and port 3389.

> - **user.txt**
>> 3b99fbdc6d430bfb51c72c651a261927

> -**root.txt**
>> 7958b569565d7bd88d10c6f22d1c4063

The hint saying to figure out what the user last was trying to find. So we went into the browser history. CVE-2019-1388? So apparently this was a bug in Windows which lets you escalate you privilege. We need to download a executable hhupd.exe but luckily it is downloaded and placed in recycle bin. We just need to restore the file. Before we perform the exploit, start up both IE and Chrome because sometimes the exploit might not work due to no options is present when choosing app to open the link.
Now right click on the executable and choose 'run as administrator'. A screen will pop out and ask to enter password. Click on 'show more information' then click on 'view certificate'. Next click on the hyperlink and choose to open with IE. Now in IE, choose to 'save as' or 'open file' then on the pop up window, open cmd. Now we are admin.

## ALTERNATE

Download this [CVE-2017-0213_x64.exe](https://github.com/SecWiki/windows-kernel-exploits/tree/master/CVE-2017-0213)\
Then upload it to the machine. Run it and we are admin.

![badges](../../../badges/dianchia.png)