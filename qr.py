import streamlit as st
import pyqrcode
from PIL import Image

st.title("QR Code Generator")

link = st.text_input("Enter a link : ")
if link:
    qr_code = pyqrcode.create(link)
    qr_code.png("qr_code.png", scale=6)
    
    img = Image.open("qr_code.png")
    st.image(img)
    st.success("QR Code generated succesfully")
else:
    st.error("please enter a valid link")
    