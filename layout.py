import streamlit as st

st.title("Form")

fn,ln = st.columns(2)
with fn:
    st.text_input("First Name")
with ln:
    st.text_input("Last Name")

em,mo = st.columns([3,1]) # if you pass like this the col is divied into that ratio
with em:
    st.text_input("Enter your email id")
with mo:
    st.text_input("Phone Number")

un,pas,rpas = st.columns(3)
with un:
    st.text_input("Enter your User id")
with pas:
    st.text_input("Password",type='password')
with rpas:
    st.text_input("Conform Password",type='password') # type password help to put a eye icon in the text_input section so that user can hide or unhide his password

ch,bl,sub = st.columns(3)
with ch:
    st.checkbox("I Agree")
with sub:
    st.button("Submit")