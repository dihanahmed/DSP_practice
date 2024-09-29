# importing the function get_endpoint
from astros import get_endpoint
from astros import post_endpoint

import streamlit as st

st.title('My streamlit API explorer')

# creating a text area for input of url
url = st.text_input('Put the url of the API')
# display the value of url in a text box
# st.text(url)

results= get_endpoint(url)
st.json(results)

results= post_endpoint(url)
if isinstance(results,dict):
    st.json(results)
else:
    st.text(results)
