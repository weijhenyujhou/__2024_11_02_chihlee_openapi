import streamlit as st
import tools


sitenames:list[str] = tools.get_sitename(excel_name='aqi.xlxs')
#add_selectbox = st.sidebar.selectbox(
#    "請選擇站點名稱",
#    sitenames
#)
# With Notation

with st.sidebar: #with建立於文件變數底下ㄌ
    add_selectbox = st.selectbox(
    "請選擇站點名稱:",
    sitenames
    )
    
    st.title(f"{add_selectbox}")