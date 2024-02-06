from PIL import Image
import streamlit as st

image = Image.open('static\\flower.jpg')
st.image(image, caption = 'Nice Picture')