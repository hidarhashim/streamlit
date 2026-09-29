import streamlit as st

from library_db import BookListCreateRetrieveUpdateDelete

st.title('Add New Record ')

title=st.text_input('Title')
author=st.text_input('Author')
price=st.number_input('Price',min_value=0)
language=st.selectbox('Language',['Malayalam','English','Hindi'])
pages=st.number_input('Pages',min_value=0)
btn=st.button('Add')
if btn:
  b=BookListCreateRetrieveUpdateDelete()
  b.create(title,author,price,language,pages)
  st.success('Record created successfully')