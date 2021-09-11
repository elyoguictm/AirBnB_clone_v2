#!/usr/bin/python3
"""Script that starts flask web app"""
from flask import Flask, render_template
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
    repla = text.replace('_', ' ')
    return 'Python {}' .format(repla)


@app.route('/number/<int:n>')
def ints(n):
    """display int"""
    return '{} is a number'.format(n)


@app.route('/number_template/<int:n>')
def numhtml(n):
    """display html web application"""
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>')
def even_or_odd(n):
    """displays html even or odd"""
    return render_template('6-number_odd_or_even.html', n=n)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
