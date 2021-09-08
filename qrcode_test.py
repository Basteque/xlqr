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
  
# taking image which user wants 
# in the QR code center
Logo_link = 'youtube-new-logo3NB.jpg'
  
logo = Image.open(Logo_link)
  
# taking base width
basewidth = 195
  
# adjust image size
wpercent = (basewidth/float(logo.size[0]))
hsize = int((float(logo.size[1])*float(wpercent)))
logo = logo.resize((basewidth, hsize), Image.ANTIALIAS)
QRcode = qrcode.QRCode(
        error_correction=qrcode.constants.ERROR_CORRECT_H)
  
# taking url or text
url = 'https://bit.ly/AbouKouyateAssyYT'
  
# addingg URL or text to QRcode
QRcode.add_data(url)
  
# generating QR code
QRcode.make()
  
# taking color name from user
QRcolor = 'Black'
  
# adding color to QR code
# QRimg = QRcode.make_image(
    # fill_color=QRcolor, back_color="white").convert('RGB')
    
QRimg = QRcode.make_image(image_factory=StyledPilImage, module_drawer=GappedSquareModuleDrawer())
  
# set size of QR code
pos = ((QRimg.size[0] - logo.size[0]) // 2,
       (QRimg.size[1] - logo.size[1]) // 2)
QRimg.paste(logo, pos)
  
# save the QR code generated
QRimg.save('qrCodes/gfg_QR3.png')
  
print('QR code generated!')
# QRimg.show()