# INTRODUCTORY NETWORKING

## THE OSI MODEL: AN OVERVIEW

**OSI** | 
---------| 
Application | 
Presentation |
Session |
Transport |
Network |
Data Link |
Physical |


> - **Layer 7 -- Application**
>> Provides networking options to programs. Works almost exclusively
>> with applications, providing interface for transmitting data. Data
>> passed down to presentation layer
>
> - **Layer 6 -- Presentation**
>> Receives data from application layer. Data tends to be in format 
>> where app understand but not standardised format that can be
>> understand by the application layer of the *receiving computer*.
>> This layer translate the data to standardised format, handling any
>> encryption, compression or other transformation. Passed down to
>> sesion when complete.
>
> - **Layer 5 -- Session**
>> Try to set up a connection with other computer across the network.
>>
>> Send back error if can't.
>>
>> If a session *can* be established then this layer will maintain it,
>> as well as co-operate with the session layer of the *remote computer*
>> in order to synchronise communications. Session created is **unique**
>> to the communication in question. Allows for multiple requests to
>> different endpoints without data being mixed up.
>
> - **Layer 4 -- Transport**
>> Servers numerous important functions.
>>
>> 1. Choose protocol over which the data is to be transmitted.
>>     1. TCP -- Transmission Control Protocol
>>     1. UDP -- User Datagram Protocol
>>
>> **TCP**
>>> *Connection based*: Connection between computers is established
>>> and maintained for the duration of the request. Allows for 
>>> reliable transmission, ensure data is sent at an acceptable
>>> speed and lost data is re-sent. Would be chosen if accuracy
>>> is favoured over speed. (e.g. file transfer or loading web page)
>>
>> **UDP**
>>> *Session based*: Packets of data is thrown at the receiving computer
>>> and if it can't keep up then that's its problem. Would be chosen
>>> if speed is favoured over accuracy. (e.g. video streaming)
>>
>> 2. Divides the transmission into bite-sized pieces for easier
>> transmission
>>
>> **TCP** : Segments
>>
>> **UDP** : datagrams
>>
> - **Layer 3 -- Network**
>> Responsible for locating the destination of the request. Takes IP
>> address and figure out best route to take. Most common form of
>> logical addressing (IP addresses) is IPV4 format.
>>
> - **Layer 2 -- Data Link**
>> Focus on physical addressing of the transmission. Receives packets
>> from network layer (includes IP address for the remote computer) and
>> adds in the physical (MAC) address of the receiving endpoint. Every
>> network enabled computer has a Network Interface Card (NIC) which
>> comes with a unique Media Access Control (MAC) address to identify it.
>>
>> MAC addresses are set by manufacturer and literally burnt into the
>> card; they can't be changed -- although they can be spoofed.
>>
>> This layer also present the data in a format suitable for 
>> transmission.
>>
>> This layer also checks the received information to make sure it hasn's
>> been corrupted during transmission, which could well happen on 
>> layer 1.
>>
> - **Layer 1 -- Physical**
>> Right down to the hardware of the computer. Electrical pulses makes up
>> data transfer over a network are sent and received. Converts binary
>> data of transmission into signals and transmit them accross the
>> network, as well as receiving incoming signals and converting back to
>> binary data.

------------------------------------------------------------------------

> - **Which layer would choose to send data over TCP or UDP?**
>> 4
>>
> - **Which layer checks received packets to make sure that they haven't been corrupted?**
>> 2
>>
> - **In which layer would data be formatted in preparation for transmission?**
>> 2
>>
> - **Which layer transmits and receives data?**
>> 1
>>
> - **Which layer encrypts, compresses, or otherwise transforms the initial data to give it a standardised format?**
>> 6
>>
> - **Which layer tracks communications between the host and receiving computers?**
>> 5
>>
> - **Which layer accepts communication requests from applications?**
>> 7
> - **Which layer handles logical addressing?**
>> 3
> - **When sending data over TCP, what would you call the "bite-sized" pieces of data?**
>> Segments
>>
> - **[Research] Which layer would the FTP protocol communicate with?**
>> 7
>>
> - **Which transport layer protocol would be best suited to transmit a live video?**
>> UDP

------------------------------------------------------------------------
------------------------------------------------------------------------

## ENCAPSULATION

![Process Steps](image.jpeg)

> Encapsulated data is given a different name at different steps of the
> process.
> 
>> - Layers 7, 6, 5 	: data.
>>
>> - Transport Layer 	: segment or datagram.
>>
>> - Network Layer 		: packet
>>
>> - Data Link Layer 	: frame
>>
>> - Physical layer 	: bits  

------------------------------------------------------------------------

> - **How would you refer to data at layer 2 of the encapsulation process (with the OSI model)?**
>> Frames
>>
> - **How would you refer to data at layer 4 of the encapsulation process (with the OSI model), if the UDP protocol has been selected?**
>> Datagram
>>
> - **What process would a computer perform on a received message?**
>> De-encapsulation
>>
> - **Which is the only layer of the OSI model to add a trailer during encapsulation?**
>> Data Link
>>
> - **Does encapsulation provide an extra layer of security (Aye/Nay)?**
>> Aye

------------------------------------------------------------------------
------------------------------------------------------------------------

## THE TCP/IP MODEL

> Very similiar to OSI Model. A few year older and serves as the basis
> for real-world networking.
>
> Four layers: Application, Transport, Internet and Network Interface.
> 
>Cover the same range of functions as the seven layers of OSI Model.

