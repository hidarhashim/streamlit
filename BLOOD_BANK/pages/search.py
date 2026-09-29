import streamlit as st

from blood_db import bloodbank
st.title('SEARCH')
id=st.number_input('Enter Donor ID',min_value=0)
btn=st.button('Print')
if btn:
    b=bloodbank()
    a=b.retrieve(id)
    if a:
        st.write('Name: ',a[1])
        st.write('Blood Group: ',a[2])
        st.write('Phone number: ', a[3])
        st.write('City: ', a[4])
        st.write('Last Donation: ', a[5])
    else:
        st.error('No record found')