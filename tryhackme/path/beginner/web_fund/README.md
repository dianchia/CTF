# WEB FUNDAMENTALS

> - **What request verb is used to retrieve page content?**

>> GET


> - **What port do web servers normally listen on?**

>>80

> - **What's responsible for making websites look fancy?**

>> CSS

> - **VERB USED FOR LOGIN**

>>POST

> - **ONCE LOGIN, VERB USED TO RETRIEVE BANK BALANCE**

>> GET

> - **BODY OF GET REQUESTS MATTERS?**

>> Nay

> - **STATUS CODE FOR I'M A TEAPOT**

>>418

> - **UNAUTHENTICATED STATUS CODE**

>> 401

# BASIC INFO
```
export IP=10.10.172.218
```

> - **GET FLAG**
```
curl http://$IP:8081/ctf/get

```
>>>thm{162520bec925bd7979e9ae65a725f99f}

> - **POST FLAG**
```
curl http://$IP:8081/ctf/post --data flag_please

```
>>thm{3517c902e22def9c6e09b99a9040ba09}

> - **GET COOKIE FLAG**
```
curl http://$IP:8081/ctf/getcookie -c cookies.txt

```
>> thm{91b1ac2606f36b935f465558213d7ebd}

> - **SET COOKIE FLAG**
```
curl --cookie "flagpls=flagpls" http://$IP:8081/ctf/sendcookie

```
>> thm{c10b5cb7546f359d19c747db2d0f47b3}