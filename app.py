from resources.jw import *
from flask import Flask,jsonify
from flask.ext import restful


app = Flask(__name__)
api = restful.Api(app)
app.config['JSON_AS_ASCII'] = False


class HelloWorld(restful.Resource):
    def get(self):
        return {'hello': 'world'}

api.add_resource(HelloWorld, '/')

api.add_resource(grade_all, '/grade/all')
api.add_resource(grade_year, '/grade/year')
api.add_resource(grade_term, '/grade/term')

if __name__ == '__main__':
    app.run(debug=True)