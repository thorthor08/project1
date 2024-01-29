import streamlit as st

# Main page title
st.title("Main Page")

# Button to show/hide sidebar content
if st.button("Show Sidebar Content"):
    st.sidebar.title("Sidebar")
    st.sidebar.write("This is some content in the sidebar.")
    st.sidebar.slider("Slider in sidebar", 0, 100)
elif st.button("Hide Sidebar Content"):
    st.sidebar.empty()
