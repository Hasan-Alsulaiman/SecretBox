# SecretBox

SecretBox is a Python app for encrypting/decrypting messages in a secure device that is kept away from the internet.

## Installation

after installing python on your machine, open a ```cmd``` and type:

```pip install -r requirements.txt```.

this will install all the required packages.

## Usage

start the application using the file named user1.py [or user2.py], you will be greeted with these choices:
```
pick operation
 [1]Encrypt
 [2]Decrypt
 [3]Generate new key pair
 or press 'q' to quit
```
but before you can start encrypting/decrypting you need to have public/private key pair, you can generate those using option 3.

### Encryption:
before encrypting a new msg, make sure you have the latest public key of the destination user, copy and paste that key into folder "peerpublickey"
now you can encrypt, the resulting msg will be saved in the folder "outbox",
you will be asked if you want to generate QR codes of your msg, these would also be saved in that folder if you chose "yes"

### Decryption:
to decrypt a msg, place that msg into the folder "inbox", the decryption result will be displayed on the command line.

### Generating new key pair
the public key will be stored in folder "outbox", the private key will be saved in the current directory, you must always share the public key but never share the private key.

## Notes:
the critical part is sharing the keys, this must be done manualy since our device is kept diconnected from the internet, you must always have the correct public key of the destination before encrypting the msg.

the QR images can be used to scan the public key and the encrypted msg, although I found that this works better with small size msg.

```

## HASAN ALSULAIMAN


## EMAIL:
hasan.alsulaimanaqa@agu.edu.tr
