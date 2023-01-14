import sys
import mysql.connector

def insertRecord(userInfo):
    conn=None
    sql="""INSERT INTO users VALUES(%s,%s,%s,%s,%s,%s)"""
    try:
        conn = mysql.connector.connect(host='localhost', user='root', password='',port='3306', database='level4d')
        cursor=conn.cursor()
        cursor.execute(sql,userInfo)
        conn.commit()
        cursor.close()
        conn.close()
        print("Successfully Inserted")
    except:
        print("Error", sys.exc_info())
    finally:
        del sql
        del conn

def loginUser(userInfo):
    conn=None
    sql="""SELECT * FROM users WHERE email=%s and password=%s"""
    try:
        conn = mysql.connector.connect(host='localhost', user='root', password='', port='3306', database='level4d')
        cursor = conn.cursor()
        cursor.execute(sql, userInfo)
        user=cursor.fetchall()
        print(user)
        if user!=None:
            print('Welcome',user[0][1])
        else:
            print('User Not Found!')
        cursor.close()
        conn.close()
    except:
        print("Error",sys.exc_info())
    finally:
        del sql
        del conn
#test
# userInfo=(3,'Mota','Baluwa','baluwamotu@gmail.com','1432','9841360969')
# insertRecord(userInfo)
userInfo=('baluwamotu@gmail.com','1432')
loginUser(userInfo)