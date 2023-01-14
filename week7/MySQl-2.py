import sys
import mysql.connector

def insertRecord():
    try:
        sql="""INSERT INTO students VALUES(%s,%s,%s,%s)"""
        values=[1,'Dangol',69,56]
        conn=mysql.connector.connect(host='localhost',user='root',password='',database='level4d')
        cursor=conn.cursor()
        cursor.execute(sql,values)
        conn.commit()
        cursor.close()
        conn.close()
        print("Reocrds Inserted")
    except:
        print("Error",sys.exc_info())

def searchRecord():
    try:
        sid = (1,)
        sql="""SELECT * FROM students WHERE sid=%s"""
        conn=mysql.connector.connect(host='localhost',user='root',password='',database='level4d')
        cursor=conn.cursor()
        cursor.execute(sql, sid)
        record=cursor.fetchone()
        print(record)
        cursor.close()
        conn.close()
        print("Successfully Searched")
    except:
        print("Error",sys.exc_info())

def displayAll():
    try:
        sql="""SELECT * FROM students"""
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

def updateRecord():
    try:
        values=('Abhaya',99,80,1)
        sql="UPDATE students set name=%s, isd=%s, fcs=%s, WHERE sid=%s"
        conn = mysql.connector.connect(host='localhost', user='root', password='', database='level4d')
        cursor = conn.cursor()
        cursor.execute(sql, values)
        conn.commit()
        cursor.close()
        conn.close()
        print("Successfully Updated")
    except:
        print("Error",sys.exc_info())

def deleteRecord():
    try:
        sid=(1,)
        sql="""DELETE FROM students WHERE sid=%s"""
        conn = mysql.connector.connect(host='localhost', user='root', password='', database='level4d')
        cursor = conn.cursor()
        cursor.execute(sql,sid)
        conn.commit()
        cursor.close()
        conn.close()
        print("Successfully Deleted")
    except:
        print("Error",sys.exc_info())

#Test
# insertRecord()
# searchRecord()
# displayAll()
# updateRecord()
deleteRecord()

# sql="""INSERT INTO students"""
# try:
#     conn=mysql.connector.connect(host='localhost',user='root',password='',database='level4d')
#     cursor=conn.cursor()
#     cursor.execute(sql)
#     conn.commit()
#     cursor.close()
#     conn.close()
#     print("Successfully Inserted")
# except:
#     print("Error while Inserting",sys.exc_info())