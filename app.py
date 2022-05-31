from flask import Flask,render_template,url_for,request
import os
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index1.html',title='Home')
import db
con,cur = db.tbl_con() 
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
        return "data inserted successfully.."
    finally:
        con.commit()
        cur.close()
        con.close()
        

    # pred = pd.DataFrame(data={'month':[float(month)],'emp.var.rate':[float(emp)] ,'cons.conf.idx':[float(cons)],'contact':[float(contact)],
    #                    'housing':[float(housing)],'euribor3m':[float(euribor3m)],'default': [float(default)]})
    # prediction = model.predict(pred)
    # output = prediction[0] 
    # if output > 0:
    #     output="Genuine"
    #     return render_template('prediction.html', prediction_text=f'Prediction For Applied Person is {output} Person.')
    # else:
    #     output = "Fraud"
    #     return render_template('prediction.html', prediction_text=f'Prediction For Applied Person is {output} Person!!')
# employee.insert()   
port = int(os.environ.get('PORT',5000))
if __name__ == "__main__":
    app.run(debug=1,host='0.0.0.0',port=port) # or True             
