#!/usr/bin/python3
""" This script starts a Flask web application."""


from flask import Flask, render_template
from models import storage


app = Flask(__name__)


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """this function returns a message when /hbnb is requested."""
    states = storage.all('State').values()
    states = sorted(states, key=lambda state: state.name)
    amenities = storage.all('Amenity').values()
    amenities = sorted(amenities, key=lambda amenity: amenity.name)
    users = storage.all('User').values()
    users = sorted(users, key=lambda user: user.first_name)
    return render_template('100-hbnb.html',
                           states=states, amenities=amenities, users=users)


@app.teardown_appcontext
def teardown_db(exception):
    """ This function removes the current SQLAlchemy session."""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
