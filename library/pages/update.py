import streamlit as st

from library_db import BookListCreateRetrieveUpdateDelete
st.title('UPDATE')
id=st.number_input('ID',min_value=0)
title=st.text_input('Title')
author=st.text_input('Author')
price=st.number_input('Price',min_value=0)
language=st.selectbox('Language',['Malayalam','English','Hindi'])
pages=st.number_input('Pages',min_value=0)
btn=st.button('update')
if btn:
    b=BookListCreateRetrieveUpdateDelete()
    a=b.update(id, title, author, price, language, pages)
    if a:
        st.success('Record updated')
    else:
        st.error('No record')
