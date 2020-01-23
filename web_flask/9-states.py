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
def list_states():
    state = storage.all('State')
    return render_template('7-states_list.html', state=state)


@app.route('/states/<id>')
def display(id):
    states = storage.all('State')
    id_l = None
    for llave, valor in states.items():
        if valor.id == id:
            id_l = valor
            break
    return render_template('9-states.html', states=id_l)

if __name__ == "__main__":
    app.run(debug=True)
