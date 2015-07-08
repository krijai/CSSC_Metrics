from flask import Flask,render_template,request
import sys, os

app = Flask(__name__)

@app.route("/")
def hello():
    print "Hello Heroku!"
