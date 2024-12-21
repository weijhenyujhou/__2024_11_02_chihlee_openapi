#我請Github polit 產生
from tools import get_youBikes
import streamlit as st
import pandas as pd

get_youBikes:list[dict] = get_youBikes()

#使用streamlit分2個欄位
#使用youBike_data:list的資料, 取出行政區域(sarea)的資料,並使用set()取出不重複的行政區
#左邊選擇行政區,使用下拉式表單
#右邊是顯示該行政區的youbike站點的表格資訊
#最下方顯示該行政區的youbike站點數地圖
# 使用streamlit分2個欄位
col1, col2 = st.columns(2)

# 使用youBike_data:list的資料, 取出行政區域(sarea)的資料,並使用set()取出不重複的行政區
sareas = set([bike['sarea'] for bike in get_youBikes])

# 左邊選擇行政區,使用下拉式表單
selected_sarea = col1.selectbox('選擇行政區', sareas)

# 右邊是顯示該行政區的youbike站點的表格資訊
filtered_bikes = [bike for bike in get_youBikes if bike['sarea'] == selected_sarea]
col2.table(filtered_bikes)

# 最下方將選取的行政區Youbike資訊顯示在地圖上

# 將 list 轉換為 DataFrame
bike_df = pd.DataFrame(filtered_bikes)

# 重新命名經度欄位
bike_df = bike_df.rename(columns={'lng': 'lon'})

# 將 lat 和 lon 轉為數值型態
bike_df['lat'] = pd.to_numeric(bike_df['lat']) 
bike_df['lon'] = pd.to_numeric(bike_df['lon'])

st.map(bike_df)