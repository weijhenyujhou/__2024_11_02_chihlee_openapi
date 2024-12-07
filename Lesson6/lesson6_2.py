from openpyxl import load_workbook, workbook, worksheet
from pprint import pprint
#讀入資料的function
def get_aqi(excel_name:str)-> list[dict]:
    wb:workbook = load_workbook(excel_name)
    sheet:worksheet = wb.worksheets[0]
    type(sheet)
    sheets:list = []
    # comprehensions語法快數建立list
    column_name = [cell.value for cell in list(sheet)[0]]
    print(column_name)

    for row in list(sheet)[1:]:
        site:dict = {column_name[idx]:cell.value for idx, cell in enumerate(row)}
        sheets.append(site)
    return sheets

def main():
    data:list[dict] = get_aqi(excel_name='aqi.xlsx')
    pprint(data)

if __name__=='__main__':
    main()