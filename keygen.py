from cryptography.hazmat.backends import default_backend  
from cryptography.hazmat.primitives.asymmetric import rsa  
from cryptography.hazmat.primitives import serialization  
  
def gen(name):
        
    
    # Generate an RSA Keys  
    private_key = rsa.generate_private_key(  
            public_exponent=65537,  
            key_size=2048,  
            backend=default_backend()  
        )  
    
    public_key = private_key.public_key()  
    
    # Save the RSA key in PEM format  
    with open(name+"PrivateKey.pem", "wb") as f:  
        f.write(private_key.private_bytes(  
            encoding=serialization.Encoding.PEM,  
            format=serialization.PrivateFormat.TraditionalOpenSSL,  
            encryption_algorithm=serialization.NoEncryption(),  
        )  
        )  
    
    # Save the Public key in PEM format  
    with open(name+"PublicKey.pem", "wb") as f:  
        f.write(public_key.public_bytes(  
            encoding=serialization.Encoding.PEM,  
            format=serialization.PublicFormat.SubjectPublicKeyInfo,  
        )  
    )