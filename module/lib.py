import json
import sqlite3

def readAccount(account:str,password:str):
    """
    讀取帳號並判斷是否正確
    """
    with open("pass.json","r",encoding="UTF-8") as f:
        content=json.load(f)
        for scan in content:
            if(scan["帳號"]==account and scan["密碼"]==password):
                return True

def connectDB(dbName:str):
    """
    資料庫連線
    """
    global cursor,conn
    conn = sqlite3.connect(dbName)
    cursor = conn.cursor()

def creatDataBase_Table(dbName:str):
    """
    建立資料庫與資料表
    """
    conn = sqlite3.connect(dbName)
    cursor = conn.cursor()
    cursor.execute(''' 
    CREATE TABLE IF NOT EXISTS members(
        ild INTEGER PRIMARY KEY AUTOINCREMENT,
        mname TEXT NOT NULL,
        msex TEXT NOT NULL,
        mphone TEXT NOT NULL           
    );
    ''')
    print("=>資料庫已建立")

def importData():
    """
    匯入資料
    """
    global cursor,conn
    count=0
    with open("members.txt","r",encoding="UTF8")as f:
        for line in f:
            member=line.strip().split(",")
            try:
                cursor.execute("INSERT INTO members(mname,msex,mphone) VALUES (?,?,?);",member)
                count=count+1
                conn.commit()    
            except sqlite3.Error as error:
                print(f"執行 INSERT 操作時發生錯誤：{error}")    
        print(f"=>異動 {count} 筆記錄")    

def viewAll():
    """
    顯示所有資料
    """
    try:
        cursor.execute("SELECT * FROM members")
        data = cursor.fetchall()
    except sqlite3.Error as error:
        print(f"執行 SELECT 操作時發生錯誤：{error}")
    if len(data) > 0:
        print("姓名　　　　性別　手機")
        print("-----------------------------")
        for record in data:
            print(f"{record[1]:　<6}{record[2]:<6}{record[3]}")
    else:
        print("查無資料")

def addMember(name:str,gander:str,phone:str):
    """
    新增成員
    """
    try:
        cursor.execute("INSERT INTO members(mname, msex, mphone) VALUES (?, ?, ?);",
             (name, gander, phone))
        print(f"=>異動 {cursor.rowcount} 筆記錄")
        conn.commit()
    except sqlite3.Error as error:
        print(f"執行 INSERT 操作時發生錯誤：{error}")

def selectName(name:str):
    """
    搜尋成員
    """
    try:
        cursor.execute("SELECT * FROM members WHERE mname LIKE ?",("%"+name+"%",))
        data = cursor.fetchall()
    except sqlite3.Error as error:
        print(f"執行 SELECT 操作時發生錯誤：{error}")
    if len(data) > 0:
        for record in data:
            print(f"姓名:{record[1]},性別:{record[2]},手機:{record[3]}")
    else:
        print("查無資料")

def updateMember(gander:str,phone:str,name:str):
    """
    更新成員
    """
    print()
    print("原資料：")
    selectName(name)
    cursor.execute("UPDATE members SET msex=?, mphone=? WHERE mname=?;", (gander,phone,name))
    print(f"=>異動 {cursor.rowcount} 筆記錄")
    print("修正後資料：")
    selectName(name)
    conn.commit()

def selectPhone(phoneNumber:str):
    """
    搜尋電話話碼
    """
    try:
        cursor.execute("SELECT * FROM members WHERE mphone LIKE ?",("%"+phoneNumber+"%",))
        data = cursor.fetchall()
    except sqlite3.Error as error:
        print(f"執行 SELECT 操作時發生錯誤：{error}")
    if len(data) > 0:
        print("姓名　　　　性別　手機")
        print("-----------------------------")
        for record in data:
            print(f"{record[1]:　<6}{record[2]:<6}{record[3]}")
    else:
        print("查無資料")

def deleteAll():
    """
    刪除所有資料
    """
    try:
        cursor.execute("DELETE FROM  members")
        print(f"=>異動 {cursor.rowcount} 筆記錄")
        conn.commit()
    except sqlite3.Error as error:
        print(f"執行 DELETE 操作時發生錯誤：{error}")           