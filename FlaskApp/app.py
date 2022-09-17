#!/usr/bin/env python3

from flask import Flask
from flask import render_template

import os
import ast

app = Flask(__name__)

from dotenv import load_dotenv

load_dotenv()

FLASK_PUBLIC = ast.literal_eval(os.getenv('FLASK_PUBLIC'))
PUBLIC_HOST = "0.0.0.0"

@app.route("/")
def hello_world():
	return "<p>Hello, World!</p>"

@app.route("/index")
def index(name=None):
	return render_template("index.html", name=name)

if __name__ == "__main__":
	host = PUBLIC_HOST if FLASK_PUBLIC else None
	app.run(debug=True, host=host)
