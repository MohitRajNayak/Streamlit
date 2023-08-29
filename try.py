import streamlit as st

st.title("Hi My First Streamlit")
st.header("Main Header")
st.subheader("Sub Header")
st.text("Description or Detailed Explanation Of The Sub Header")
st.markdown("""
# the "#" is same work as the markdown work in jupyter notebook
## the "##" is same work as the markdown work in jupyter notebook
### the "###" is same work as the markdown work in jupyter notebook
#### Add emoji as follow - 
:smile:
:rose:
#### add html tag as below -
HTML p Tag. HTML p tag is used to represents a paragraph text. <br>
The paragraph element acts as a container for the text between the start tag p and the end tag /p
Strong emphasis, aka bold, with **asterisks** or __underscores__.
Emphasis, aka italics, with *asterisks* or _underscores_.
""",True) # add true in the end to apply html tags 

st.subheader("to view mathmatical formula use st.latex")
st.latex(r'''
    a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
    \sum_{k=0}^{n-1} ar^k =
    a \left(\frac{1-r^{n}}{1-r}\right)
    ''')

st.write(st.write)

