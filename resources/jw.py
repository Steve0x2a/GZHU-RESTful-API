from flask_restful import reqparse
import flask_restful as restful

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