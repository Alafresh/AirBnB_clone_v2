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


@app.route('/cities_by_states')
def display():
    state = storage.all('State')
    return render_template('8-cities_by_states.html', state=state)

if __name__ == "__main__":
    app.run(debug=True)
