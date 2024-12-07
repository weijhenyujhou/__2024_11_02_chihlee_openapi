import tools

def main():
    data:list[dict] = tools.get_aqi(excel_name='aqi.xlsx')
    sitenames:list =[]
    for item in data:
        sitenames.append(item['sitename'])
        #刪除重複的
        sitenames = list(set(sitenames))
        for name in sitenames:
            print(name)
    print(len(sitenames))

if __name__=='__main__':
    main()