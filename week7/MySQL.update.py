import sys
import mysql.connector
sql="""UPDATE persons set Name='Abhaya Dangol',Address='Ktm' WHERE pid=1"""
try:
    conn=mysql.connector.connect(host='localhost',user='root',password='',database='level4d')
    cursor=conn.cursor()
    cursor.execute(sql)
    conn.commit()
    cursor.close()
    conn.close()
    print("Update successfull")
except:
    print("Error While Updating",sys.exc_info())