# NAX

## BASIC INFO
```
export IP=10.10.232.128
```

> - **What hidden file did you find?**
>> /PI3T.PNg

On the landing page we saw some elements. Search for a periodic table and decode them.

> - **Who is the creator of the file?**
>> Piet Mondrian

exiftool

> - **What is the username you found?**
>> nagiosadmin

This is the default admin username

> - **What is the password you found?**
>> %n3p3UQ&9BjLp4$7uhWdY

While searching online for stego in png I came across [this website](https://0xrick.github.io/lists/stego/). It mentioned a type of esoteric language [npiet online](https://www.bertnase.de/npiet/npiet-execute.php) which progrmas written in it are images. Using this to decode the image we got earlier gives us the password.\
*Note: % is a seperator*

> - **What is the CVE number for this vulnerability? This will be in the format: CVE-0000-0000**
>> CVE-2019-15949

> - **After Metasploit has started, let's search for our target exploit using the command 'search applicationame'. What is the full path (starting with exploit) for the exploitation module?**
>> exploit/linux/http/nagios_xi_authenticated_rce

> - **Compromise the machine and locate user.txt**
>> THM{84b17add1d72a9f2e99c33bc568ae0f1}

> - **Locate root.txt**
>> THM{c89b2e39c83067503a6508b21ed6e962}

We are in a root shell.