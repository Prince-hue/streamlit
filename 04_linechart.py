import pandas as pd
import numpy as np
import streamlit as st
import matplotlib.pyplot as plt

chart_data = pd.DataFrame(
    np.random.rand(20, 3),
    columns = ['A', 'B', 'C']
)
st.line_chart(chart_data)
st.area_chart(chart_data)
st.bar_chart(chart_data)

data =  np.random.normal(1,1,size=100)
fig, ax = plt.subplots()
ax.hist(data, bins=20)
st.pyplot(fig)