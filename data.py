import pandas as pd
import numpy as np
import streamlit as st
import time

st.header(" Working on how to show data on the Streamlit! ")


a = [1,2,3,5,4,6,7,8]
n = np.array(a)
nd = n.reshape(2,4)

dic = {
    "trigger" : ["tiger","play"],
    "concept" : ["triger is running","boys are playing"],
    "gif" : ["tiger.gif","football.gif"]
}

df = pd.read_csv(r"data\pizza_sales.csv")

st.subheader("Showing DataFrame by importing data as csv")
st.dataframe(df)
st.subheader("Showing Data by importing data as dic")
st.dataframe(dic)
st.subheader("Showing Data by creatind data using np.array")
st.dataframe(nd)

df1 = pd.DataFrame(
   np.random.randn(10, 5),
   columns=('col %d' % i for i in range(5)))

st.subheader("Showing DataFram by creating data using pd.Dataframe but using st.table()")
st.table(df1)

st.subheader("Showing Data in Json fromat")
st.json(dic)

st.subheader("Showing Data using st.write fun")
col1,col2 = st.columns(2)
with col1:
    st.text("Showing Data by importing data as dic")
    st.write(dic)
with col2:
    st.text("Showing DataFram by creating data using pd.Dataframe")
    st.write(df1)

st.subheader("created a cache dacorater")
@st.cache_data
def ret_time(a):
    time.sleep(5)
    return time.time()

st.text("using st.checkbox created checkboxes")
if st.checkbox("first"):
    st.write(ret_time(1))

if st.checkbox("second"):
    st.write(ret_time(0.5))


