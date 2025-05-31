
import pyqrcode
import os

from PIL import Image
link = input("Enter the link: ")
qr_code = pyqrcode.create(link)
qr_code.png("qr_code.png", scale=6)
img = Image.open("qr_code.png")
os.startfile("qr_code.png")
