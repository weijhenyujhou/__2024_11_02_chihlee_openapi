def bmi_status(bmi:float)->str:
    '''
    Docstring 
        -丟入BMI 回傳狀態
        
    '''
    if bmi < 18.5:
        status ="過輕"
    elif bmi >= 18.5 and bmi < 24:
        status = "正常範圍"
    elif bmi >= 24 and bmi < 27:
        status = "過重"
    elif bmi >= 27 and bmi < 30:
        status = "輕度肥胖"
    elif bmi >= 30 and bmi < 35:
        status = "中度肥胖"
    else:
        status ="重度肥胖"
    return status

def new_func():
    '''
    Docstring 
        輸入身高體重後計算BMI
        型別提示
        
    '''
    while(True):
        try:
            height = int(input("請輸入身高（公分）"))
            weight = int(input("請輸入體重(公斤)"))
            if height <= 0 or weight <= 0:
                print("身高和體重必須是正數！")
                continue
            
        except Exception:
            print("輸入錯誤，請輸入有效的數字")
            continue
        else:
            bmi = weight /(height/100)**2
            status = bmi_status(bmi)
            print(f"您輸入的體重:{weight}(Kg)及身高:{height}(cm),\n計算後取得的BMI值約為{bmi:.2f},\n您的BMI被歸類為{status}。")
            break
        
def main():
    #初始計算次數       
    counter = 0
    while(True):
        new_func()
        #每計算過一次加一
        counter +=1
        print(f"=======以上為您第{counter}次輸入後計算的BMI資料=======")
        
        responed = input("請問您還要再計算其他BMI嗎？(y,n) ").lower().strip() #自動將人員輸入空格刪除及轉換成小寫
        if responed != "y":
            break
    print(f"程式結束。總共計算了 {counter} 次 BMI。")
    
if __name__=='__main__':
    main()