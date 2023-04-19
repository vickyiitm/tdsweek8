#!pip install streamlit -q

import streamlit as st

st.title("Find the largest number")
st.write(" Enter three numbers and click the below button to find the largest number")


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
   
if st.button('Find the Largest'):
    st.write('The Largest number is', largest)

