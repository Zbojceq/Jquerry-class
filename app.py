from flask import Flask
app = Flask(__name__)
    

@app.route('/')
def hello_world():
    return 'Hello, Ernest!'

from flask import Flask, render_template
@app.route('/about/<name>')
def hello(name):
    return render_template('about.html', name=name)


from flask import Flask, render_template, request
@app.route('/method', methods=['GET', 'POST'])
def method():
    if request.method == 'POST':
        return 'Użyto metody POST'
    else:
        return 'Użyto metody GET. '
    
@app.route('/hello/<name>')
def hello_name(name):
    return f'Witaj, {name}!'

@app.route('/<number>')
def number_check(number):
    if int(number) % 2 == 0:
        return f'Liczba podzielna przez 2'
    if int(number) % 3 == 0:
        return f'Liczba podzielna przez 3'
    if int(number) % 5 == 0:
        return f'Liczba podzielna przez 5'
