#!/usr/bin/env python3
"""
A Flask app with Babel i18n configuration.
"""
from flask import Flask, render_template, request
# Import the `_` function for translations
from flask_babel import Babel, _

app = Flask(__name__)
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


app.config.from_object(Config)
app.url_map.strict_slashes = False


@babel.localeselector
def get_locale() -> str:
    """
    Determine the best-matching language for the user based
    on their accepted languages and the available languages
    configured in the app.

    Returns:
        str: The best-matching language code (e.g., "en" for English).
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def home():
    """
    Render the home page with Babel-supported internationalization.

    Returns:
        str: Rendered HTML page with translated content.
    """
    return render_template('3-index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
