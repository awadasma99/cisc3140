from flask import Flask
from flask import render_template
from nasa import connect, test_connect  # explicit imports from nasa.py 

app = Flask(__name__)

@app.route('/')
def home():
    data = connect()
    return render_template('page.html', content=data)

@app.route('/<date>')
def today(date):
    data = connect(date=date)
    return render_template('page.html', content=data)

if __name__ == '__main__':
    # This is used when running locally. Gunicorn is used to run the
    # application on Google App Engine. See entrypoint in app.yaml.
    app.run(host='127.0.0.1', port=8080, debug=True)
