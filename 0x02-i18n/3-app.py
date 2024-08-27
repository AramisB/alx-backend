#!/usr/bin/env python3
"""
Use the _ or gettext function
"""

from flask import Flask, render_template, request
from flask_babel import Babel, _

app = Flask(__name__)
babel = Babel(app)


class Config:
    """
    Config class
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


@babel.localeselector
def get_locale():
    """
    Get locale
    """
    return request.accept_languages.best_match(app.config["LANGUAGES"])


@app.route('/')
def index():
    """
    render template and parametrize your templates
     Use the message IDs home_title and home_header
    """
    home_title = _("Welcome to Holberton")
    home_header = _("Hello world")
    return render_template('3-index.html', title=home_title, header=home_header)

if __name__ == "__main__":
    app.run(debug=True)
