#!/usr/bin/env python3
"""
Use the _ or gettext function
"""

from flask import Flask, render_template, request
from flask_babel import Babel, _

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


@app.route('/', methods=['GET'], strict_slashes=False)
def hello_world() -> str:
    """
    render template and parametrize your templates
     Use the message IDs home_title and home_header
    """
    return render_template('4-index.html')


@babel.localeselector
def get_locale() -> str:
    """
    Get locale
    detect if the incoming request contains locale argument
    and ifs value is a supported locale, return it.
    If not or if the parameter is not present,
    resort to the previous default behavior.
    """
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


if __name__ == "__main__":
    app.run(debug=True)
