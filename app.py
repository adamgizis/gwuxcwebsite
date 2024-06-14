from flask import Flask, session, render_template, redirect, url_for, request

app = Flask('app')

app.secret_key = "SECRET"

@app.route('/')
def hello_world():
    return redirect('/home')

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/dues')
def dues():
    return render_template('dues.html')

@app.route('/eboard')
def eboard():
    return render_template('eboard.html')

@app.route('/records')
def records():
    return render_template('records.html')

@app.route('/routes')
def routes():
    return render_template('routes.html')

app.run(host='0.0.0.0', port=8080, debug=True)