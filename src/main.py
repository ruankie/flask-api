from flask import Flask
from utilities import greet_name

app = Flask(__name__)

@app.route('/helloworld')
def index():
    return {'Message': 'Hello World'}

@app.route('/hello/<name>')
def greet_with_name(name):
    return {'Message': greet_name(name)}

if __name__ == "__main__":
    app.run(debug=True)