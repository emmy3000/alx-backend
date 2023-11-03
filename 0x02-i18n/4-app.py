#!/usr/bin/env python3
"""
A Flask app with Babel i18n configuration and support
for locale parameter.
"""
from flask import Flask, render_template, request
from flask_babel import Babel

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
    Determine the best-matching language for the user based on their
    accepted languages, the available languages configured in the app,
    and the 'locale' parameter in the request.

    Returns:
        str: The best-matching language code (e.g., "en" for English).
    """
    # Check if 'locale' parameter is present in the request
    selected_locale = request.args.get('locale')

    if selected_locale in app.config['LANGUAGES']:
        # If 'locale' parameter is a supported locale, use it
        return selected_locale

    # Otherwise, use the best-matching language from request.accept_lang
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def home():
    """
    Render the home page with Babel-supported internationalization.

    Returns:
        str: Rendered HTML page with translated content.
    """
    return render_template('4-index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
