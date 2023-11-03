#!/usr/bin/env python3
"""
A Flask app with Babel i18n configuration, user login emulation, and
support for preferred locale selection.
"""
from flask import Flask, render_template, request, g
from flask_babel import Babel
from typing import Union, Dict

app = Flask(__name__)
babel = Babel(app)


class Config:
    """
    Configuration class for the Flask app and Babel extension.

    Attributes:
        LANGUAGES (list): A list of available languages.
        BABEL_DEFAULT_LOCALE (str): The default locale.
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"

app.config.from_object(Config)
app.url_map.strict_slashes = False

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user(user_id) -> Union[Dict, None]:
    """Retrieve a user from the mock user database.
    Args:
        user_id (int): The ID of the user to retrieve.
    Returns:
        dict: A user dictionary or None if the user is not found.
    """
    return users.get(user_id)


@babel.localeselector
def get_locale() -> str:
    """
    Determine the best-matching language for the user based on their preferences.

    The order of priority is as follows:
    1. Locale from URL parameters
    2. Locale from user settings
    3. Locale from request header
    4. Default locale

    Returns:
        str: The best-matching language code (e.g., "en" for English).
    """
    # Check if 'locale' parameter is present in the request URL
    selected_locale = request.args.get('locale')
    
    if selected_locale in app.config['LANGUAGES']:
        # If 'locale' parameter is a supported locale, use it
        return selected_locale

    # Check if a user is logged in
    if 'user' in g:
        user_locale = g.user.get('locale', None)
        if user_locale in app.config['LANGUAGES']:
            # If user has a preferred locale, use it
            return user_locale

    # If no preferred locale is found in URL or user settings, use request header
    header_locale = request.accept_languages.best_match(app.config['LANGUAGES'])
    
    if header_locale:
        return header_locale

    # If no supported locale is found in the request, use the default locale
    return app.config['BABEL_DEFAULT_LOCALE']


@app.before_request
def before_request() -> None:
    """
    Executed before all other functions to find and set the user, if any.
    """
    user_id = request.args.get('login_as', type=int)
    if user_id in users:
        g.user = users[user_id]
    else:
        g.user = None


@app.route('/')
def home():
    """
    Render the home page with Babel-supported internationalization.

    Returns:
        str: Rendered HTML page with translated content.
    """
    return render_template('6-index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
