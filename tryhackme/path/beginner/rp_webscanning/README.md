# BASIC INFO

```
export IP=10.10.228.95
```

# USING NIKTO

> - **Switch used to set target host**
>> -h
>
> - **Disable secure transport**
>> -nossl
>
> - **Force secure transport**
>> -ssl
>
> - **Set specific port**
>> -p
>
> - **Verify database is working and free from error**
>> -dbcheck
>
> - **Enumerate usernames in Apache**
>> -mutate 3
>
> - **Credential check**
>> -id admin:PrettyAwesomePassword1234
>
> - **Scan target. Version of the webserver**
>> Apache/2.4.7

> - **Directory indexed that really shouldn't be**
>> config

> - **Limit scan to end at a certain time**
>> -until

> - **List all available plugins**
>> -list-plugins

> - **Use plugin checks to find out dated software**
>> -Plugins outdated

> - **Plugins run a standard test**
>> -Plugins tests

# USING OWASP-ZAP

> - **Option to set in order to attack**
>> URL to attack

> - **File contains pages of sections to avoid**
>> robots.txt

> - **Entry disallowed in the file**
>> /

> - **Directory that contains images of application**
>> /dvwa/images

> - **Website doesn't force secure connection. Related cookie?**
>> HttpOnly

> - **Warning produced by ZAP on XSS**
>> Web Browser XSS Protection Not Enabled

> - **Out of scope site**
>> http://www.dvwa.co.uk

> - **HTTP methods that requests content**
>> GET

> - **HTTP methods that submid content**
>> POST