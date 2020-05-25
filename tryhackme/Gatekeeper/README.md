# GATE KEEPER

## BASIC INFO
```
export IP=10.10.112.179

```

> - **Locate and find the User Flag.**
>> {H4lf_W4y_Th3r3}

Using `smbclient -L` to enumerate the machine. Found `Users` available to log in. Get gatekeeper.exe from there and it is just some simple buffer overflow. Using msfvenom to generate a reverse tcp payload for windows, then set up a listener in msfconsole. Run the [exploit](get_shell.py) and now we're in.

> - **Locate and find the Root Flag**
>> {Th3_M4y0r_C0ngr4tul4t3s_U}

`run post/windows/gather/enum_applications` on msfconsole to gather the application running. we discover that Firefox is running. Using `post/multi/gather/firefox_creds` to for credential dump. Once we got it, rename the file to `cert9.db`, `cookies.sqlite`, `key4.db` and `logins.json`. Then run [firefox_decrypt.py](https://github.com/unode/firefox_decrypt) on it and we got the credentials.
```
mayor:8CL7O1N78MdrCIsV
```

Now we run `psexec.py` from [impacket](https://github.com/SecureAuthCorp/impacket) to log in as mayor.