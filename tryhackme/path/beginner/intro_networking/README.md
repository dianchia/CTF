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
>> Provides networking options to programs. Works almost exclusively with
>> applications, providing interface for transmitting data. Data passed
>> down to presentation layer
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
> - **Layer 5 -- Transport**
>> Servers numerous important functions.
>>
>> 1. Choose protocol over which the data is to be transmitted.
>>     1. TCP -- Transmission Control Protocol
>>     1. UDP -- User Datagram Protocol