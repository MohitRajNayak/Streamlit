import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import time
st.set_option('deprecation.showPyplotGlobalUse', False) # to disable warnings

plt.style.use("ggplot")

data = {
    "num":[x for x in range(1,11)],
    "square":[x**2 for x in range(1,11)],
    "twice":[x*2 for x in range(1,11)],
    "thrice":[x*3 for x in range(1,11)]
}

df = pd.DataFrame(data=data)

with st.sidebar:
    st.subheader("Select box in side bar")
    opi = st.selectbox(
        "Putting the select box on the side bar",
        ("option1","option2","option3")
    )

with st.sidebar:
    st.subheader("Filters")
    col =st.selectbox(
            "Select the col",
            df.columns
            )
    mcol = st.multiselect(
        "select multipule col",
        df.columns
    )
    rad = st.radio(
        "Navigation",
        ["Home","contact","Status"]
        )

if rad == "Home":
    st.header("Link to *sidebar*")
    st.subheader("From *SelectBox* in the sidebar")
    if opi == "option1":
        st.write("filter in sidebar but showing it in the main body **Opthin 1**")
    elif opi == "option2":
        st.write("filter in sidebar but showing it in the main body **Opthin 2**")
    else:
        st.write("filter in sidebar but showing it in the main body **Opthin 3**")
    st.subheader("Line Plot")
    plt.plot(df["num"],df[col])
    st.pyplot()
    st.subheader("Line Plot with multiselect")
    plt.plot(df["num"],df[mcol])
    st.pyplot()
if rad == "contact":
    n = st.text_input("Enter your Name")
    a = st.text_area("Enter your Address")
    ag = st.slider("Your age please",0,85,0)
    b = st.button("Submit")
    if b == True:
        st.write("Name: ",n)
        st.write("Address: ",a)
        st.write("Age: ",ag)
        st.toast('Submited Done', icon='😍')
if rad == "Status":
    st.header("Status Elements")
    st.text("Progress Bar")
    pro = st.progress(0)
    for i in range(100):
        time.sleep(0.1)
        pro.progress(i+1)
    st.snow()
    st.error("Error",icon="🚨")
    st.exception(RuntimeError("Run time error"))
    st.warning("warning",icon="⚠️")
    st.info("Info",icon="ℹ️")
    st.success("Success",icon="✅")


