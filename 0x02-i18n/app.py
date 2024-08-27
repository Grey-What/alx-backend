#!/usr/bin/env python3
"""
This is an example app for the 0x02-i18n project.
"""
from flask import Flask, render_template, request, g
from flask_babel import Babel
from pytz import timezone
import pytz.exceptions
from datetime import datetime
import locale


class Config(object):
    """config class"""
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
babel = Babel(app)
app.config.from_object(Config)


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user():
    """return user dictionary else None"""
    if request.args.get('login_as'):
        return users.get(int(request.args.get('login_as')))
    return None


@app.before_request
def before_request() -> None:
    """get user and set global user"""
    user = get_user()
    g.user = user

    cur_time = pytz.utc.localize(datetime.utcnow())
    time = cur_time.astimezone(timezone(get_timezone()))
    locale.setlocale(locale.LC_TIME, (get_locale(), 'UTF-8'))
    g.time = time.strftime("%b %d, %Y %I:%M:%S %p")


@babel.timezoneselector
def get_timezone():
    """get timezone and return it"""
    time_zone = request.args.get('timezone')
    if time_zone:
        try:
            return timezone(time_zone).zone
        except pytz.exceptions.UnknownTimeZoneError:
            pass

    if g.user:
        try:
            time_zone = g.user.get('timezone')
            return timezone(time_zone).zone
        except pytz.exceptions.UnknownTimeZoneError:
            pass

    default_timezone = app.config['BABEL_DEFAULT_TIMEZONE']
    return default_timezone


@babel.localeselector
def get_locale():
    """get locale and return it"""
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale

    if g.user and g.user['locale'] in app.config['LANGUAGES']:
        return g.user['locale']

    locale_header = request.headers.get('locale', None)
    if locale_header in app.config['LANGUAGES']:
        return locale_header

    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/', strict_slashes=False)
def index():
    """simple main index route"""
    return render_template('index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
