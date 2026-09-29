import streamlit as st

from blood_db import bloodbank
st.title('UPDATE')
id=st.number_input('Donor ID',min_value=0)
n=st.text_input('Name of Donor')
bg=st.text_input('Blood Group')
p=st.text_input('Phone Number')
c=st.text_input('City')
ld=st.date_input('Last Donation')
btn=st.button('UPDATE')
if btn:
    b=bloodbank()
    a=b.update(n,bg,p,c,ld)
    if a:
        st.success('Updated Successfully')
    else:
        st.error('No Record')