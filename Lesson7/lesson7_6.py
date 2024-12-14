import streamlit as st

if 'key' not in st.session_state:
    print("first")
    st.session_state['key'] = 'value'
    
if 'key' not in st.session_state:
    print('sencond')
    st.session_state['key'] = 'value'
    