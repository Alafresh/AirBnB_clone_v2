#!/usr/bin/python3
from flask import Flask, escape

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello():
    return "Hello HBNB!"


@app.route('/hbnb')
def hbnb():
    return 'HBNB'


@app.route('/c/<text>')
def show_text(text):
    text = text.replace('_', ' ')
    return 'C %s' % text


@app.route('/python', defaults={'text': 'is cool'})
@app.route('/python/<text>')
def show_python(text):
    text = text.replace('_', ' ')
    return 'Python %s' % text

if __name__ == "__main__":
    app.run(debug=True)
