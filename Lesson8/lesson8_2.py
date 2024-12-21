import streamlit as st
#手動建立session_state, 並且設定初始值為0 
if "counter" not in st.session_state:
    #st.session_state["counter"] = 0
    st.session_state.counter = 1
## 這裡的kwargs是一個dict
def increment_counter(**kwargs):
    st.session_state.counter += kwargs['first']
    st.session_state.counter -= kwargs['second']

st.header(f"這頁已經執行 {st.session_state.counter} 次.")
st.button("再執行一次", key="restart",help='按下時要加1',on_click=increment_counter,kwargs={'first':5,'second':3}) # key="restar"不管有沒有建立都會自動建立
st.write(st.session_state)