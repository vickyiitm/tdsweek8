!pip install streamlit -q
#import streamlit
import streamlit as st

a= st.number_input()
b= st.number_input()
c= st.number_input()

largest = 0

if a > b and a > c:
    largest = a
if b > a and b > c:
    largest = b
if c > a and c > b:
   largest = c
   
st.button("largest")   
