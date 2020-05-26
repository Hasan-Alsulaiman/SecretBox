import os.path
from os import path
import pickle
import keygen
import aes
import keysharing
import qr
print("-------------Main Menu-------------")
name = "user1"
peername = "user2"
print("Warning: make sure that 'peer_publickey' is always up to date!")
while True:
    o = input("pick operation\n [1]Encrypt\n [2]Decrypt\n [3]Generate new key pair\n or press 'q' to quit\n")

    # for encryption
    if(o == '1'):
        # check if an icome msg exists or if peerpublic key exists
        encryptedmsgpath = "./inbox/"+peername+"_msg.txt"
        encryptedmsgexits = os.path.isfile(encryptedmsgpath)
        peerpublickeypath = "./peer_publickey/"+peername+"PublicKey.pem"
        peerpublickeyexits = os.path.isfile(peerpublickeypath)
        if(peerpublickeyexits or encryptedmsgexits):
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
            print("________________________")
            print("incoming msg = ",decryptedmsg)
            print("symmetric password = ", password_dec)
            print("________________________")
            con = input("to go back to the main menue hit 'b'")
            if(con == 'b'):
                continue
            
        else:
            print("cant find the msg")
    # generating new key pair
    if(o=='3'):
        d = input("are you sure you want new key pair?<y>/<n>\n")

        if (d == 'y'):
            print("generating new key pair...")
            keygen.gen(name)
            qrimgg = input("new keys generated successfuly, generate QR image?<y>/<n>")
            if(qrimgg == 'y'):
                with open("./outbox/"+name+"PublicKey.pem", "r") as f:
                    mypubkey = f.read()
                qr.gen(mypubkey,name+"publickey","./outbox/")
    if(o=='q'):
        break