from flask import Flask

port = 8080

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, World!'

app.run('localhost',port)