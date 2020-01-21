#!/usr/bin/python3
from flask import Flask, escape, render_template
from models import storage
from models.state import State

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.teardown_appcontext
def teardown_db(zzz):
    storage.close()


@app.route('/states_list')
def display():
    state = storage.all()
    return render_template('7-states_list.html', state=state)

if __name__ == "__main__":
    app.run(debug=True)
