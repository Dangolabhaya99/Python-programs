import sys
import mysql.connector

def connect():
    conn = None
    try:
        conn = mysql.connector.connect(host='localhost', port=3306, user='root', password='', database='level4d')
        print("Connected!")
    except:
        print("Error: ", sys.exc_info())
    finally:
        return conn

def insert(person):
    sql = "INSERT INTO persons VALUES (%s, %s, %s)"
    values = (person.getPID(), person.getName(), person.getAddress())
    result = {'status':False, 'message':None}
    try:
        conn = connect()
        cursor=conn.cursor()
        cursor.execute(sql, values)
        conn.commit()
        cursor.close()
        conn.close()
        result['status']=True
        result['message']="Record save successfully"
        print("Inserted!")
    except:
        result['status'] = False
        result['message'] = sys.exc_info()
        print("Error", sys.exc_info())
    finally:
        del values
        del sql
        return result

def all():
    sql = """SELECT * FROM persons"""
    persons = None
    try:
        conn = connect()
        cursor = conn.cursor()
        cursor.execute(sql)
        persons = cursor.fetchall()
        cursor.close()
        conn.close()
    except:
        print("Error : ", sys.exc_info())
    finally:
        del sql
        return persons