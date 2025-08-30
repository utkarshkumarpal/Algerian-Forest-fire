from flask import Flask,jsonify,render_template
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler


experiment=Flask(__name__)
app=experiment


@app.route("/")
def hellow_world():
    return "<h1>Hello,World of 2025!</h1>"

@app.route("/about")
def about():
    return "<h2>This is about page!!</h2>"

@app.route("/html")
def html():
    return "<h1>Welcome<h1><p>This  is html page<p>"


@app.route("/user/<name>")
def user(name):
    return f"Hello, {name}!"


@app.route("/new_about")
def new_about():
    return "New About Page !"


@app.route("/ur_age/<age>")
def ur_age(age):
    return f"Your age is {age}"

@app.route("/hello/<name>")
def hello(name):
    return render_template("home.html", name=name)

@app.route("/usr2")
def usr2():
    return "<h1>Working fine</h1>"


@app.route("/bye/<name>")
def bye(name):
    return render_template("bye.html",name=name)

@app.route("/finale")
def finale():
    return "<h2>This was a finale check up ! Its working before GET POST part .<h2>"





if __name__ == "__main__":
    app.run(host="0.0.0.0")

