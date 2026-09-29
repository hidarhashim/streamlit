#bmi
#equation--  bmi=weight(kg)/(height(cm)/100)(m)**2)
# bmi<18.5 -- underweight
# 18.5<=bmi<25 --- normal
# 25<=bmi<30 ---overweight
# bmi>30 --- obesity

import streamlit as st

st.title('BMI Calculator')
weight=st.number_input('weight in kg')
height=st.number_input('height in cm')

btn=st.button('BMI')
if btn:
    bmi=weight/(height/100)**2
    st.write('BMI is',bmi)
    if bmi<18.5:
        st.info('underweight')
    elif 18.5<=bmi<25:
        st.success('normal')
    elif 25<=bmi<30:
        st.warning('overweight')
    else:
        st.error('obesity')

