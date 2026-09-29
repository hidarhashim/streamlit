import streamlit as st

from blood_db import bloodbank


st.title('Add New Donor')
n=st.text_input('Name of Donor')
bg=st.text_input('Blood Group')
p=st.text_input('Phone Number')
c=st.text_input('City')
ld=st.date_input('Last Donation')

btn=st.button('Add')
if btn:
    b=bloodbank()
    a=b.create(n,bg,p,c,ld)
    st.success('New donor added successfully')