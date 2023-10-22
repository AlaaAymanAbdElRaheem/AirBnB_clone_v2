#!/usr/bin/python3
""" This script starts a Flask web application."""


from flask import Flask, render_template
from models import storage


app = Flask(__name__)


@app.route('/states', strict_slashes=False)
def states_list():
    """ This function returns a message when /states_list is requested."""
    states = storage.all('State').values()
    states = sorted(states, key=lambda state: state.name)
    return render_template('9-states.html', states=states)


@app.route('/states/<id>', strict_slashes=False)
def states_id(id):
    """ This function returns a message when /states_list is requested."""
    states = storage.all('State')
    state_id = "State." + id
    if state_id in states.keys():
        return render_template('9-states.html', state=states[state_id], id=id)
    else:
        return render_template('9-states.html', not_found=True)


@app.teardown_appcontext
def teardown_db(exception):
    """ This function removes the current SQLAlchemy session."""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
