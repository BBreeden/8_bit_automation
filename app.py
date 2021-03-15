from flask import Flask, render_template
from forms import AppForm
import os

app = Flask(__name__)

# CSRF Protection
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY

app.config["DEBUG"] = True

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/home')
def home():
    return render_template("home.html")

@app.route('/forms')
def forms():
    form = AppForm()
    return render_template("form.html", form = form)

@app.route('/confirmation')
def confirmation():
    return render_template("confirmation.html")