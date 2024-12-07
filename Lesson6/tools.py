from openpyxl import load_workbook, workbook, worksheet
from pprint import pprint
# 讀入資料的function


def get_aqi(excel_name: str) -> list[dict]:
    wb: workbook = load_workbook(excel_name)
    sheet: worksheet = wb.worksheets[0]
    type(sheet)
    sheets: list = []
    # comprehensions語法快速建立list
    column_name = [cell.value for cell in list(sheet)[0]]
    print(column_name)

    for row in list(sheet)[1:]:
        site: dict = {column_name[idx]: cell.value for idx, cell in enumerate(row)}
        sheets.append(site)
    return sheets


def get_sitename(excel_name: str) -> list[str]:
    data: list[dict] = get_aqi(excel_name='aqi.xlsx')
    sitenames: list = []
    for item in data:
        sitenames.append(item['sitename'])
        # 刪除重複的
    sitenames = list(set(sitenames))
    return sitenames


###

##macbook

##mb
