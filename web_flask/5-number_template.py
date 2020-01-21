#!/usr/bin/python3
from flask import Flask, escape, render_template

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


@app.route('/number/<int:n>')
def show_number(n):
    return "{} is a number".format(n)


@app.route('/number_template/<int:n>')
def template(n):
    return render_template('5-number.html', name=n)

if __name__ == "__main__":
    app.run(debug=True)
