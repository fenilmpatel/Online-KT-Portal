from urllib import response
from flask import Flask,render_template,url_for,request
from werkzeug.exceptions import HTTPException
import psycopg2 as db
from database import table,tbl_con

#initialize flask app
app = Flask(__name__)
con,cur = tbl_con() 


#Set home page
@app.route('/')
def home():
    return render_template('index1.html',title='Home')

@app.route('/insert',methods=['POST'])
def insert():
    try:
        Emp_Id = request.form['Emp_Id']
        Name = request.form['Name']
        Project  = request.form['Project']
        Query = request.form['Query']
        data = (Emp_Id,Name,Project,Query)
        Qry  = "INSERT INTO employee(Emp_id,Name,Project,Query) VALUES (%s,%s,%s,%s)"
        #insert data to table
        cur.execute(Qry,data)
        return "data inserted successfully.."
    
    except db.Error as e:

        print(e)
    con.commit()    
    cur.close()
    con.close()
@app.route('/view',methods=['GET'])
def view():
    try:
    
        #create a connection to database
        con,cur = tbl_con()
              
        #create a new table
        cur.execute("SELECT * FROM employee")
        data = cur.fetchall()
    except db.DatabaseError as e:
        print(e)
    con.close()
    cur.close()
    con.close()
    return render_template('prediction.html',data=data)        
@app.errorhandler(HTTPException)
def handle_exception(e):
    if isinstance(e,HTTPException):
        return e
    

    
        
        

             
