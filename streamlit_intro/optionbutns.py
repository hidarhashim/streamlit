#radio button
import streamlit as st
g=st.radio('Gender',['male','female'])
st.write(g)

#checkbox
l=st.checkbox('python')
st.write(l)

#selectbox
s=st.selectbox('places',['Ernakulam','Thrissur','Trivandrum'])
st.write(s)