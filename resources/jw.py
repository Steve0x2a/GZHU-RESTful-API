from flask_restful import reqparse
import flask_restful as restful
from common.jw import *
from flask import jsonify


def RespObj(data):
    new = {
        'status' : 200,
        'data' : data, 
    }
    return new


def post_data():
    parser = reqparse.RequestParser()
    parser.add_argument('username' , required=True,type=str)
    parser.add_argument('password', required=True,type=str)
    args = parser.parse_args()
    return args

class grade_all(restful.Resource):
    def post(self):
        args = post_data()
        app = grades(methond='all')
        res=app.main(args['username'],args['password'])
        return jsonify(RespObj(res))

class grade_year(restful.Resource):
    def post(self):
        args = post_data()
        app = grades(methond='xn')
        res=app.main(args['username'],args['password'])
        return jsonify(RespObj(res))

class grade_term(restful.Resource):
    def post(self):
        args = post_data()
        app = grades(methond='xn')
        res=app.main(args['username'],args['password'])
        return jsonify(RespObj(res))

class stu_info(restful.Resource):
    def post(self):
        args = post_data()
        app = jw()
        res=app.get_info(args['username'],args['password'])
        return jsonify(RespObj(res))