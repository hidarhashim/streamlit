#addition

import streamlit as st

st.title('Addition')

num1=st.number_input('number 1',min_value=0)
num2=st.number_input('number 2',min_value=0)

btn=st.button('Add')
if btn:
    st.write('sum is',num1+num2)