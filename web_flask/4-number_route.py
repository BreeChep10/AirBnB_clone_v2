#!/usr/bin/python3


"""
importing Flask
"""


from flask import Flask, abort
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


@app.route('/python', strict_slashes=False)
@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text='is cool'):
    """
    Replace underscores with spaces in the text variable
    """
    return f'Python {text.replace("_", " ")}'


@app.route('/number/<n>', strict_slashes=False)
def is_number(n):
    """
    return statement
    """
    try:
        num = int(n)
        return f"{num} is a number"
    except ValueError:
        abort(404)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
