from flask import Flask , render_template

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello, World!'

@app.route('/welcome')
def hello1():
    return 'Welcome to PFSD class SEC:11!'

@app.route('/emp/<int:emp1>')
def show(emp1):
    return 'Employee ID Number %d'%emp1

@app.route('/emp/<float:emp1>')
def show1(emp1):
    return 'Employee ID Number %f'%emp1

@app.route('/ex1')
def index():
    return render_template('hello.html')

if __name__ == "main":
    app.run(debug=True)