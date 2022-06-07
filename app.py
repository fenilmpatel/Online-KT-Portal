from itertools import count
from pickle import TRUE
from sys import flags
from flask import Flask,render_template,url_for,request
from werkzeug.exceptions import HTTPException
import psycopg2 as db
from database import tbl_con

#initialize flask app
app = Flask(__name__)
con,cur = tbl_con() 


#Set home page
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/insert',methods=['GET','POST'])
def insert():
    flag ='false'
    return render_template('insert.html',flag=flag)
@app.route('/run_insert',methods=['GET','POST'])
def run_insert():
    try:
        Emp_Id = request.form['Emp_Id']
        Name = request.form['Name']
        Project  = request.form['Project']
        Query = request.form['Query']
        data = (Emp_Id,Name,Project,Query)
        Qry  = "INSERT INTO employee(Emp_id,Name,Project,Query) VALUES (%s,%s,%s,%s)"
        #insert data to table
        cur.execute(Qry,data)
        con.commit()
        flag = 'true'
        con.commit()    
        cur.close()
        con.close()
        return render_template("insert.html",flag=flag)
    except db.DatabaseError as e:
        raise e
   
    
@app.route('/view',methods=['GET','POST'])
def view():
    return render_template('view.html')
@app.route('/run_view',methods=['GET','POST'])
def run_view():
    try:
    
        #create a connection to database
        con,cur = tbl_con()
              
        #create a new table
        cur.execute("SELECT * FROM employee")
        con.commit()
        data = enumerate(cur.fetchall(),1)
        con.commit()
        cur.close()
        con.close()
        return render_template('view.html',data=data)
        
    except db.DatabaseError as e:
        raise e
   
    
@app.route('/find',methods=['GET','POST'])
def find():
    flag ='false'
    return render_template('search.html',flag=flag)
    
@app.route('/run_find',methods=['GET','POST'])
def run_find():
    try:
    
        #create a connection to database
        con,cur = tbl_con()
        qry =  "SELECT * FROM employee where emp_id=%s"
        Emp_Id = request.form['Emp']
        data = (Emp_Id,)
        cur.execute(qry,data)
        count='true'
        flag = cur.fetchall()
        rec = enumerate(flag,1)
        con.commit()
        return render_template('search.html',flag=flag,rec=rec,count=count)
    except db.DatabaseError as e:
        print(e)
    con.close()
    cur.close()
    con.close()
    
@app.route('/delete',methods=['GET','POST'])
def delete():
    flag ='false'
    return render_template('delete.html',flag=flag)
@app.route('/run_delete',methods=['GET','POST'])
def run_delete():
    try:
        #create a connection to database
        con,cur = tbl_con()
        qry =  "DELETE FROM employee where emp_id=%s"
        Emp_Id = request.form['Emp']
        data = (Emp_Id,)
        cur.execute(qry,data)
        rm = cur.rowcount
        flag = 'true'
        con.commit()
        cur.close()
        con.close()
        return render_template('delete.html',flag=flag,rm=rm)
    
    except db.DatabaseError as e:
        print(e)
    
    
@app.route('/update',methods=['GET','POST'])
def update():
    flag ='false'
    return render_template('update.html',flag=flag)
@app.route('/run_update',methods=['GET','POST'])
def run_update():
    try:
    
        #create a connection to database
        con,cur = tbl_con()
        qry  =  "UPDATE employee SET Emp_Id=%s,Name=%s,Project=%s,Query=%s where Emp_Id=%s"
        Emp_Id = request.form['Emp_Id']
        Name = request.form['Name']
        Project  = request.form['Project']
        Query = request.form['Query']
        Old_Emp_Id = request.form['Old_Emp_Id']
        data = (Emp_Id,Name,Project,Query,Old_Emp_Id)
        cur.execute(qry,data)
        flag = 'true'
        con.commit()
        # cur.close() 
        # con.close()
        return render_template('update.html',flag=flag)
    except db.DatabaseError as e:
        raise e
    
@app.errorhandler(HTTPException)
def handle_exception(e):
    if isinstance(e,HTTPException):
        return e


    
        
        

             
