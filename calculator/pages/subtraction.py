

import streamlit as st

st.title('Subtraction')

num1=st.number_input('number 1',min_value=0)
num2=st.number_input('number 2',min_value=0)

btn=st.button('sub')
if btn:
    st.write('difference is',num1-num2)