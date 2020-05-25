# CONVERT MY VIDEO

## BASIC INFO
```
export IP=10.10.22.217
```


> - **What is the name of the secret folder?**
>> admin

> - **What is the user to access the secret folder?**
>> itsmeadmin

The process to get this answer will be shown later

> - **What is the user flag?**
>> flag{0d8486a0c0c42503bb60ac77f4046ed7}

On the website there is a field for input. Wonder can we exploit that... Fire up burpsuite and try to modify the payload and boom, we found a way for RCE. The details is shown in this [script](get_shell.py). Briefly explain, we replace the yt_url with command that we want to execute and surround it with ';' and replace and whitespaces with tabs since it removes our whitespaces. Now we got a reverse shell.

Once we got a reverse shell, we can check out the flag.txt. Also, to get the answer for question 2, we check out .htpasswd in admin directory.
```
.htpasswd
itsmeadmin:jessie
```

> - **What is the root flag?**
>>flag{d9b368018e912b541a4eb68399c5e94a}

There is a clean.sh in /var/www/html/tmp. At first it doesn't stand out to me but when I created a `downloads` directory in tmp, went for a break and come back and realize it is gone, I suspect that it is a scheduled cronjobs. So I modify the clean.sh and make it a reverse shell but I only got access of www-data instead of root. Trying to modify the permission then. Let's set it with SUID bit and we got a root shell.