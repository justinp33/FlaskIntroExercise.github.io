from flask import Flask

app = Flask(__name__)

@app.route('/welcome')
def welcome():
    """Returns a message that says welcome"""

    return "Welcome"

@app.route('/welcome/home')
def welcome_home():
    """Returns a message that says welcome home"""

    return "Welcome home"

@app.route('/welcome/back')
def welcome_back():
    """Returns a message that says welcome back"""

    return "Welcome back"



