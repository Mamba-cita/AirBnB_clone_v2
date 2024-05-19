#!/usr/bin/python3
"""This script starts the Flask web application"""
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """
    Returns a string
    """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    Returns a string
    """
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """
    Returns C followed by the value of the text variable
    """
    return 'C {}'.format(text.replace('_', ' '))


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text):
    """
    displays "Python" followed by a text
    """
    return 'Python {}'.format(text.replace('_', ' '))


if __name__ == '__main__':
    """
    Ensures that the module is not executable when  imported
    """
    app.run(host='0.0.0.0', port=5000)
