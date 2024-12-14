# session
import streamlit as st

st.title("次數的範例")
if 'count' not in st.session_state:
    st.session_state['count'] = 0

increasement = st.button("每次加一")
if increasement:
    st.session_state['count'] +=1
    
st.write('次數=',st.session_state['count'])