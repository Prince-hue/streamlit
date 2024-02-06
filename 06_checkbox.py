import streamlit as st
from datetime import time, datetime

#checkbox
agree = st.checkbox("I agree")

if agree:
    st.write("Great !!!") 
    
#radio buttons
radio = st.radio(
    "You can only choose an option",
    ('Prince', 'Atsrim', 'Adanuti')
    )

if radio == 'Atsrim':
    st.write('You choose your surname')
else:
    st.write('You did not select your surname')
    
#select box
option = st.selectbox(
    'How would you like to be contacted?',
    ('----', 'Email', 'Home Phone', 'Mobile Phone')
)
st.write('You selcted:', option)

#slider
age = st.slider(
    'How old are you?',
    0, 130, 25
)
st.write('I am', age, 'year old.')

values = st.slider(
'Select a range of value',
0.0, 100.0, (25.0, 75.0)
)
st.write('Values:', values)

appointment = st.slider(
    'Schedule your appointment:',
    value = (time(11,30), time(12,45))
)
st.write("You're scheduled for:", appointment)

start_time = st.slider(
    "when do you start?",
    value = datetime(2024,2,6,9,30),
    format="MM/DD/YY - hh:mm"
)
st.write('Start time:', start_time)