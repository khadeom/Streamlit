import streamlit as st
import qrcode
import cv2

st.set_page_config(layout="wide")

st.markdown("""
<style>
.big-font {
    font-size:20px !important;
}
</style>
""", unsafe_allow_html=True)


st.title("App by aditi")

st.markdown('<p class="big-font">Demo qrcode generator and Scanner</p>'
	, unsafe_allow_html=True)

# st.markdown('<p class="big-font">Enter text</p>'
# 	, unsafe_allow_html=True)

user_input = st.text_input('Enter text',"Enter text here")

st.write("QRcode for entered text")
but=True
if st.button('View') and but==True:

	img=qrcode.make(user_input)
	img.save("adie.jpg")




	st.image('adie.jpg', channels="BGR")


	a=cv2.QRCodeDetector()
	val,points,straight_qrcode=a.detectAndDecode(cv2.imread("adie.jpg"))
	#print(val)
	st.write("Decoded text from QRcode :",val)

if st.button("Close"):
	but=False

# st.markdown('<p class="big-font">Hello World !!</p>'
# 	, unsafe_allow_html=True)
