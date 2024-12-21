import streamlit as st
#手動建立session_state, 並且設定初始值為0 
if "counter" not in st.session_state:
    #st.session_state["counter"] = 0
    st.session_state.counter = 1

def increment_counter(args):
    st.session_state.counter += args[0]
    st.session_state.counter -= args[1]

st.header(f"這頁已經執行 {st.session_state.counter} 次.")
st.button("再執行一次", key="restart",help='按下時要加1',on_click=increment_counter,args=(5,3)) # key="restar"不管有沒有建立都會自動建立
st.write(st.session_state)