from flask import Flask, render_template, request, flash, redirect, url_for
from forms import AppForm
import os

app = Flask(__name__)

# CSRF Protection
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY

app.config['DEBUG'] = True

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/forms', methods=['GET', 'POST'])
def forms():
    form = AppForm()
    if (form.validate_on_submit() and request.method == 'POST'):
        return render_template('confirmation.html', form = request.form)
    return render_template('form.html', form = form)

@app.route('/confirmation', methods=['GET', 'POST'])
def confirmation():
    return render_template('confirmation.html')

@app.route('/iframe')
def iframe():
    return render_template('iframe.html')