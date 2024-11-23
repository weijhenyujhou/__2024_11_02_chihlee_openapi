import tool
def main():
    #初始計算次數       
    counter = 0
    while(True):
        tool.new_func()
        #每計算過一次加一
        counter +=1
        print(f"=======以上為您第{counter}次輸入後計算的BMI資料=======")
        
        responed = input("請問您還要再計算其他BMI嗎？(y,n) ").lower().strip() #自動將人員輸入空格刪除及轉換成小寫
        if responed != "y":
            break
    print(f"程式結束。總共計算了 {counter} 次 BMI。")
    
if __name__=='__main__':
    main()