from app import app
from flask import render_template

@app.route('/users')
def users():
    return render_template('users.html')

