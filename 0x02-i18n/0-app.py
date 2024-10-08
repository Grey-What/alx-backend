#!/usr/bin/env python3
"""basic flask app with simple index route"""
from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def index_page():
    """simple main index route"""
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
