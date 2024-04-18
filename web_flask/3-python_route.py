#!/usr/bin/python3
""" Starts a Flask web application """


from flask import Flask

app = Flask(__name__)


# Define the route for the root url '/'
@app.route('/', strict_slashes=False)
def hello_hbnb():
    """ Return 'Hello HBNB! """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def display_hbnb():
    """ Return HBNB """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def display_c_with_text(text):
    """ Displays 'C' followed by the value of <text> given """
    # Replace underscores with spaces in <text>
    formatted_text = text.replace('_', ' ')
    return "C {}".format(formatted_text)


@app.route('/python/<text>', strict_slashes=False)
def display_python_with_text(text='is cool'):
    """ Displays 'Python' followed by the value of <text> given """
    # Replace underscores with spaces in <text>
    formatted_text = text.replace('_', ' ')
    return "Python {}".format(formatted_text)


if __name__ == "__main__":
    # Start the Flask development server
    # Listen on all available networj interfaces (0.0.0.0) and port 5000
    app.run(host='0.0.0.0', port=5000)
