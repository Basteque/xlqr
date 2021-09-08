# -*- coding: utf-8 -*-
"""
Created on Sun Sep  5 17:29:10 2021

@author: basil
"""

# import modules
import qrcode
from PIL import Image
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers import CircleModuleDrawer
from qrcode.image.styles.moduledrawers import GappedSquareModuleDrawer
  
# center image
Logo_link = 'youtube-new-logo3NB.jpg'
  
logo = Image.open(Logo_link)
  
# image width
basewidth = 190
  
# setting up overlay image + qrcode instance
wpercent = (basewidth/float(logo.size[0]))
hsize = int((float(logo.size[1])*float(wpercent)))+4
logo = logo.resize((basewidth, hsize), Image.ANTIALIAS)
QRcode = qrcode.QRCode(
        error_correction=qrcode.constants.ERROR_CORRECT_H)

def qr_generate(url,name,i):
    QRcode.clear()
      
    QRcode.add_data(url)
      
    # Generating qr code with the url
    QRcode.make()
    QRimg = QRcode.make_image(image_factory=StyledPilImage, module_drawer=GappedSquareModuleDrawer())
      
    # putting overlay image on QR code
    pos = ((QRimg.size[0] - logo.size[0]) // 2,
           (QRimg.size[1] - logo.size[1]) // 2)
    QRimg.paste(logo, pos)
      
    # saving the QR code generated
    # QRimg.save('qrCodes/{}.png'.format(name.replace(" ","_")))
    filename=name.replace(" ","_")
    QRimg.save('qrCodes/{}.png'.format(filename))
    print(filename)
      
    print('QR code number {} generated!'.format(i-1))
    return QRimg
    # QRimg.show()