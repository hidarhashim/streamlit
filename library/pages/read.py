import streamlit as st
from library_db import BookListCreateRetrieveUpdateDelete
st.title('READ')

btn=st.button('print')
if btn:
  b=BookListCreateRetrieveUpdateDelete()
  a=b.list()
  if a:
    st.table(a)
  else:
    st.info('no record')