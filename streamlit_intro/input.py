import streamlit as st

#text_input()
#number_input()
#date_input()

#number
num1=st.number_input('enter number 1',min_value=0)
num2=st.number_input('enter number 2',min_value=0)
st.write(num1)
st.write(num2)

#text
name=st.text_input('enter name')
st.write(name)

#date
date=st.date_input('enter date')
st.write(date)

#########################

#Button
#button()
btn=st.button('click')
print(btn)

if btn:              #if button clicked
    st.write(num1)
    st.write(num2)
    st.write(name)
    st.write(date)
