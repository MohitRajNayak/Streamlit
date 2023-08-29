import streamlit as st

st.title("WIDGETS")

st.subheader("Button Widgets")
st.text("use **st.button** to create a Button")
if st.button("Button"):
    st.write("uesd a **if statment**, if the button was pressed then the **if condition** is true and excecute the **st.write()**")

st.subheader("Input Text Widgets")
n = st.text_input("used **st.text_input** to input a text here")
st.write(n)

st.subheader("Text Area Widgets")
a = st.text_area("used **st.text_area** to input a long text here")
st.write(a)

st.subheader(" Date Input Widgets")
d = st.date_input("used **st.date_input** to input a  date here")
st.write(d)

st.subheader("Time Input Widgets")
t = st.time_input("used **st.time_input** to input a time here")
st.write(t)

st.subheader("Checkbox Widget")
if st.checkbox("checkbox",value=False):
    st.write("use **st.checkbox** to input a checkbox")

st.subheader("Radio Widget")
radio = st.radio(
    "use **st.radio** to input radio button",
    ['radio1','radio2'],
    captions=['cap_radio1','cap_radio2']
    )
if radio == 'radio1':
    st.write('you selected *radio1*')
else:
    st.write('you selected *radio2*')


st.subheader("Selection Box Widget")
option = st.selectbox(
    "use **st.selectbox** to input radio button",
    ('option1','option2')
    )
if option == 'option1':
    st.write('you selected *option1*')
else:
    st.write('you selected *option2*')


st.subheader("Multi-Select Box Widget")
mul = st.multiselect(
    "use **st.multiselect** to input radio button",
    ('option1','option2','option3','option4')
    )
if 'option1' in mul:
    st.write('you have *selected 1*')
if 'option2' in mul:
    st.write('you have *selected 2*')
if 'option3' in mul:
    st.write('you have *selected 3*')
if 'option4' in mul:
    st.write('you have *selected 4*')

st.subheader("Slider Widget")
num = st.slider("your project count",0,10,0)
st.write('My Project count is: ',num)

st.subheader("Number Input")
num2 = st.number_input('used **st.number_input** to get number value but we have to use float number for start,end,defult value and step',0.0,20.0,2.0,step=2.0)
st.write("the output is", num2)

st.subheader("Upload File Widget")
file = st.file_uploader('use **st.file_uploader** to upload any type of file *for this i am using an image*')
st.image(file)