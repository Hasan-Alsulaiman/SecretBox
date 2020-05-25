import pyqrcode
import png
from pyqrcode import QRCode


# takes payload and name and returns qr code of that payload using that name


def gen(payload, name,path):
    if(type(payload)!= type("string")):
        payload = str(payload)
    # Generate QR code
    try:
        url = pyqrcode.create(payload)
        # Create and save the png file naming "myqr.png"
        finalpath = path + name+'.png'
        url.png(file = finalpath, scale=6)
    except:
        print("failed to generate qr image for", name)
        pass

