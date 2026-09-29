import streamlit as st

from library_db import BookListCreateRetrieveUpdateDelete

st.title('Welcome to LIBRARY App')

b=BookListCreateRetrieveUpdateDelete()

tab1,tab2,tab3,tab4,tab5=st.tabs(['ADD','READ','RETRIEVE','UPDATE','DELETE'])

with tab1:
    st.title('Add New Record ')

    title = st.text_input('Title')
    author = st.text_input('Author')
    price = st.number_input('Price', min_value=0)
    language = st.selectbox('Language', ['Malayalam', 'English', 'Hindi'])
    pages = st.number_input('Pages', min_value=0)
    btn = st.button('Add')
    if btn:
        b.create(title, author, price, language, pages)
        st.success('Record created successfully')

with tab2:
    st.title('READ')

    btn = st.button('print')
    if btn:
        a = b.list()
        if a:
            st.table(a)
        else:
            st.info('no record')

with tab3:
    st.title('RETRIEVE')
    a = st.number_input('Book ID', min_value=0)
    btn = st.button('Retrieve')
    if btn:
        r = b.retrieve(a)
        if r:
            st.write('Title: ', r[1])
            st.write('Author: ', r[2])
            st.write('Price: ', r[3])
            st.write('Language; ', r[4])
            st.write('Pages: ', r[5])
        else:
            st.error('no record')

with tab4:
    st.title('UPDATE')
    id = st.number_input('ID', min_value=0)
    title = st.text_input('Title')
    author = st.text_input('Author')
    price = st.number_input('Price', min_value=0)
    language = st.selectbox('Language', ['Malayalam', 'English', 'Hindi'])
    pages = st.number_input('Pages', min_value=0)
    btn = st.button('update')
    if btn:
        a = b.update(id, title, author, price, language, pages)
        if a:
            st.success('Record updated')
        else:
            st.error('No record')

with tab5:
    st.title('DELETE')
    a = st.number_input('Enter id', min_value=0)
    btn = st.button('Delete')
    if btn:
        d = b.delete(a)
        if d:
            st.success('Record Deleted')
        else:
            st.error('No Record found')