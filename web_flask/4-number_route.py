#!/usr/bin/python3
""" Flask web app
Listens on 0.0.0.0, port 5000.
Routes:
 /: Prints 'Hello HBNB!'.
 hbnb: Prints 'HBNB'.
c/<text>: Displays 'C' followed by the value of <text>.
print python
"""
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """Prints 'Hello HBNB!'."""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Prints 'HBNB'."""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c(text):
    """Prints 'C' followed by text"""
    text = text.replace("_", " ")
    return "C {}".format(text)


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python(text="is cool"):
    """Displays 'Python' and text
    """
    text = text.replace("_", " ")
    return "Python {}".format(text)


@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    """Prints if n is int"""
    return "{} is a number".format(n)


if __name__ == "__main__":
    app.run(host="0.0.0.0")
