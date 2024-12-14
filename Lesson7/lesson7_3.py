import tools

try:
    youBike_data:list[dict] = tools.get_youBikes()
except Exception as e: #修改當連線發生異常時,tools內的異常訊息可以傳遞出來
    print(e)
else:
    print(youBike_data)