#!/usr/bin/env python3
"""
This is an example app for the 0x02-i18n project.
"""
from flask import Flask, render_template, request
from flask_babel import Babel


class Config(object):
    """config class"""
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
babel = Babel(app)
app.config.from_object(Config)


@babel.localeselector
def get_locale():
    """get locale"""
    if (request.args.get('locale')
       and request.args.get('locale') in app.config['LANGUAGES']):
        return request.args.get('locale')
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/', strict_slashes=False)
def index():
    """simple main index route"""
    return render_template('4-index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000", debug=True)
