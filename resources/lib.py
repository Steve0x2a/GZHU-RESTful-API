from flask_restful import reqparse
import flask_restful as restful
from common.lib import *
from flask import jsonify
def lib_num_post_data():
    parser = reqparse.RequestParser()
    parser.add_argument('begin' , required=True,type=str)
    parser.add_argument('end', required=True,type=str)
    args = parser.parse_args()
    return args

def lib_books_post_data():
    parser = reqparse.RequestParser()
    parser.add_argument('username' , required=True,type=str)
    parser.add_argument('password', required=True,type=str)
    args = parser.parse_args()
    return args

    
class lib_date_num_all(restful.Resource):
    def post(self):
        args = lib_num_post_data()
        app = DateTotal(args['begin'],args['end'])
        res = app.get_all()
        return jsonify(res)

class lib_date_num_total(restful.Resource):
    def post(self):
        args = lib_num_post_data()
        app = DateTotal(args['begin'],args['end'])
        res = app.get_total()
        return jsonify(res)

class lib_now_num_all(restful.Resource):
    def get(self):
        app = NowTotal()
        res = app.get_all()
        return jsonify(res)

class lib_now_num_total(restful.Resource):
    def get(self):
        app = NowTotal()
        res = app.get_total()
        return jsonify(res)

class lib_borrowed_books(restful.Resource):
    def post(self):
        args = lib_books_post_data()
        app = LibBooks()
        res = app.get_borrowed_books(args['username'],args['password'])
        return jsonify(res)

class lib_renew_books(restful.Resource):
    def post(self):
        args = lib_books_post_data()
        app = LibBooks()
        res = app.renew_books(args['username'],args['password'])
        return jsonify(res) 