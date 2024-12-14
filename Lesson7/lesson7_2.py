import requests
from io import StringIO
from csv import DictReader
url = 'https://data.ntpc.gov.tw/api/datasets/34b402a8-53d9-483d-9406-24a682c2d6dc/csv?page=0&size=1000'
r = requests.get(url)
r.text
print(r.text)

from requests import Response # type: ignore
r_1:Response = requests.request('Get',url)
if r_1.status_code == 200:
    print("DownLoad Successful")
    file = StringIO(r_1.text)
    reader = DictReader(file)
    list_reader = reader 
    for row in list_reader: # reader是一個generator的實體
        print(row)
    
else:
    print("DownLoad Failed")