import streamlit as st
import qrcode
import cv2

st.title("App by aditi but does it work")

st.write(""" 
	#demo QRcode scanner and decoder
	""")

user_input = st.text_input("Enter text"
	, "Hey m aditi")

st.write("QRcode for entered text")
img=qrcode.make(user_input)
img.save("adie.jpg")




st.image('adie.jpg', channels="BGR")


a=cv2.QRCodeDetector()
val,points,straight_qrcode=a.detectAndDecode(cv2.imread("adie.jpg"))
#print(val)
st.write("Decoded text from QRcode :",val)