**OSI** | **TCP/IP**
--------|-----------
Application | Application
Presentation | Application
Session | Application
Transport | Transport
Network | Internet
Data Link | Network Interface
Physical | Network Interface

> Three-way handshake must be carried out before a connection can be
> established using TCP.
> 1. Special request sent to remote server containing SYN (synchronise)
> bit.
>
> 2. Remote server respond with packet containing SYN bit and ACK
> (acknowledge) bit.
>
> 3. Send packet containing ACK bit, confirming the connection.

------------------------------------------------------------------------

> - **Which model was introduced first, OSI or TCP/IP?**
>> TCP/IP
>>
> - **Which layer of the TCP/IP model covers the functionality of the Transport layer of the OSI model (Full Name)?**
>> Transport
>>
> - **Which layer of the TCP/IP model covers the functionality of the Session layer of the OSI model (Full Name)?**
>> Application
>>
> - **The Network Interface layer of the TCP/IP model covers the functionality of two layers in the OSI model. These layers are Data Link, and?.. (Full Name)?**
>> Physical
>>
> - **Which layer of the TCP/IP model handles the functionality of the OSI network layer?**
>> Internet
>>
> - **What kind of protocol is TCP?**
>> Connection-based
>>
> - **What is SYN short for?**
>> Synchronise
>>
> - **What is the second step of the three way handshake?**
>> SYN/ACK
>>
> - **What is the short name for the "Acknowledgement" segment in the three-way handshake?**
>> ACK

------------------------------------------------------------------------
------------------------------------------------------------------------

## WIRESHARK

> - **Frame 1**
>> Showing details from the pysical layer
>>
> - **Ethernet II**
>> Showing details from the Data Link layer
>>
> - **Internet Protocol Version 4**
>> Showing details from the Network layer
>>
> - **Transmission Control Protocol**
>> Showing details from the Transport layer
>>
> - **Hypertext Transfer Protocol**
>> Showing details from the Application layer

------------------------------------------------------------------------

> - **What is the protocol specified in the section of the request that's linked to the Application layer of the OSI and TCP/IP Models?**
>> Domain Name System
>>
> - **Which layer of the OSI model does the section that shows the IP address "172.16.16.77" link to (Name of the layer)?**
>> Network
>>
> - **In the section of the request that links to the Transport layer of the OSI and TCP/IP models, which protocol is specified?**
>> User Datagram Protocol
>>
> - **Over what medium has this request been made (linked to the Data Link layer of the OSI model)?**
>> Ethernet II
>>
> - **Which layer of the OSI model does the section that shows the number of bytes transferred (81) link to?**
>> Physical
>>
> - **[Research] Can you figure out what kind of address is shown in the layer linked to the Data Link layer of the OSI model?**
>> MAC

------------------------------------------------------------------------
------------------------------------------------------------------------

## NETWORKING TOOLS

### PING

> Can be used to determine the IP address as well
>
>Pretty much ubiquitous to any network enabled device.
```
ping <target>
```

------------------------------------------------------------------------

> - **What command would you use to ping the bbc.co.uk website?**
>> ping bbc.co.uk
>>
> - **Ping tryhackme.com
What is the IP address?**
>> 68.183.254.76
>>
> - **What switch lets you change the interval of sent ping requests?**
>> -i
>>
> - **What switch would allow you to restrict requests to IPV4?**
>> -4
>>
> - **What switch would give you a more verbose output?**
>> -v

------------------------------------------------------------------------
------------------------------------------------------------------------

### Traceroute

> Allows us to see every intemediate step between host computer and
> remote computer.
```
traceroute <destination>
```

------------------------------------------------------------------------

> - **What switch would you use to specify an interface when using Traceroute?**
>> -i
>>
> - **What switch would you use if you wanted to use TCP requests when tracing the route?**
>> -t
>>
> - **[Lateral Thinking] Which layer of the TCP/IP model will traceroute run on by default?**
>> Internet

------------------------------------------------------------------------
------------------------------------------------------------------------

### WHOIS

> Query who a domain name is registered to.
```
whois <domain>
```
>
> Personal details are redacted in Europe but elsewhere great deal
> of information can potentially be leaked.

------------------------------------------------------------------------

> - **What is the registrant postal code for facebook.com?**
>> 94025
>>
> - **When was the facebook.com domain first registered?**
>> 29/03/1997
>>
> - **Which city is the registrant based in?**
>> Redmond
>>
> - **[OSINT] What is the name of the golf course that is near the registrant address for microsoft.com?**
>> Bellevue golf course
>>
> - **What is the registered Tech Email for microsoft.com?**
>> msnhst@microsoft.com

------------------------------------------------------------------------
------------------------------------------------------------------------

### DIG

> Manually query recursive DNS servers of your choice for info

```
dig <domain> @<dns-server-ip>
```

------------------------------------------------------------------------

> - **What is DNS short for?**
>> Domain Name System
>>
> - **What is the first type of DNS server your computer would query when you search for a domain?**
>> Recursive
>>
> - **What type of DNS server contains records specific to domain extensions (i.e. .com, .co.uk, etc)? Use the long version of the name.**
>> Top-Level Domain
>>
> - **Where is the very first place your computer would look to find the IP address of a domain?**
>> Local cache
>>
> - **[Research] Google runs two public DNS servers. One of them can be queried with the IP 8.8.8.8, what is the IP address of the other one?**
>> 8.8.4.4
>>
> - **If a DNS query has a TTL of 24 hours, what number would the dig query show?**
>> 86400