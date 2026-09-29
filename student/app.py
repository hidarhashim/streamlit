import streamlit as st
from datetime import date
st.title('Student Registration Form')
name=st.text_input('Name')
age=st.number_input('Age',min_value=0)
DOB=st.date_input('DOB',max_value=date.today(),min_value=date(1900,1,1))
email=st.text_input('Email')
gender=st.radio('gender',['male','female'])
courses=st.selectbox('Courses',['Python','Dotnet','Testing'])
btn=st.button('submit')
if btn:
    st.write('Name',name)
    st.write('Age',age)
    st.write('DOB',DOB)
    st.write('Email',email)
    st.write('Gender',gender)
    st.write('Courses',courses)

