import streamlit as st
import pandas as pd

st.write(AVD2)
data = {
    'Course Name':['DevOps','Hadoop','PySpark'],
    'Duration':['30 days','20 days','30 days']
}

df = pd.DataFrame(data)

st.title('Course Information')
st.write(df)