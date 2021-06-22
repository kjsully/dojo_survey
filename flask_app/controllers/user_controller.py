from flask import render_template, redirect, request, session

from flask_app import app
from ..models.user import User

@app.route('/')
def index():
    return render_template("index.html")



@app.route('/result', methods=['POST'])
def users():
    if not User.validate_user(request.form):
        return redirect('/')
        

    print('Got Post Info')
    print(request.form)
    name = request.form['name']
    location = request.form['location']
    language = request.form['language']
    comments = request.form['comments']

    return render_template(
        'success.html',
    name = request.form['name'],
    location = request.form['location'],
    language = request.form['language'],
    comments = request.form['comments']
    )
