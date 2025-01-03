# tool 
class Person:
    '''
    我是person
    '''
    def __init__ (self,name:str,age:int):
        self.name = name
        self.age = age
    def echo(self):
        print(f"我的名子是{self.name}")
        print(f"我的年紀是{self.age}")
    
class student(Person):
    '''
    我是student
    '''
    def __init__(self,name:str,age:int,score:int):
        super().__init__(name=name,age=age) #呼叫父類別初始化
        self.__score =score
    
    @property
    def socre(self)->int:
        return self.__score
    
    def echo(self):
        super().echo() #呼叫父類別方法
        print(f"我的分數是:{self.__score}")



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

