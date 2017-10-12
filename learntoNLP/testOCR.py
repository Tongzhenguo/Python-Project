'''
测试的时候tesseract命令总是找不到，所以我直接把图片放到了tesseract的根目录下了

'''

import pytesseract
from PIL import Image

img = Image.open(r'1.png')
print (pytesseract.image_to_string(img,))
