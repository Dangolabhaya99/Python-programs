import sys
import mysql.connector

def insertDetails():
    try:
        sql="""INSERT INTO users VALUES(%s,%s,%s,%s,%s,%s)"""
        values=[1,'Magar','Thankot','magar69@gmail.com','wish@123',9841360969]
        conn=mysql.connector.connect(host='localhost',user='root',password='',database='level4d')
        cursor=conn.cursor()
        cursor.execute(sql,values)
        conn.commit()
        cursor.close()
        conn.close()
        print("Successfully Inserted")
    except:
        print("Error While Inserting",sys.exc_info())

def searchDetails():
    try:
        email=('magar69@gmail.com',)
        sql="""SELECT * FROM users WHERE email=%s"""
        conn=mysql.connector.connect(host='localhost',user='root',password='',database='level4d')
        cursor=conn.cursor()
        cursor.execute(sql, email)
        record=cursor.fetchone()
        print(record)
        cursor.close()
        conn.close()
        print("Successfully Searched")
    except:
        print("Error",sys.exc_info())

def displayAlldetails():
    try:
        sql="""SELECT * FROM users"""
        conn=mysql.connector.connect(host='localhost',user='root',password='',database='level4d')
        cursor = conn.cursor()
        cursor.execute(sql)
        record = cursor.fetchall()
        print(record)
        cursor.close()
        conn.close()
        print("Displayed Successfully")
    except:
        print("Error",sys.exc_info())

def updateDetails():
    try:
        values=(2,'Magarni','Thankot,ktm','wishmeluck123','143298765','magar69@gmail.com')
        sql="UPDATE users set uid=%s,fullname=%s,address=%s,password=%s,mobile=%s WHERE email=%s"
        conn = mysql.connector.connect(host='localhost', user='root', password='', database='level4d')
        cursor = conn.cursor()
        cursor.execute(sql, values)
        conn.commit()
        cursor.close()
        conn.close()
        print("Successfully Updated")
    except:
        print("Error",sys.exc_info())

def deleteDetails():
    try:
        email=('arsenal99@gmail.com',)
        sql="""DELETE FROM users WHERE email=%s"""
        conn = mysql.connector.connect(host='localhost', user='root', password='', database='level4d')
        cursor = conn.cursor()
        cursor.execute(sql,email)
        conn.commit()
        cursor.close()
        conn.close()
        print("Successfully Deleted")
    except:
        print("Error",sys.exc_info())

# #test
# # insertDetails()
# searchDetails()
# displayAlldetails()
# updateDetails()
# deleteDetails()