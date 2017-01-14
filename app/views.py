from app import app, db
from flask import request, render_template,redirect, url_for
import json
from app.models import *

@app.route("/",methods=["GET","POST"])
def index():
    if request.method=="POST":
        username = request.form.get("username")
    return render_template("index.html")

@app.route("/splash",methods=["GET","POST"])
def splash():
    return render_template("index2.html")

@app.route("/sign-in",methods=["GET","POST"])
def sign_in():
    return render_template("sign_in.html")

@app.route("/sign-up",methods=["GET","POST"])
def sign_up():
    return render_template("sign_up.html")

# Postgres documentation for Python: https://github.com/EricSchles/postgres_flask_macosx
