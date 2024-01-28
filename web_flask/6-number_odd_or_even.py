#!/usr/bin/python3


"""
importing Flask
"""


from flask import Flask, abort, render_template
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


@app.route('/number_template/<int:n>', strict_slashes=False)
def num_template(n):
    """
    Display HTML page if n is an integer
    """
    return render_template('5-number.html', num=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
    """
    Display a HTML page with 'Number: n is even|odd' inside the tag BODY
    """
    return render_template('6-number_odd_or_even.html', n=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
