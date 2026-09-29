

import streamlit as st

st.title('Multiplication')

num1=st.number_input('number 1',min_value=0)
num2=st.number_input('number 2',min_value=0)

btn=st.button('mul')
if btn:
    st.write('product is',num1*num2)