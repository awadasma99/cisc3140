from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def main():
    d = "a string"
    d = 123
    d = "is really a string"
    return d
    # return 'Hello, World!'

@app.route('/hello')
def index(imagename='giphy.webp'):
    # return 'Hello World'
    return render_template('hello.html', name=imagename)

@app.route('/hello/today')
def today():
    return 'today'
