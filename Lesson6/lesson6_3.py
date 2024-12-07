import streamlit as st
import tools


sitenames:list[str] = tools.get_sitename(excel_name='aqi.xlxs')
add_selectbox = st.sidebar.selectbox(
    "請選擇站點名稱",
    sitenames
)
