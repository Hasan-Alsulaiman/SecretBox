import os.path
from os import path
import pickle
import keygen
import aes
import keysharing
import qr

name = "user1"
peername = "user2"
d = input("do you want to generate new private/public keys?<y>/<n>\n")

if (d == 'y'):
    print("generating new key pair...")
    keygen.gen(name)


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
        print("peer's public key was found, encrypting the password with his public key..")
        encryptedpassword = keysharing.enc(peerpublickeypath, p)
        print(encryptedpassword)
        with open(name+"PublicKey.pem", "r") as f:
            mypubkey = f.read()
        keyinfo = {"password": encryptedpassword, "iv": iv,
                    name+"publickey": mypubkey, "encmsg": encmsg}
        # we save the encrypted msg and key info to file
        with open("./outbox/"+name+'_msg.txt', 'wb+')as f:
            f.write(pickle.dumps(keyinfo))
        qrimage = input("would you like to generate qr images? <y>/<n>")
        if(qrimage == 'y'):
            qr.gen([{"password":encryptedpassword,"iv":iv}],"password-info",'./outbox/')
            qr.gen(mypubkey,name+"publickey","./outbox/")
            qr.gen(encmsg,"encmsg",'./outbox/')
        print("msg encrypted and saved.")
    else:
        print("can find peer's public key file, please add it to directory")
# for decryption
if(o == '2'):
    # change name to peername for final application
    encryptedmsgpath = "./inbox/"+peername+"_msg.txt"
    encryptedmsgexits = os.path.isfile(encryptedmsgpath)
    if(encryptedmsgexits):
        # load encrypted msg
        with open("./inbox/"+peername+'_msg.txt', 'rb+')as f:
            encryptedmsg = pickle.loads(f.read())
        print("msg found.")
        print(encryptedmsg)
        password_dec = keysharing.dec(name+"PrivateKey.pem",b"hi",encryptedmsg['password'])
        iv_dec = encryptedmsg['iv']
        decryptedmsg = aes.dec(encryptedmsg['encmsg'],password_dec,iv_dec)
        print(decryptedmsg)
        
    else:
        print("cant find it")
