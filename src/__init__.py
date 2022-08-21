from flask import Flask, render_template


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/mens')
def mens():
    return render_template('mens.html')

@app.route('/womens')
def womens():
    return render_template('womens.html')
