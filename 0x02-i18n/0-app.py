#!/usr/bin/env python3
"""
 a single / route
"""
from flask import Flask, render_template

app_flask = Flask(__name__)


@app_flask.route('/')
def index():
    return render_template('0-index.html')


if __name__ == "__main__":
    app_flask.run(debug=True)
