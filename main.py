import streamlit as st

# Title of the main page
st.title("Main Page")

# Sidebar with a slider
st.sidebar.title("Sidebar")
slider_value = st.sidebar.slider("Select a value", 0, 100)

# Displaying the slider value in the main page
st.write(f"You selected: {slider_value}")
