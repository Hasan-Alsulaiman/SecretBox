import os
import pickle
import keygen
import aes
d = input("do you want to generate new private/public keys?<y>/<n>\n")
if (d=='y'):
    keygen.gen("user1")
else:
    o = input("pick operation\n [1]encrypt\n [2]decrypt")
    
    # for encryption
    if(o=='1'):
        p = input("pick a password: ")
        msg = input("enter a message: ")
        encmsg,iv = aes.enc(msg,p)
        print(encmsg)


