from app import app, db
from flask import request, render_template,redirect, url_for
import json
from app.models import *

@app.route("/",methods=["GET","POST"])
@app.route("/index", methods=["GET","POST"])
def index():
    return render_template("index.html")

@app.route("/bio",methods=["GET","POST"])
def bio():
    return render_template("bio.html")

@app.route("/contact", methods=["GET","POST"])
@app.route("/contact-us",methods=["GET","POST"])
def contact():
    return render_template("contact.html")

@app.route("/blog", methods=["GET", "POST"])
def blog():
    return render_template("blog.html")
# Postgres documentation for Python: https://github.com/EricSchles/postgres_flask_macosx
