#import Library
import sys
import mysql.connector
sql="""SELECT * FROM persons"""
try:
    #conncet
    conn=mysql.connector.connect(host='localhost',user='root',password='',database='level4d')
    cursor=conn.cursor()
    cursor.execute(sql)
    records=cursor.fetchall()
    print(records)
    #close
    cursor.close()
    conn.close()
    print("Records retrieve successfully")
except:
    print("Errror",sys.exc_info())