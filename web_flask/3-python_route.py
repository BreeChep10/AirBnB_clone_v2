#!/usr/bin/python3


"""
importing Flask
"""


from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """
    return statement
    """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    return statements
    """
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """
    Replace underscores with spaces in the text variable
    """
    formatted_text = text.replace('_', ' ')
    return f'C {formatted_text}'


@app.route('/python/<text>', strict_slashes=False)
def python_text(text='is cool'):
    """
    Replace underscores with spaces in the text variable
    """
    return f'Python {text.replace("_", " ")}'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
