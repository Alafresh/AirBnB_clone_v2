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
if __name__ == "__main__":
    app.run(debug=True)
