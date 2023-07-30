import streamlit as st
import pandas as pd
import numpy as np

st.title("App title")

if st.sidebar.button('Say hello'):
    st.sidebar.write('Why hello there')

col1, col2, col3 = st.columns(3)

with col1:
   st.header("A cat")
   st.image("https://static.streamlit.io/examples/cat.jpg")

col1.header("A cat")

with col2:
   st.header("A dog")
   st.image("https://static.streamlit.io/examples/dog.jpg")

with col3:
   st.header("An owl")
   st.image("https://static.streamlit.io/examples/owl.jpg")
