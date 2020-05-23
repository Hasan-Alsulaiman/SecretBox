import os.path
from os import path
import pickle
import keygen
import aes
import keysharing

name = "user1"
peername = "user2"
d = input("do you want to generate new private/public keys?<y>/<n>\n")
if (d == 'y'):
    keygen.gen(name)
else:
    o = input("pick operation\n [1]encrypt\n [2]decrypt\n")

    # for encryption
    if(o == '1'):
        peerpublickeypath = "./peer_publickey/"+peername+"PublicKey.pem"
        peerpublickeyexits = os.path.isfile(peerpublickeypath)
        if(peerpublickeyexits):
            p = input("pick a password: ")
            msg = input("enter a message: ")
            encmsg, iv = aes.enc(msg, p)
            print(encmsg)

        # key sharing
            print("peer's public key was found, exchanging password..")
            encryptedpassword = keysharing.enc(peerpublickeypath, p)
            print(encryptedpassword)
            with open(name+"PublicKey.pem", "r") as f:
                mypubkey = f.read()
            keyinfo = {"password": encryptedpassword, "iv": iv,
                       name+"publickey": mypubkey, "encmsg": encmsg}
            # we save the encrypted msg and key info to file
            with open(name+'_msg.txt', 'wb+')as f:
                f.write(pickle.dumps(keyinfo))
            print("msg encrypted and saved.")
        else:
            print("can find peer's public key file, please add it to directory")
