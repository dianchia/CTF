# BASIC INFO

```
export IP=10.10.228.95
```

# USING NIKTO

> 1. Switch used to set target host
>> -h
>
> 2. Disable secure transport
>> -nossl
>
> 3. Force secure transport
>> -ssl
>
> 4. Set specific port
>> -p
>
> 5. Verify database is working and free from error
>> -dbcheck
>
> 6. Enumerate usernames in Apache
>> -mutate 3
>
> 7. Credential check
>> -id admin:PrettyAwesomePassword1234
>
> 8. Scan target. Version of the webserver
>> Apache/2.4.7