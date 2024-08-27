#!/usr/bin/env python3
"""
This is an example app for the 0x02-i18n project.
"""
from flask import Flask, render_template, request, g
from flask_babel import Babel


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


class Config(object):
    """config class"""
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
babel = Babel(app)
app.config.from_object(Config)


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


@babel.localeselector
def get_locale():
    """get locale and return it"""
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale

    if g.user['locale'] in app.config['LANGUAGES']:
        return g.user['locale']

    locale_header = request.headers.get('locale', None)
    if locale_header in app.config['LANGUAGES']:
        return locale_header

    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/', strict_slashes=False)
def index():
    """simple main index route"""
    return render_template('6-index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
