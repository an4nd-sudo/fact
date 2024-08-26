import streamlit as st

st.header('factorial')

x=st.number_input('enter a number',value=0,min_value=0)

btn=st.button('cal fact')

if btn:
  result=1
  fact=1
  i=1
  while i<=x:
    result=result*i
    i=i+1
  st.subheader(result)


