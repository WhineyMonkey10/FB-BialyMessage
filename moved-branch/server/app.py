import flask
from flask import request, render_template, url_for, redirect, session
from bundle import Application

app = flask.Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        return render_template('home.html')
    return render_template('home.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == 'admin' and password == 'admin':
            return redirect(url_for('chat'))
    return render_template('home.html')


@app.route('/chat', methods=['GET', 'POST'])
def chat():
    return render_template('chat.html')


@app.route('/getMessages', methods=['GET', 'POST'])
def getMessages():
    if request.method == 'POST' or request.method == 'GET':
            render_template('chat.html', messages=Application.readMessages()) 
    return render_template('chat.html')

app.run(host='0.0.0.0', port=5000, debug=True)