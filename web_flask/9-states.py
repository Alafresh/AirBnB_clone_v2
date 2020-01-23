#!/usr/bin/python3
from flask import Flask, escape, render_template
from models import storage
from models.state import State
from models.city import City

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.teardown_appcontext
def teardown_db(zzz):
    storage.close()


@app.route('/states')
@app.route('/states/<id>')
def display(id=None):
    states = storage.all('State')
    return render_template('9-states.html', states=states, id=id)

if __name__ == "__main__":
    app.run(debug=True)
