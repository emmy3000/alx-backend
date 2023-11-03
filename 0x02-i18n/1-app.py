#!/usr/bin/env python3
"""
A Flask app with Babel i18n configuration.
"""
from flask import Flask, render_template
from flask_babel import Babel

app = Flask(__name)
babel = Babel(app)


class Config:
    """
    Configuration class for the Flask app and Babel extension.

    Attributes:
        LANGUAGES (list): A list of available languages.
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


babel.init_app(app)
app.config.from_object(Config)
app.url_map.strict_slashes = False
babel = Babel(app)


@app.route('/')
def index():
    """
    Render the home page with Babel-supported internationalization.

    Returns:
        str: Rendered HTML page.
    """
    return render_template('1-index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
