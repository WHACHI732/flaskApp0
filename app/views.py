from app import app
from flask import jsonify

@app.route('/')
def home():
    return "WHACHI says Hello world!"

@app.route('/phonebook')
def index():
    return app.send_static_file('phonebook.html')

@app.route('/api/data')
def data():

    d = {
        "Alice": "(708) 727_2377",
        "Whachi": "0610527443"
    }

    return jsonify(d)
