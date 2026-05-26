from flask import Flask, render_template, request
app=Flask(__name__)

@app.route("/")
def main():
    return render_template("main.html")

@app.route("/add")
def add():
    return render_template("add.html")

@app.route("/result", methods=['post'])
def result():
    a = int(request.form['txtFirst'])
    b = int(request.form['txtSecond'])
    add = a+b
    return render_template("result.html", result = add)

@app.route('/count')
def count():
    return render_template('condition.html')

@app.route('/marks')
def marks():
    return render_template('marks.html')

@app.route('/show_result',methods=["post"])
def show_result():
    m = int(request.form['txtMarks'])
    # if(m>=35):
    #     status = 'Student is passed'
    # else:
    #     status='student is failed'
    return render_template('std_result.html',result= m)


app.run(debug=True)