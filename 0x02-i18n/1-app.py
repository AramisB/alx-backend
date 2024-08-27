#!/usr/bin/env python3
"""
instantiate the Babel object in your app.
"""

from flask import Flask, render_template, request
from flask_babel import Babel

app = Flask(__name__, template_folder='templates')
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


@app.route('/', methods=['GET'], strict_slashes=False)
def hello_world() -> str:
    """
    render template
    """
    return render_template('1-index.html')


if __name__ == "__main__":
    app.run(debug=True)
