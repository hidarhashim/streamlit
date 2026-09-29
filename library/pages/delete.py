


import streamlit as st
import library_db import BookListCreateRetrieveUpdateDelete
st.title('DELETE')
a=st.number_input('Enter id',min_value=0)
btn=st.button('Delete')
if btn:
    b=BookListCreateRetrieveUpdateDelete()
    d=b.delete(a)
    if d:
        st.success('Record Deleted')
    else:
        st.error('No Record found')