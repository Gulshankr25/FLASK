from flask import Flask, render_template, request
from flask_mysqldb import MySQL

app = Flask(__name__)

app.secret_key= 'gulshan123'
app.config['MYSQL_HOST']= 'localhost'
app.config['MYSQL_USER']= 'root'
app.config['MYSQL_PASSWORD']= ''
app.config['MYSQL_DB']= 'real_project_db'

mysql = MySQL(app)

# @app.route('/')
# def header():
#     return render_template('realhome.html')

@app.route('/')
def realhome():
    return render_template('realhome.html')

@app.route('/contact')
def contact():
    return render_template('realcontact.html')

@app.route('/about')
def aboutus():
    return render_template('realabout.html')

@app.route('/admin')
def admin():
    return render_template('realadmin.html')

@app.route('/successlogin', methods=['post'])
def successlogin():

    u = request.form['txtUsername']
    p = request.form['txtPassword']

    if(u=="admin" and p=="admin"):
        return render_template('admin_dashboard.html')
    else:
        msg = "Invalide Username or Password"
        # return "Invalide username or password"
        return render_template('realadmin.html', message = msg)



@app.route('/admin_addemp')
def admin_addemp():
    return render_template('admin_addemp.html')

@app.route('/emp_added', methods=['post'])
def emp_added():
    i = request.form['txtEmpID']
    n = request.form['txtName']
    e = request.form['txtEmail']
    p = request.form['txtPhone']

    cur = mysql.connection.cursor()
    cur.execute('insert into addemp(empid,name,email,phone) values(%s,%s,%s,%s)',(i,n,e,p))
    mysql.connection.commit()
    cur.close()

    return 'employee added successfully'


@app.route('/admin_showemp')
def admin_showemp():

    cur = mysql.connection.cursor()
    cur.execute('select empid,name,email,phone from addemp')
    emplist = cur.fetchall()

    return render_template('admin_showemp.html', recordlist = emplist)

@app.route('/admin_login')
def adminlogout():
    return 'logout succeessfully'

@app.route('/admin_emp_profile')
def admin_empprofile():
    
    id = request.args.get('empid')
    cur = mysql.connection.cursor()
    cur.execute('select * from addemp where empid='+id)
    emplist = cur.fetchall()

    return render_template('admin_emp_profile.html',recordlist = emplist)

@app.route('/emp_updated', methods=['post'])
def emp_update():
    i = request.form['txtEmpID']
    n = request.form['txtName']
    e = request.form['txtEmail']
    p = request.form['txtPhone']

    cur = mysql.connection.cursor()
    cur.execute ( 'update addemp set name=%s, phone=%s, email=%s where empid=%s',(n,p,e,i,))
    mysql.connection.commit()
    cur.close()
    
    return 'employee updated successfully'

@app.route('/emp_delete', methods=['post'])
def emp_delete():

    i = request.form['txtEmpID']

    cur = mysql.connection.cursor()
    cur.execute('delete from addemp where empid=%s',(i,))
    mysql.connection.commit()
    cur.close()

    return 'employee deleted successfully'

@app.route('/admin_search')
def admin_search():
    return render_template('admin_search.html')

@app.route('/admin_search_result',methods=['post'])
def admin_search_result():

    n = request.form['txtName']
    print(n)

    cur = mysql.connection.cursor()
    cur.execute("select * from addemp where name like '"+n+"%'")
    emplist = cur.fetchall()

    return render_template('admin_search_result.html',recordlist = emplist)



app.run(debug=True)















