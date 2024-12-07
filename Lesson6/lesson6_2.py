import tools  # 將模組化方法匯入
import openpyxl
from openpyxl import Workbook, worksheet


def main():
    sitenames: list[str] = tools.get_sitename(excel_name='aqi.xlsx')
    print(sitenames)
    wb: Workbook = openpyxl.Workbook()
    sheet: worksheet = wb.active
    sheet.title = "站點名稱"
    for idy, name in enumerate(sitenames):  # enumerate ?
        print(name)
        sheet.cell(column=1, row=idy+1, value=name)
    wb.save('老闆要的資料.xlsx')


if __name__ == '__main__':
    main()
