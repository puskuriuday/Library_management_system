import psycopg2
import os
from dotenv import load_dotenv
load_dotenv()

def dbconn():
    try:
        db = os.getenv("DBString")
        conn = psycopg2.connect(db)
        cur = conn.cursor()
        return conn , cur

    except Exception as error:
        print(error)

def comm(conn):
    try:
        conn.commit()
    except Exception as error:
        print(error)

def clscur(cur):
    try:
        cur.close()
    except Exception as error:
        print(error)

def clsconn(conn):
    try:
        conn.close()
    except Exception as error:
        print(error)