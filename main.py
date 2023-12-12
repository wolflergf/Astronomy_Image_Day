# Import the streamlit library for creating web apps
import streamlit as st

# Import the get_image function from the get_image module
from get_image import get_image

# Call the get_image function and unpack its return values into title, explanation, and url
title, explanation, url = get_image()

# Use streamlit to create a title on the web page with the title from get_image
st.markdown("<h1 style='text-align: center'>{}</h1>".format(title), unsafe_allow_html=True)

# Use streamlit to display an image on the web page with the url from get_image
st.image(url)

# Use streamlit to write the explanation from get_image on the web page
st.write(explanation)