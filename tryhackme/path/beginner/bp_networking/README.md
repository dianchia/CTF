# BP: NETWORKING

**IP Address Classes**


Class | Range
--------| ---------
Class A | 1 - 127
Class B | 128 - 191
Class C | 192 - 223
Class D | 224 - 239
Class E | 240 - 255

**Private Address Space**

Class | Range
----- | ------
Class A | 10.0.0.0
Class B | 172.16.0.0 - 172.31.255.255
Class C | 192.168.0.0 - 192.168.255.255

-------------------------------------------------------------------------

> - **How many categories of IPv4 addresses are there?**
>> 5
>>
> - **Which type is for research? \*Looking for a letter rather than a number here**
>> E
>>
> - **How many private address ranges are there?**
>> 3
>>
> - **Which private range is typically used by businesses?**
>> A
>>
> - **There are two common default private ranges for home routers, what is the first one?**
>> 192.168.0.0
>>
> - **How about the second common private home range?**
>> 192.168.1.0
>>
> - **How many addresses make up a typical class C range? Specifically a /24**
>> 256
>>
> - **Of these addresses two are reserved, what is the first addresses typically reserved as?**
>> Network
>>
> - **The very last address in a range is typically reserved as what address type?**
>> Broadcast
>>
> - **A third predominant address type is typically reserved for the router, what is the name of this address type?**
>> Gateway
>>
> - **Which address is reserved for testing on individual computers?**
>> 127.0.0.1
>>
> - **A particularly unique address is reserved for unroutable packets, what is that address? This can also refer to all IPv4 addresses on the local machine.**
>> 0.0.0.0

-------------------------------------------------------------------------
-------------------------------------------------------------------------

## Binary to Decimal

An IPv4 address consists of 32 bits split up into four sections of eight bit. For example, the address 192.168.1.12 translates to this:
```
11000000 10101000 00000001 00001100
```

Break down of the second octet valuing 168:

Decimal | Binary
--------|--------
128 | 1
64 | 0
32 | 1
16 | 0
8 | 1
4 | 0
2 |0
1 | 0

-------------------------------------------------------------------------

> - **1001 0010**
>> 146

> - **0111 0111**
>> 119

> - **11111111**
>> 255

> - **1100 0101**
>> 197

> - **1111 0110**
>> 246

> - **0001 0011**
>> 19

> - **1000 0001**
>> 129

> - **0011 0001**
>> 49

> - **0111 1000**
>> 120

> - **1111 0000**
>> 240

> - **0011 1011**
>> 59

> - **0000 0111**
>> 7

------------------------------------------------------------------------
------------------------------------------------------------------------

## Decimal to Binary

> - **238**
>> 11101110

> - **34**
>> 00100010

> - **123**
>> 01111011

> - **50**
>> 00110010

> - **255**
>> 11111111

> - **200**
>> 11001000

> - **10**
>> 00001010

> - **138**
>> 10001010

> - **1**
>> 00000001

> - **13**
>> 00001101

> - **250**
>> 11111010

> - **114**
>> 01110010

------------------------------------------------------------------------
------------------------------------------------------------------------

## Address Class Identification

> - **10.240.1.1**
>> A

> - **150.10.15.0**
>> B

> - **192.14.2.0**
>> C

> - **148.17.9.1**
>> B

> - **193.42.1.1**
>> C

> - **126.8.156.0**
>> A

> - **220.200.23.1**
>> C

> - **230.230.45.58**
>> D

> - **177.100.18.4**
>> B

> - **119.18.45.0**
>> A

> - **117.89.56.45**
>> A

> - **215.45.45.0**
>> C