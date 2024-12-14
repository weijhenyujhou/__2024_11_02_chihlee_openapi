from tools import taipei

try:
    youBike_data:list[dict] = taipei.get_youBikes()
except Exception as e: #修改當連線發生異常時,tools內的異常訊息可以傳遞出來
    print(e)
else:
    print(youBike_data)