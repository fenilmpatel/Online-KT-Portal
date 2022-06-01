from flask import Flask,render_template,url_for,request
import database


#initialize flask app
app = Flask(__name__)
con,cur = database.tbl_con() 


#Set home page
@app.route('/')
def home():
    return render_template('index1.html',title='Home')

@app.route('/insert',methods=['POST'])
# def predict():
    # '''For rendering results on HTML GUI
    # '''
    # Emp_Id = request.form['Emp_Id']
    # Name = request.form['Name']
    # Project  = request.form['Project']
    # contact = request.form['Query']
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
    finally:
        con.commit()
        cur.close()
        con.close()
        
             
