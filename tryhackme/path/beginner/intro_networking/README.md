# INTRODUCTORY NETWORKING

## NOTES

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
