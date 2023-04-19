#!pip install streamlit -q
#import streamlit
Print ('Find the Largest number')

import streamlit as st


a= st.number_input('Enter number 1')
b= st.number_input('Enter number 2')
c= st.number_input('Enter number 3')

largest = 0

if a > b and a > c:
    largest = a
if b > a and b > c:
    largest = b
if c > a and c > b:
   largest = c
   
#st.button("Largest")   
#st.write('The current number is ', largest)
if st.button('Largest'):
    st.write('The Largest number is', largest)

