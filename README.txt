Different types of text elements
----------------------------------------
import streamlit as st
st.title("I am a title")
st.header("I am a header")
st.subheader("I am a subheader")
st.markdown("I am a markdown")
st.code("I am a code block. Eg - int a = 5")
st.text("I am Text")
st.write("I am a write")

Run streamlit server 
--------------------------------------
streamlit run textelement.py

Working with DataFrames
-------------------------------------------

In table form, you cannot filter or sort the
data unlike in st.DataFrames(df)

Working with json
--------------------------------------
import steamlit as st
st.json(
    {
        'abc': '1',
        'xyz': '2',
        'qwe': 'Key'
    }
)
