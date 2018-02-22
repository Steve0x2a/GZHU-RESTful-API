from resources.jw import *
from flask import Flask,jsonify
import flask_restful as restful


app = Flask(__name__)
api = restful.Api(app)
app.config['JSON_AS_ASCII'] = False


class HelloWorld(restful.Resource):
    def get(self):
        return {'hello': 'world'}

api.add_resource(HelloWorld, '/')

api.add_resource(grade_all, '/jw/grade/all')
api.add_resource(grade_year, '/jw/grade/year')
api.add_resource(grade_term, '/jw/grade/term')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)