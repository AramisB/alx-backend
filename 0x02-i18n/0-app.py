#!/usr/bin/env python3
"""
 a single / route
"""
from flask import Flask, render_template

app_flask = Flask(__name__, template_folder='templates')


@app_flask.route('/', methods=['GET'], strict_slashes=False)
def hello_world() -> str:
    """
    Render template for Babel usage.
    """
    return render_template('0-index.html')


if __name__ == "__main__":
    app_flask.run(debug=True)
