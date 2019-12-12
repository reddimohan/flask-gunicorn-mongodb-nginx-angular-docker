import os
from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_restplus import Api, Resource, fields
from flask_pymongo import PyMongo
from werkzeug.middleware.proxy_fix import ProxyFix

app = Flask(__name__)
app.wsgi_app = ProxyFix(app.wsgi_app)

# MongoDB connection
app.config["MONGO_URI"] = 'mongodb://' + os.environ['MONGODB_USERNAME'] + ':' + os.environ['MONGODB_PASSWORD'] + '@' + os.environ['MONGODB_HOSTNAME'] + ':27017/' + os.environ['MONGODB_DATABASE']

mongo = PyMongo(app)
db = mongo.db

api = Api(app, version='1.0', title='TodoMVC API',
    description='A simple TodoMVC API',
)

ns = api.namespace('todos', description='TODO operations')

todo = api.model('Todo', {
    'id': fields.Integer(readonly=True, description='The task unique identifier'),
    'task': fields.String(required=True, description='The task details')
})


@ns.route('/')
class TodoList(Resource):
    '''Shows a list of all todos, and lets you POST to add new tasks'''
    # @ns.doc('list_todos')
    # @ns.marshal_list_with(todo)
    def get(self):
        '''List all tasks'''
        _todos = db.todo.find()
        print('SUdo')
        item = {}
        data = []
        for todo in _todos:
            item = {
                'id': str(todo['_id']),
                'todo': todo['todo']
            }
            data.append(item)
        return jsonify(
            # status=True,
            data=data
        )

    @ns.expect(todo)
    @ns.marshal_with(todo, code=201)
    def post(self):
        '''Create a new task'''
        data = request.get_json(force=True)
        item = {
            'todo': data['task']
        }
        db.todo.insert_one(item)

        return jsonify(
            status=True,
            message='To-do saved successfully!'
        ), 201


if __name__ == '__main__':
    ENVIRONMENT_DEBUG = os.environ.get("APP_DEBUG", False)
    ENVIRONMENT_PORT = os.environ.get("APP_PORT", 7000)
    app.run(debug=ENVIRONMENT_DEBUG, port=ENVIRONMENT_PORT)

