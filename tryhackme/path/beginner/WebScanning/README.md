# BASIC INFO

```
export IP=10.10.228.95
```

# USING NIKTO

> 1. Switch used to set target host
>> -h
>
> 1. Disable secure transport
>> -nossl
>
> 1. Force secure transport
>> -ssl
>
> 1. Set specific port
>> -p
>
> 1. Verify database is working and free from error
>> -dbcheck
>
> 1. Enumerate usernames in Apache
>> -mutate 3
>
> 1. Credential check
>> -id admin:PrettyAwesomePassword1234
>
> 1. Scan target. Version of the webserver
>> Apache/2.4.7