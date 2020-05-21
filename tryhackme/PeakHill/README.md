# PEAK HILL

## BASIC INFO
```
export IP=10.10.138.203

```

Decode from binary to bytes, then unpickle them.
```
Username:  gherkin
Password:  p1ckl3s_@11_@r0und_th3_w0rld
```

uncompyle6
```
Username: dill
Password: n3v3r_@_d1ll_m0m3nt
```

> - **What is the user flag?**
>> f1e13335c47306e193212c98fc07b6a0

> - **What is the root flag?**
>> e88f0a01135c05cf0912cf4bc335ee28

Upon enumerating found interesting file in /opt. Because of the title of this challenge, wondering would it be pickle?

Tried some random thing first such as 'potato' and realize it has to be base64 encoded. Using this [script](eveilPickle.py) to generate a payload to execute `/bin/bash`. Now we're root. 

Navigate to root and trying to cat root.txt but failed? Seems like the name is modified with a space in front or maybe something else. Using wildcards also seems to be disabled. Nevermind, there's other tricks.

Running the command belowe gives us the root flag.
```
for f in `ls -R`; do cat "$f"; done
```