# HACKING WITH POWERSHELL

## BASIC POWERSHELL COMMAND
> - **What is the location of the file "interesting-file.txt"**
>> C:\Program Files

using `Get-ChildItem -Include \*interesting\* -Path C:\ -Recurse`

> - **Specify the contents of this file**
>> notsointerestingcontent

`Get-Content -Path "C:\Program Files\interesting-file.txt.txt"`

> - **How many cmdlets are installed on the system(only cmdlets, not functions and aliases)?**
>> 6638

`(Get-Command -Type Cmdlet).count`

> - **Get the MD5 hash of interesting-file.txt**
>> 49A586A2A9456226F8A1B4CEC6FAB329

`Get-FileHash "C:\Program Files\interesting-file.txt.txt" -Algorithm MD5`

> - **What is the command to get the current working directory?**
>> Get-Location

> - **Does the path "C:\Users\Administrator\Documents\Passwords" Exist(Y/N)?**
>> N

`Test-Path "C:\Users\Administrator\Documents\Passwords"`

> - **What command would you use to make a request to a web server?**
>> Invoke-WebRequest

> - **Base64 decode the file b64.txt on Windows.**
>> ihopeyoudidthisonwindows

```
$EncodedeString = Get-Content b64.txt
[System.Text.Encoding]::UTF8.GetString([System.Convert]::FromBase64String($EncodedString))
```

## ENUMERATION

> - **How many users are there on the machine?**
>> 5

`Get-LocalUser`

> - **Which local user does this SID(S-1-5-21-1394777289-3961777894-1791813945-501) belong to?**
>> Guest

`Get-LocalUser | select name, SID`

> - **How many users have their password required values set to False?**
>> 4

`Get-LocalUser | select PasswordRequired`

> - **How many local groups exists**
>> 24

`(Get-LocalGroup).count`

> - **What command did you use to get the IP address info?**
>> Get-NetIPAddress

> - **How many ports are listed as listening?**
>> 20

`(Get-NetTCPConnection -state Listen).count`

> - **What is the remote address of the local port listening on port 445?**
>> ::

> - **How many patches have been applied?**
>> 20

`(Get-HotFix).count`

> **When was the patch with ID KB4023834 installed?**
>> 6/15/2017 12:00:00 AM

`Get-HotFix | where-object HotFixID -eq KB4023834 | select InstalledOn`

> - **Find the contents of a backup file.**
>> backpassflag

```
Get-ChildItem -Path C:\ -Include *.bak* -File -Recurse
```

> - **Search for all files containing API_KEY**
>> fakekey123

`Get-ChildItem -Path C:\ -recurse | Select-String -pattern API_KEY`


> - **What command do you do to list all the running processes?**
>> Get-Process

> - **What is the path of the scheduled task called new-sched-task?**
>> /

`Get-ScheduledTask | Where-Object TaskName -eq new-sched-task`

> - **Who is the owner of the C:\\**
>>NT SERVICE\TrustedInstaller

`Get-ACL -Path C:\`

## SCRIPTING CHALLENGE

> - **What file contains the password?**
>> Doc3M

```
$path = "C:\Users\Adminstrator\Desktop\emails\*"
$exec = Get-ChildItem $path -recurse | Select-String -pattern password
```

> - **What is the password?**
>> johnisalegend99

> - **What files contains an HTTPS link?**
>> Doc2Mary

## INTERMEDIATE SCRIPTING

> - **How many open ports did you find between 130 and 140(inclusive of those two)?**
>> 11