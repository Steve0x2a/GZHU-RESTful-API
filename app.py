from resources.jw import *
from resources.lib import *
from flask import Flask,jsonify
import flask_restful as restful


#添加错误提醒
errors = {
    'PasswordError': {
        'message': "You give a wrong password",
    },
    'UnknownError': {
        'message': "Unknown Erorr. Try again later",
    },
    'requests.exceptions.Timeout':{
        'message': "Timeout!"
    }
}

app = Flask(__name__)
api = restful.Api(app,errors = errors)
app.config['JSON_AS_ASCII'] = False



class HelloWorld(restful.Resource):
    def get(self):
        return {'hello': 'world'}

api.add_resource(HelloWorld, '/')
'''JW Route'''
api.add_resource(grade_all, '/jw/grade/all')#查询所有成绩路由
api.add_resource(grade_year, '/jw/grade/year')#按学年查询成绩路由
api.add_resource(grade_term, '/jw/grade/term')#按学期查询成绩路由
api.add_resource(stu_info,'/jw/info')#查询个人信息路由
'''Library Number Route'''
api.add_resource(lib_date_num_all, '/lib/num/date/all')#按日期查询所有学院进馆人数路由
api.add_resource(lib_date_num_total, '/lib/num/date/total')#按日期查询总进馆人数路由
api.add_resource(lib_now_num_all, '/lib/num/now/all')#查询当前日期所有学院进馆人数路由
api.add_resource(lib_now_num_total, '/lib/num/now/total')#查询当前日期总进馆人数路由
api.add_resource(lib_borrowed_books, '/lib/books/borrowed')#获得当前所借书籍
api.add_resource(lib_renew_books, '/lib/books/renew')#续借当前所借书籍

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
