from app import app, db
from flask import request, render_template,redirect, url_for
import json
from app.models import *

@app.route("/",methods=["GET","POST"])
@app.route("/index", methods=["GET","POST"])
def index():
    return render_template("index.html")

@app.route("/for_students",methods=["GET","POST"])
def for_students():
    return render_template("for_students.html")

@app.route("/contact", methods=["GET","POST"])
@app.route("/contact-us",methods=["GET","POST"])
def contact():
    return render_template("contact.html")

@app.route("/blog", methods=["GET", "POST"])
def blog():
    return render_template("blog.html")

@app.route("/for-educators", methods=["GET", "POST"])
def for_educators():
    return render_template("for_educators.html")

@app.route("/for-journalists", methods=["GET", "POST"])
def for_journalists():
    return render_template("for_journalists.html")

@app.route("/services", methods=["GET", "POST"])
def services():
    return render_template("services.html")

@app.route("/in-the-news", methods=["GET", "POST"])
def in_the_news():
    return render_template("in_the_news.html")

@app.route("/journalist-fellows", methods=["GET", "POST"])
def journalist_fellows():
    return render_template("journalist_fellows.html")

@app.route("/we-are-hiring", methods=["GET", "POST"])
def we_are_hiring():
    return render_template("we_are_hiring.html")

@app.route("/news-literacy", methods=["GET","POST"])
def news_literacy():
    return render_template("news_literacy.html")

@app.route("/search-results", methods=["GET","POST"])
def search_results():
    return render_template("search_results.html")
# Postgres documentation for Python: https://github.com/EricSchles/postgres_flask_macosx
