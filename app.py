from module.lib import readAccount,creatDataBase_Table,importData,viewAll,addMember,updateMember,selectPhone,deleteAll,connectDB

menu='''
---------- 選單 ----------
0 / Enter 離開admin
1 建立資料庫與資料表
2 匯入資料
3 顯示所有紀錄
4 新增記錄
5 修改記錄
6 查詢指定手機
7 刪除所有記錄
--------------------------'''

account=input("請輸入帳號：")
password=input("請輸入密碼：")


if(readAccount(account,password)):
    while True:
        print(menu)
        connectDB("wanghong.db")
        menuNumber=input("請輸入您的選擇 [0-7]:")
        if(menuNumber=="0" or menuNumber==""):
            break
        menuNumber=int(menuNumber)
        if(menuNumber==1):
            creatDataBase_Table("wanghong.db")
        elif(menuNumber==2):
            importData()    
        elif(menuNumber==3):
            viewAll()
        elif(menuNumber==4):
            name=input("請輸入姓名: ")
            gander=input("請輸入性別: ")
            phone=input("請輸入手機: ")
            addMember(name,gander,phone)
        elif(menuNumber==5):
            name=input("請輸入想修改記錄的姓名: ")
            if(name!=""):
                gander=input("請輸入要改變的性別: ")
                phone=input("請輸入要改變的手機: ")
                updateMember(gander,phone,name)
            else:
                print("=>必須指定姓名才可修改記錄")    
        elif(menuNumber==6):
            phoneNumber=input("請輸入想查詢記錄的手機: ")
            selectPhone(phoneNumber)
        elif(menuNumber==7):
            deleteAll()     
        else:
            print("=>無效的選擇")                 
else:
    print("=>帳密錯誤，程式結束")  

