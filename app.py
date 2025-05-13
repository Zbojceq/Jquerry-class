from flask import Flask
app = Flask(__name__)
    

@app.route('/')
def hello_world():
    return 'Hello, Ernest!'


@app.route('/method', methods=['GET', 'POST'])
def method():
    if request.method == 'POST':
        return 'Użyto metody POST'
    else:
        return 'Użyto metody GET. '
    
@app.route('/hello/<name>')
def hello_name(name):
    return f'Witaj, {name}!'