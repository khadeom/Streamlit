import streamlit as st
import qrcode
import cv2


img=qrcode.make("Hey m aditi")
img.save("adie.jpg")


st.title("App by aditi")

st.write(""" 
	#demo QRcode scanner and decoder\n
	QRcode is below 
	""")

st.image('adie.jpg', channels="BGR")


a=cv2.QRCodeDetector()
val,points,straight_qrcode=a.detectAndDecode(cv2.imread("adie.jpg"))
#print(val)
st.write("Decoded text from QRcode :",val)
