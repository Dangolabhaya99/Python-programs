import mysql.connector
import sys
from driver import Driver

def saveDriver(driverInfo):
    conn = None
    sql = """INSERT INTO drivers VALUES (%s, %s, %s)"""
    values = (driverInfo.getDID(),driverInfo.getName(),driverInfo.getLicenseNo())
    try:
        conn = mysql.connector.connect(host='localhost',port='3306',user='root',password='',database='level4d')
        cursor = conn.cursor()
        cursor.execute(sql, values)
        conn.commit()
        cursor.close()
        conn.close()
        print("Save Driver!")
    except:
        print("Error", sys.exc_info())
    finally:
        del values
        del sql
        del conn

def searchDriver(licenseno):
    conn = None
    sql = """SELECT * FROM drivers WHERE licenseno=%s"""
    values = (licenseno,)
    driver = None
    try:
        conn = mysql.connector.connect(host='localhost', port='3306', user='root', password='', database='level4d')
        cursor = conn.cursor()
        cursor.execute(sql, values)
        driver = cursor.fetchall()
        cursor.close()
        conn.close()
        print("Search Successfull!")
    except:
        print("Error", sys.exc_info())
    finally:
        del values
        del sql
        del conn
        return driver

def updateDriver(driverInfo):
    conn = None
    sql = """UPDATE drivers set name=%s,licenseno=%s WHERE did=%s"""
    values=(driverInfo.getName(),driverInfo.getLicenseNo(),driverInfo.getDID())
    result=False
    try:
        conn = mysql.connector.connect(host='localhost', user='root', password='', database='level4d')
        cursor = conn.cursor()
        cursor.execute(sql, values)
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

def deleteDriver(did):
    conn=None
    sql = """DELETE FROM drivers WHERE did=%s"""
    values=(did,)
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
    sql="""SElECT * From drivers"""
    drivers=None
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
        return drivers