from common.jw import jw,grades
from flask import Flask,jsonify
from flask.ext import restful
from flask.ext.restful import reqparse

app = Flask(__name__)
api = restful.Api(app)
app.config['JSON_AS_ASCII'] = False

def post_data():
    parser = reqparse.RequestParser()
    parser.add_argument('username' , required=True,type=str)
    parser.add_argument('password', required=True,type=str)
    args = parser.parse_args()
    return args

class grade_all(restful.Resource):
    def post(self):
        args = post_data()
        app = grades(args['username'],args['password'],methond='all')
        res=app.main()
        return jsonify(res)

class grade_year(restful.Resource):
    def post(self):
        args = post_data()
        app = grades(args['username'],args['password'],methond='xn')
        res=app.main()
        return jsonify(res)

class grade_term(restful.Resource):
    def post(self):
        args = post_data()
        app = grades(args['username'],args['password'],methond='xn')
        res=app.main()
        return jsonify(res)

api.add_resource(grade_all, '/grade/all')
api.add_resource(grade_year, '/grade/year')
api.add_resource(grade_term, '/grade/term')

if __name__ == '__main__':
    app.run(debug=True)