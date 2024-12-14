from tools import taipei
import streamlit as st

@st.dialog("Cast your vote")
def vote(error):
    st.write(error)

try:
    youBike_data:list[dict] = taipei.get_youBikes()
except Exception as error: #修改當連線發生異常時,tools內的異常訊息可以傳遞出來
    vote(error)
    st.stop()
else:
    st.write(youBike_data)