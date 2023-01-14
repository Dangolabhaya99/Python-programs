import mysql.connector
import sys
from customer import Customer

def saveCustomer(customerInfo):
    conn = None
    sql = """INSERT INTO customers VALUES (%s,%s,%s)"""
    values=(customerInfo.getCID(),customerInfo.getName(),customerInfo.getAddress())
    try:
        conn = mysql.connector.connect(host='localhost',port='3306',user='root',password='',database='level4d')
        cursor = conn.cursor()
        cursor.execute(sql,values)
        conn.commit()
        conn.close()
        cursor.close()
        print("Customer Saved!!")
    except:
        print("Error",sys.exc_info())
    finally:
        del values
        del sql
        del conn

def searchCustomer(cid):
    conn = None
    sql = """SELECT * FROM customers WHERE cid=%s"""
    values = (cid,)
    customer = None
    try:
        conn = mysql.connector.connect(host='localhost', port='3306', user='root', password='', database='level4d')
        cursor = conn.cursor()
        cursor.execute(sql, values)
        customer=cursor.fetchall()
        conn.commit()
        conn.close()
        cursor.close()
        print("Search Success!!")
    except:
        print("Error",sys.exc_info())
    finally:
        del values
        del sql
        del conn
        return customer

def updateCustomer(customerInfo):
    conn = None
    sql = """UPDATE customers set name=%s,address=%s WHERE cid=%s"""
    values = (customerInfo.getName(),customerInfo.getAddress(),customerInfo.getCID())
    result = False
    try:
        conn = mysql.connector.connect(host='localhost', port='3306', user='root', password='', database='level4d')
        cursor = conn.cursor()
        cursor.execute(sql, values)
        conn.commit()
        conn.close()
        cursor.close()
        result = True
        print("Update Success!!")
    except:
        print("Error",sys.exc_info())
    finally:
        del values
        del sql
        del conn
        return result

def deleteCustomer(cid):
    conn = None
    sql = """DELETE FROM customers WHERE cid=%s"""
    values=(cid,)
    result=False
    try:
        conn = mysql.connector.connect(host='localhost', user='root', password='', database='level4d')
        cursor = conn.cursor()
        cursor.execute(sql,values)
        conn.commit()
        cursor.close()
        conn.close()
        result=True
    except:
        print("Error", sys.exc_info())
    finally:
        del values
        del sql
        del conn
        return result

def allDrivers():
    conn = None
    sql = """SElECT * From customers"""
    customers = None
    try:
        sql = """SELECT * FROM drivers"""
        conn = mysql.connector.connect(host='localhost', user='root', password='', database='level4d')
        cursor = conn.cursor()
        cursor.execute(sql)
        record = cursor.fetchall()
        print(record)
        cursor.close()
        conn.close()
        print("Displayed Successfully")
    except:
        print("Error", sys.exc_info())
    finally:
        del sql
        del conn
        return customers