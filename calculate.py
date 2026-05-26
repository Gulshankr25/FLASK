from flask import Flask, render_template, request
app=Flask(__name__)

@app.route("/")
def calculate():
    return render_template("mainpage.html")

@app.route("/addition")
def addition():
    return render_template("calculate.html")

@app.route("/addresult", methods=["post"])
def addresult():
    a = int(request.form['txtNumber'])
    b = int(request.form['txtNumber'])
    add = a+b
    return "sum of a and b is "+add

@app.route("/subtraction")
def subtraction():
    return render_template("sub.html")

@app.route("/subresult", methods=["post"])
def subresult():
    a = int(request.form['txtNumber1'])
    b = int(request.form['txtNumber2'])
    sub = a-b
    return "sum of a and b is "+sub

@app.route("/multiplition")
def multiplition():
    return render_template("mult.html")

@app.route("/multresult", methods=["post"])
def multresult():
    a = int(request.form['txtNumber1'])
    b = int(request.form['txtNumber2'])
    mult = a*b
    return "sum of a and b is "+mult

@app.route("/division")
def division():
    return render_template("divide.html")

@app.route("/divresult", methods=["post"])
def divresult():
    a = int(request.form['txtNumber1'])
    b = int(request.form['txtNumber2'])
    div = a/b
    return "sum of a and b is "+div


app.run(debug=True)