import streamlit as st

from blood_db import bloodbank

st.title('DELETE')
id=st.number_input('Donor ID',min_value=0)
btn=st.button('Delete')
if btn:
    b=bloodbank()
    a=b.delete(id)
    if a:
        st.success('Record Deleted Successfully')
    else:
        st.error('No Record found')
