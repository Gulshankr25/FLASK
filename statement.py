from flask import Flask, request, render_template
app = Flask(__name__)

@app.route("/")
def condition():
    return render_template('main.html')

@app.route('/')
def count():
    return render_template('condition.html')

@app.route('/user/<username>')
def user(username):
    return 'user name is %s' % (username)

app.run(debug=True)