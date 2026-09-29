import streamlit as st

from blood_db import bloodbank
st.title('RECORDS')
btn=st.button("Print Record")
if btn:
    b=bloodbank()
    a=b.list()
    if a:
        st.table(a)
    else:
        st.error("No Record")