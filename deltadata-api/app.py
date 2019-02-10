#!flask/bin/python
from flask import Flask, jsonify
from flask import request
from flask import abort
from flask_cors import CORS
from flask import make_response

synopsis = []
numbers =[]

app = Flask(__name__)
CORS(app)

sets = [
    {
        'id':0,
        'classA': 0,
        'configA': 0,
        'classB': 0,
        'configB': 0,
        'synopsis': [],
        'numbers': []
    }
]

def makeData(classA, configA, classB, configB):
    global synopsis
    global numbers
    synopsis = ['lolz', 'hi there', 'this is a test', 'idk what else to write', 'good shit bro']
    numbers = ['1', '10', '8', '3', '5']

@app.route('/data/api/sets', methods=['GET'])
def get_tasks():
    return jsonify({'sets': sets})

@app.route('/data/api/sets/<int:set_id>', methods=['GET'])
def get_task(set_id):
    set = [set for set in sets if set['id'] == set_id]
    if len(set) == 0:
        abort(404)
    return jsonify({'sets': set[0]})

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

@app.route('/data/api/sets', methods=['POST'])
def create_task():
    if not request.json or not 'classA' or not 'classB' or not 'configA' or not 'configB' in request.json:
        abort(400)
    makeData(request.json['classA'],request.json['configA'],request.json['classB'],request.json['configB'])
    global synopsis
    global numbers
    set = {
        'id': sets[-1]['id'] + 1,
        'classA': request.json['classA'],
        'configA': request.json['configA'],
        'classB': request.json['classB'],
        'configB': request.json['configB'],
        'synopsis': synopsis,
        'numbers': numbers
    }
    sets.append(set)
    return jsonify({'set': set}), 201

@app.route('/todo/api/v1.0/tasks/<int:set_id>', methods=['DELETE'])
def delete_task(set_id):
    set = [set for set in sets if set['id'] == set_id]
    if len(set) == 0:
        abort(404)
    sets.remove(set[0])
    return jsonify({'result': True})

if __name__ == '__main__':
    app.run(debug=True)