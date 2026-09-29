import streamlit as st

from library_db import BookListCreateRetrieveUpdateDelete

st.title('RETRIEVE')
a=st.number_input('Book ID',min_value=0)
btn=st.button('Retrieve')
if btn:

    b=BookListCreateRetrieveUpdateDelete()
    r=b.retrieve(a)
    if r:
        st.write('Title: ',r[1])
        st.write('Author: ', r[2])
        st.write('Price: ', r[3])
        st.write('Language; ', r[4])
        st.write('Pages: ', r[5])
    else:
        st.error('no record')