from flask import Flask

app = Flask(__name__)




@app.route('/')
def home():
    return "Hello, World!"

@app.route('/about')
def about():
    return "This is the about page."

from routes import *

if __name__ == '__main__':
    app.run(debug=True)