#!/usr/bin/env python
from flask import Flask
app = Flask(__name__)

@app.route('/')
@app.route('/hello/')

def hello_world():
    return 'Hello World! This is Project v0.3 Dockerizing Jenkins Pipeline\n'


@app.route('/hello/<username>') # dynamic route

def hello_user(username):
    return  '%s Is Dockerizing v0.3 Jenkins Pipeline\n' %username

if __name__ == '__main__':

    app.run(host='0.0.0.0')     # open for everyone
