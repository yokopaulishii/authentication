import os

from flask import Flask, flash, redirect, render_template, request, session, url_for, abort
from helpers import get_users, hash_password

__winc_id__ = "8fd255f5fe5e40dcb1995184eaa26116"
__human_name__ = "authentication"

app = Flask(__name__)

app.secret_key = os.urandom(16)


@app.route("/home")
def redirect_index():
    return redirect(url_for("index"))


@app.route("/")
def index():
    return render_template("index.html", title="Index")


@app.route("/about")
def about():
    return render_template("about.html", title="About")


@app.route("/lon")
def lon():
    return render_template("lon.html", title="League of Nations")

def helpers(get_users, hash_password):
    return helpers.get_users(), helpers.hash_password()

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == ['GET']:
        request.form['hash_password'] == 'hash_password' 
    if request.method == ['POST']:
        request.form['get_users'] =='admin'
        session['logged-in']=True
    else:
        flash('wrong password!')
        return redirect('/login?error=True')
    return redirect('/dashboard')


@app.route('/dashboard', methods=['GET'])
def dashboard():
    if request.method ==['GET']: 
        return dashboard.html
    
@app.route("/logout", methods=["GET", "POST"])
def logout():
    session['logged-in']=False
    return redirect('/')

