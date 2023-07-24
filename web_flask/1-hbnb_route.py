#!/usr/bin/python3
"""Flask web application
Listens on 0.0.0.0, port 5000
The Route:
    /: Print 'Hello HBNB!'.
    /hbnb: Print 'HBNB'.
"""
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """Prints 'Hello HBNB!'"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Prints 'HBNB'"""
    return "HBNB"


if __name__ == "__main__":
    app.run(host="0.0.0.0")
