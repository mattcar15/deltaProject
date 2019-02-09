#!flask/bin/python
from flask import Flask, jsonify
from flask import abort
from flask import make_response
from flask import request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

tasks = [
         {
         'id': 1,
         'synopsis': u'Bobby Report',
         'description': u'Hi my name is bobby and this is a piece that I would like to share when I fly I like to crash land.',
         'keywords': [ "crash", "fly", "land" ]
         },
         {
         'id': 2,
         'synopsis': u'Tom Report',
         'description': u'yeet yeet boom bang pow',
         'keywords': [ "boom", "bang", "pow" ]
         }
         ]

@app.route('/todo/api/v1.0/tasks', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': tasks})

@app.route('/todo/api/v1.0/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = [task for task in tasks if task['id'] == task_id]
    if len(task) == 0:
        abort(404)
    return jsonify({'task': task[0]})

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

@app.route('/todo/api/v1.0/tasks', methods=['POST'])
def create_task():
    if not request.json or not 'title' in request.json:
        abort(400)
    task = {
        'synopsis': tasks[-1]['id'] + 1,
        'title': request.json['title'],
        'description': request.json.get('description', ""),
        'keywords': False
    }
    tasks.append(task)
    return jsonify({'task': task}), 201

if __name__ == '__main__':
    app.run(debug=True)
