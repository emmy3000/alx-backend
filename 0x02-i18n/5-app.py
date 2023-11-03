#!/usr/bin/env python3
"""
A Flask app with Babel i18n configuration and user login emulation.
"""
from flask import Flask, render_template, request, g
from flask_babel import Babel, gettext

app = Flask(__name__)
babel = Babel(app)

# Mock user database
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


class Config:
    """Configuration class for the Flask app and Babel extension.
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)
app.url_map.strict_slashes = False
babel = Babel(app)


def get_user(user_id):
    """Retrieve a user from the mock user database.
    Args:
        user_id (int): The ID of the user to retrieve.
    Returns:
        dict: A user dictionary or None if the user is not found.
    """
    return users.get(user_id)


@app.before_request
def before_request():
    """Execute before all other functions to find and set a user in flask.g.
    """
    user_id = request.args.get('login_as', type=int)
    g.user = get_user(user_id)


@app.route('/')
def home():
    """Render the home page with Babel-supported internationalization.
    Returns:
        str: Rendered HTML page with a welcome message or a default message.
    """
    return render_template('5-index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
