import psycopg2 as database
from flask import Flask,render_template,url_for,request
import database
con,cur = database.tbl_con()   

def insert():
    try:
        # E = input("Enter your emp id")
        # N   = input("Enter Your Name")
        # P = input("Enter your project name")
        # Q  = input("Write your query")
        Emp_Id = request.form['Emp_Id']
        Name = request.form['Name']
        Project  = request.form['Project']
        Query = request.form['Query']
        data = (Emp_Id,Name,Project,Query)
        Qry  = "INSERT INTO employee(Emp_id,Name,Project,Query) VALUES (%s,%s,%s,%s)"
        #insert data to table
        cur.execute(Qry,data)
        print("data inserted successfully..")
    finally:
        con.commit()
        cur.close()
        con.close()
        
def show():
    try:
        cur.execute("SELECT * FROM employee;")
        data = cur.fetchall()
        #iterate over data to retrive info..
        for d in data:
            print("emp id", d[0])
            print("Employee name:",d[1])
            print("Project name",d[2])
            print("Query",d[3])
            
    finally:

        con.commit()
        cur.close()
        con.close()
show()
# insert()