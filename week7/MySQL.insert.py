import sys
import mysql.connector
sql="""INSERT INTO persons VALUES(2,'Dangol','Chandragiri')"""
try:
    #connect
    conn=mysql.connector.connect(host='localhost',user='root',password='',database='level4d')
    #insert
    cursor=conn.cursor()#Traveller
    cursor.execute(sql)#insert
    conn.commit()#save
    #close
    conn.close()
    print("Insert record successfully")
except:
    print("Error",sys.exc_info())# Display Error message