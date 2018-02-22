from resources.jw import *
from resources.lib import *
from flask import Flask,jsonify
import flask_restful as restful


app = Flask(__name__)
api = restful.Api(app)
app.config['JSON_AS_ASCII'] = False


class HelloWorld(restful.Resource):
    def get(self):
        return {'hello': 'world'}

api.add_resource(HelloWorld, '/')
'''Grade Route'''
api.add_resource(grade_all, '/jw/grade/all')
api.add_resource(grade_year, '/jw/grade/year')
api.add_resource(grade_term, '/jw/grade/term')

'''Library Number Route'''
api.add_resource(lib_date_num_all, '/lib/num/date/all')
api.add_resource(lib_date_num_total, '/lib/num/date/total')
api.add_resource(lib_now_num_all, '/lib/num/now/all')
api.add_resource(lib_now_num_total, '/lib/num/now/total')
api.add_resource(lib_borrowed_books, '/lib/books/borrowed')
api.add_resource(lib_renew_books, '/lib/books/renew')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)