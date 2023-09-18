from flask import Flask
app = Flask(__name__)

# example 2-1
@app.route('/')
def index():
    return '<h1>Hello World!</h1>'

app.add_url_rule('/', 'index', index)

# example 2-2 
@app.route('/user/<name>')
def user(name):
    return '<h1>Hello, {}!</h1>'.format(name)