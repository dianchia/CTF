# ANTHEM

## BASIC INFO
```
export IP=10.10.41.225

open port:
	80		http
	135		msrpc
	139		netbios-ssn
	445		microsoft-ds?
	3389	ms-wbt-server
```


## WEBSITE ANALYSIS

> - **What port is for the web server?**
>> 80

> - **What port is for remote desktop service?**
>> 3389

> - **What is a possible password in one of the pages web crawlers check for?**
>> UmbracoIsTheBest!

> - **What CMS is the website using?**
>> Umbraco

> - **What is the domain of the website?**
>> Anthem.com

> - **What's the name of the Administrator**
>> Solomon Grundy

Search for admin in the search bar. One of the post wrote a poem about the admin. Search it up on google.

> - **Can we find find the email address of the administrator?**
>> `SG@anthem.com`

On the "we are hiring" post there's an example email for John Doe which is `JD@anthem.com`.

## SPOT THE FLAGS

> - **What is flag 1?**
>> THM{L0L_WH0_US3S_M3T4}

Inspect the source on the first post

> - **What is flag2?**
>> THM{G!T_G00D}

Inspect the soure on any page.

> - **What is flag3?**
>> THM{L0L_WH0_D15}

Inspect the source on /authors/

> - **What is flag4?**
>> THM{AN0TH3R_M3TA}

Inspect the source on the second post

## FINAL STAGE

Username:	SG
Password:	UmbracoIsTheBest!

> - **Gain initial access to the machine, what is the contents of user.txt?**
>> THM{N00T_NO0T}

> - **Can we spot the admin password?**
>> ChangeMeBaby1MoreTime

In a hidden directory on C:/ named backup. Have to add permission manually.

> - **Escalate your privileges to root, what is the contents of root.txt?**
>> THM{Y0U_4R3_1337}