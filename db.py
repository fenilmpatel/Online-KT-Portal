import psycopg2 as db
from  psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
#connection variable for creating database
def db_con():
    con = db.connect(host='localhost',user='fenil',password="fenilpatel@123",port=5432)
    con.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    return con
#connection variable for creating table    
def tbl_con():
    con = db.connect(database="Portal",user="fenil",password="fenilpatel@123",host="localhost",port=5432)
    cur = con.cursor()
    return con,cur

#creating new database 
def database():
    try:
        con = db_con()
        with con.cursor() as cur:
            cur.execute("DROP DATABASE IF EXISTS Game")
            cur.execute("CREATE DATABASE Game")
            print("database created successfully")
    finally:
        if con:
            # con.commit()
            cur.close()
            con.close()
            print("Transaction closed")
            
#creating  table into database 
def table():
    try:
    
        #create a connection to database
        con,cur = tbl_con()
              
        #create a new table
        cur.execute("CREATE TABLE IF NOT EXISTS employee (Emp_id numeric(10), Name VARCHAR(40), Project VARCHAR(40), Query VARCHAR(80));")
        print("Table created successfully")
    finally:
        con.commit()
        cur.close()
        con.close()
        
# database()
# table()