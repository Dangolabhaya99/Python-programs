# install library to connect
# pip install mysql-connector-python


# Connect with Database Server
import mysql.connector  # import Library
import sys
try:
    conn =mysql.connector.connect(
        host='localhosts',
        user='root',
        password='',
        database='persons'
    ) # Connectwith mysql server
    conn.close() #connection close with mysql
    print("Conncet with database server successfully")
except:
    print("Error",sys.exc_info())