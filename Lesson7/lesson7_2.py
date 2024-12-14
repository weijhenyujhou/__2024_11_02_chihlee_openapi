import requests
from io import StringIO
from csv import DictReader
from requests.exceptions import RequestException,HTTPError 
url = 'https://data.ntpc.gov.tw/api/datasets/34b402a8-53d9-483d-9406-24a682c2d6dc/csv?page=0&size=1000'
r = requests.get(url)
r.text
print(r.text)

from requests import Response # type: ignore
r_1:Response = requests.request('Get',url)
try:
    r:Response = requests.request('GET',url)
    r.raise_for_status()   
except HTTPError as e:
    print(e)
except RequestException as e:
    print(e)
else:
    print("下載成功")
    file = StringIO(r_1.text)
    reader = DictReader(file)
    list_reader:list[dict] = list(reader)
    for row in list_reader: # reader是一個generator的實體
        print(row)