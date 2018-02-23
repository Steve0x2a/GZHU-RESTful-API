import requests,urllib.parse
from common.parse import get_webflow,get_stuinfo,get__VIEWSTATE,get__VIEWSTATE2,getGrade
from common.error import PasswordError,UnknownError
import json
from flask_restful import abort



class jw(object):


    def __init__(self):
        self.baseUrl = 'http://202.192.18.184'
        self.session = requests.session()
        self.session.headers['User-Agent'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.131 Safari/537.36'
        self.loginurl = 'https://cas.gzhu.edu.cn/cas_server/login?service=http%3a%2f%2f202.192.18.183%2fLogin_gzdx.aspx'
   


        
    def login(self,username,password):
        '''
        :使用账号密码模拟登录 并且存储cookie
        '''
        #获得登录表格所需的值
        self.username = username
        get_lt = self.session.get(url = self.loginurl,timeout = 5)
        lt, execution = get_webflow(get_lt)
        #构建post表单
        postdata = {
            'username' : username,
            'password' : password,
            'lt' : lt,
            'execution' : execution,
            '_eventId' : 'submit',
            'submit' : '登录'
        }
        #用requests post模拟登陆

        response = self.session.post(url = self.loginurl, data = postdata)
        #若返回response中有xs_main.aspx项则证明登录成功
        if "xs_main.aspx" in response.text:
            #获得登陆者信息
            return 'Account login successfully'
        elif "密码错误" in response.text:
            raise PasswordError
        else:
            raise UnknownError

    def get_info(self,username,password):
        self.login(username,password)
        infourl = self.baseUrl+"/xsgrxx.aspx?xh="+self.username+"&"
        self.session.get(self.baseUrl)
        res = self.session.get(infourl)
        return get_stuinfo(res)


class grades(jw):


    def __init__(self,methond, XN = "",XQ = ""):
        jw.__init__(self)
        self.post_data = {    
            "__VIEWSTATE":"",
            "__VIEWSTATEGENERATOR" : "",
            "ddlXN":XN,
            "ddlXQ":XQ,
            "Button1" : ""#urllib.parse.quote_plus("按学期查询".encode('gb2312'))
        }
        self.methond = methond
    def main(self,username,password):
        self.grades_url = 'http://202.192.18.184/xscj_gc.aspx?xh='+username
        self.login(username,password)
        if self.methond == 'all':
            self.get_all()
        elif self.methond == 'xn':
            self.get_xn()
        elif self.methond == 'xq':
            self.get_xq()
        self.session.get(self.baseUrl,timeout = 5)
        __VIEWSTATE , __VIEWSTATEGENERATOR = get__VIEWSTATE(self.session.get(self.grades_url))
        self.post_data["__VIEWSTATE"] = __VIEWSTATE
        self.post_data["__VIEWSTATEGENERATOR"] = __VIEWSTATEGENERATOR
        response = self.session.post(self.grades_url,data=self.post_data,timeout = 5)
        grades = getGrade(response)
        return grades

    def get_all(self):
        self.post_data['Button1'] = urllib.parse.quote_plus("在校学习成绩查询".encode('gb2312'))
    def get_xn(self):
        self.post_data['Button1'] = urllib.parse.quote_plus("按学年查询".encode('gb2312'))
    def get_xn(self):
        self.post_data['Button1'] = urllib.parse.quote_plus("按学期查询".encode('gb2312'))



