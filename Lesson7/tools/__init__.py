#將tools.py 轉換成package tools資料夾內__init__.py檔
import requests
from io import StringIO
from csv import DictReader
from requests import Response # type: ignore
from requests.exceptions import RequestException,HTTPError 

def get_youBikes()->list[dict]:
    url = 'https://data.ntpc.gov.tw/api/datasets/010e5b15-3823-4b20-b401-b1cf000550c5/csv?page=0&size=1000'
    
    
    try:
        r:Response = requests.request('GET',url)
        r.raise_for_status()   
    except HTTPError as e: #例外處理
        raise Exception("伺服器有問題")
    except RequestException as e:
        raise Exception("伺服器連線有問題")
    else:
        print("下載成功")
        file = StringIO(r.text)
        reader = DictReader(file)
        list_reader:list[dict] = list(reader)
        #for row in list_reader:
            #print(row)
        return list_reader