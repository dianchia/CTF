# SCRIPTING

## [EASY] BASE64

This file has been base64 encoded 50 times - write a script to retrieve the flag.

Just use for loop to decode it. Code shown in [b64.py](b64.py)

## [MEDIUM] GOTTA CATCH EM ALL

Using the socket library of python.
Connect to the host on the specific port. Send a GET request then wait for response. Then extract the information needed from the response.

Code shown in [catch_em_all.py](catch_em_all.py)

## ENCRYPTED SERVER CHIT-CHAT

> Python 2 is used in this [script](enc_server.py)

This challenge is slightly more complicated.

First we define a few method, AES_GCM_decrypt for decrypting the key
and SHA256_hash for hashing the plaintext.

Then we create a UDP socket
```python
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
```

Notice the `socket.SOCK_DGRAM` is used to create a UDP socket.

Then we send payload consisting 'hello' to the server to get the next move.

Everything is sent in byte therefore the 'b' prefix is used.

After that we send a 'ready' and carve out the checksum from the response. We then encode it to hex.

Then we send two payload with 'final' to get the flag and the tag. After we got everything we just put in the key, iv, ciphertext and tag into the decrypt function we defined before. Then we hash the plaintext to see whether it matches the checksum we got before.

Once we got the correct plaintext, we just print it out.

Code shown in [enc_server.py](enc_server.py)