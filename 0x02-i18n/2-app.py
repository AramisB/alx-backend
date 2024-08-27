#!/usr/bin/env python3
"""
get_locale function with the babel.localeselector decorator. Use request.accept_languages to determine the best match with our supported languages.
"""

from flask import Flask, render_template, request
from flask_babel import Babel

app_flask = Flask(__name__)
babel = Babel(app_flask)


class Config:
    """
    Config class
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app_flask.config.from_object(Config)


@babel.localeselector
def get_locale():
    """
    Get locale
    """
    return request.accept_languages.best_match(app_flask.config["LANGUAGES"])


@app_flask.route('/')
def index():
    """
    render template
    """
    return render_template('2-index.html')


if __name__ == "__main__":
    app_flask.run(debug=True)
