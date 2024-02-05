import streamlit as st
import pandas as pd

if st.button('Say Hello'):
    st.write('Hey Hello There!')
else:
    st.write('Goodbye')
    
text = "Some Texts that will be downloaded."
st.download_button('Download text', text)

with open("static\\flower.jpg", "rb") as file:
    btn = st.download_button(
        label= "Download Image",
        data = file,
        file_name = "flower.jpg",
        mime = "image/jpg"
    )
    
@st.cache_data

def convert_df(df):
    return df.to_csv().encode('utf-8')

df1 = pd.read_excel('static\\book1.xlsx')
csv = convert_df(df1)

st.download_button(
    label = "Download data as csv",
    data = csv,
    file_name = "large_df.csv",
    mime = "text/csv"
)
