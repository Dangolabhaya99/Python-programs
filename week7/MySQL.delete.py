import sys
import mysql.connector
sql="""DELETE FROM persons WHERE pid=2"""
try:
    conn=mysql.connector.connect(host='localhost',user='root',password='',database='level4d')
    cursor=conn.cursor()
    cursor.execute(sql)
    conn.commit()
    cursor.close()
    conn.close()
    print("Delete Sucessfully")
except:
    print("Error While Delecting",sys.exc_info())