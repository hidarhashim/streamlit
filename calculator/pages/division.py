

import streamlit as st

st.title('Division')

num1=st.number_input('number 1',min_value=0)
num2=st.number_input('number 2',min_value=0)

btn=st.button('Div')
if btn:
    st.write('quotient is',num1/num2)