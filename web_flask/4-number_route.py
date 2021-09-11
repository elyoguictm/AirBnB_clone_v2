#!/usr/bin/python3
"""Script that starts flask web app"""
from flask import Flask
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def suphbnb():
    """Display Hello HBNB!"""
    return 'Hello HBNB!'


@app.route('/hbnb')
def hbnb():
    """Display HBNB!"""
    return 'HBNB!'


@app.route('/c//<text>')
def cisfun(text):
    """display c"""
    return ("C {}".format(text.replace('_', ' ')))


@app.route('/python')
@app.route('/python/<text>')
def python(text="is cool"):
    """Display python follow by the text"""
    return 'Python {}' .format(text.replace('_', ' '))


@app.route('/number/<int:n>')
def ints(n):
    """display int"""
    return '{} is a number'.format(n)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
