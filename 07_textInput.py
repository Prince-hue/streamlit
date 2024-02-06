import streamlit as st
import datetime

#text Input
title = st.text_input('Movie Title', 'Life of Brain')
st.write("The current movie title is", title)

#number input
num = st.number_input('Enter number')
st.write('The number you entered is:', num)

#date input
d = st.date_input(
    'When is your birthday?',
    datetime.date(2000, 7, 6)
)
st.write("your birthday is:", d)