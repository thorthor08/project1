import streamlit as st

# Main page title
st.title("Main Page")

# Adding elements to the sidebar with reduced spacing using HTML in Markdown
st.sidebar.title("Sidebar")
st.sidebar.markdown("<span style='line-height: 0.5;'>boulders</span>", unsafe_allow_html=True)
st.sidebar.markdown("<span style='line-height: 0.5;'>flashes</span>", unsafe_allow_html=True)
st.sidebar.markdown("<span style='line-height: 0.5;'>create</span>", unsafe_allow_html=True)

