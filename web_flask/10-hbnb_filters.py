#!/usr/bin/python3
""" This script starts a Flask web application."""


from flask import Flask, render_template
from models import storage


app = Flask(__name__)


@app.route('/hbnb_filters', strict_slashes=False)
def hbnb_filters():
    """this function returns a message when /hbnb_filters is requested."""
    states = storage.all('State').values()
    states = sorted(states, key=lambda state: state.name)
    amenities = storage.all('Amenity').values()
    amenities = sorted(amenities, key=lambda amenity: amenity.name)
    return render_template('10-hbnb_filters.html',
                           states=states, amenities=amenities)


@app.teardown_appcontext
def teardown_db(exception):
    """ This function removes the current SQLAlchemy session."""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
