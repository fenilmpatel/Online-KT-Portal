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
    return render_template('insert.html')
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
        data = 1
        return render_template("insert.html",data=data)
    except db.DatabaseError as e:
        pass
    con.commit()    
    cur.close()
    con.close()
    
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
        data = cur.fetchall()
        return render_template('view.html',data=data)
    except db.DatabaseError as e:
        print(e)
    con.close()
    cur.close()
    con.close()
    
# @app.route('/find',methods=['GET','POST'])
# def find():
#     try:
    
#         #create a connection to database
#         con,cur = tbl_con()
#         qry =  "SELECT * FROM employee where emp_id=%s"
#         Emp_Id = request.form['Emp']
#         data = (Emp_Id,)
#         cur.execute(qry,data)
#         search = cur
#         con.commit()
#         return render_template('view.html',search=search)
#     except db.DatabaseError as e:
#         print(e)
#     con.close()
#     cur.close()
#     con.close()
    
# @app.route('/delete',methods=['GET','POST'])
# def delete():
#     try:
    
#         #create a connection to database
#         con,cur = tbl_con()
#         qry1 =  "DELETE FROM employee where emp_id=%s"
#         qry2 = "SELECT * FROM employee"
#         Emp_Id = request.form['Emp']
#         data = (Emp_Id,)
#         cur.execute(qry1,data)
#         rm = cur.rowcount
#         # con.commit()
#         cur.execute(qry2)
#         tbl = cur.fetchall()
#         con.commit()
#         return render_template('view.html',rm=rm,tbl=tbl)
    
#     except db.DatabaseError as e:
#         print(e)
#     con.close()
#     cur.close()
#     con.close()
    
# @app.route('/update',methods=['GET','POST'])
# def update():
#     try:
    
#         #create a connection to database
#         con,cur = tbl_con()
#         qry1 =  "UPDATE employee SET Emp_Id=%s,Name=%s,Project=%s,Query=%s where Emp_Id=%s"
#         qry2 = "SELECT * FROM employee"
#         Emp_Id = request.form['Emp_Id']
#         Name = request.form['Name']
#         Project  = request.form['Project']
#         Query = request.form['Query']
#         Old_Emp_Id = request.form['Old_Emp_Id']
#         data = (Emp_Id,Name,Project,Query,Old_Emp_Id)
    
#         cur.execute(qry1,data)
#         cur.execute(qry2)
#         upi = cur.fetchall()
#         con.commit()
        
#         return render_template('view.html',upi=upi)
#     except db.DatabaseError as e:
#         print(e)
#     con.close()
#     cur.close()
#     con.close()
# @app.errorhandler(HTTPException)
# def handle_exception(e):
#     if isinstance(e,HTTPException):
#         return e


    
        
        

             
