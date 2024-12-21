#老師的程式碼
from tools import get_youBikes
import streamlit as st
youbike_data:list[dict] = get_youBikes()
def map_func(value:dict)->str:
    return value['sarea']

area_list = list(set(map(lambda value:value['sarea'],youbike_data)))
col1,col2 = st.columns([1,3]) #網頁分成1:3
with col1:
    select_area = st.selectbox("行政區域",area_list)
with col2:
    def filter_func(value:dict)->bool:
        return value['sarea'] == select_area
    
    filter_list:list[dict] = list(filter(filter_func,youbike_data))
    show_data:list[dict] = [{'站點':value['sna'],
                             '總增量數':value['tot'],
                             '可還':value['bemp'],
                             '營業中':value['act'],
                             '緯度':value['lat'],
                             '經度':value['lng']} for value in filter_list]
    st.dataframe(show_data)

