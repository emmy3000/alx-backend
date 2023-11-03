#!/usr/bin/env python3
"""
A Flask app with Babel i18n configuration, user-based locale
and timezone preferences.
"""
import pytz
from flask import Flask, render_template, request, g
from flask_babel import Babel
from typing import Dict, Union

app = Flask(__name__)
babel = Babel(app)

# Mock user data
users = {
    1: {"name": "Alice", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Bob", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Charlie", "locale": "de", "timezone": "Europe/Berlin"},
}


@app.before_request
def set_user() -> Union[Dict, None]:
    """
    Set the user based on the 'login_as' parameter in the request.
    """
    user_id = request.args.get('login_as')
    g.user = users.get(int(user_id)) if user_id and int(
        user_id) in users else None


@babel.localeselector
def get_locale() -> str:
    """
    Determine the best-matching language for the user based
    on URL parameters, user settings, request header,
    or default to accept languages.
    """
    tz_param = request.args.get('locale')
    if tz_param:
        if tz_param in app.config['LANGUAGES']:
            return tz_param

    if g.user and 'locale' in g.user:
        if g.user['locale'] in app.config['LANGUAGES']:
            return g.user['locale']

    header_locale = request.headers.get('locale')
    if header_locale:
        if header_locale in app.config['LANGUAGES']:
            return header_locale

    return request.accept_languages.best_match(app.config['LANGUAGES'])


@babel.timezoneselector
def get_timezone() -> str:
    """
    Determine the user's preferred timezone based on URL parameters,
    user settings, or default to UTC if not specified or invalid.
    """
    tz_param = request.args.get('timezone')
    if tz_param:
        try:
            pytz.timezone(tz_param)
            return tz_param
        except pytz.exceptions.UnknownTimeZoneError:
            pass

    if g.user and 'timezone' in g.user:
        try:
            pytz.timezone(g.user['timezone'])
            return g.user['timezone']
        except pytz.exceptions.UnknownTimeZoneError:
            pass

    return 'UTC'


@app.route('/')
def index():
    """
    Render the home page with user-specific locale
    and timezone preferences.
    """
    return render_template('7-index.html', user=g.user)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
