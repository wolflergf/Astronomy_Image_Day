import streamlit as st
from get_image import get_image

title, explanation, url = get_image()

st.title(title)
st.image(url)
st.write(explanation)   

