import requests,urllib.parse
from common.parse import get_webflow,get_stuinfo,get__VIEWSTATE,get__VIEWSTATE2,getGrade
import json

class jw(object):


    def __init__(self,username,password):
        self.baseUrl = 'http://202.192.18.184'
        self.username = username
        self.password = password
        self.session = requests.session()
        self.session.headers['User-Agent'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.131 Safari/537.36'
        self.loginurl = 'https://cas.gzhu.edu.cn/cas_server/login?service=http%3a%2f%2f202.192.18.183%2fLogin_gzdx.aspx'
        self.infourl = self.baseUrl+"/xsgrxx.aspx?xh="+self.username+"&"
        self.login_status = self.login()     


        
    def login(self):
        '''
        :使用账号密码模拟登录 并且存储cookie
        '''
        #获得登录表格所需的值
        get_lt = self.session.get(url = self.loginurl)
        lt, execution = get_webflow(get_lt)
        #构建post表单
        postdata = {
            'username' : self.username,
            'password' : self.password,
            'lt' : lt,
            'execution' : execution,
            '_eventId' : 'submit',
            'submit' : '登录'
        }
        #用requests post模拟登陆
        try:
            response = self.session.post(url = self.loginurl, data = postdata, timeout = 7)
        #若返回response中有xs_main.aspx项则证明登录成功
            if "xs_main.aspx" in response.text:
                #获得登陆者信息
                return 'Account login successfully'
            elif "密码错误" in response.text:
                return 'Got a wrong password'
            else:
                return 'Got a unknown error'
        except requests.exceptions.Timeout:
            return 'TimeOut!'
    def test1(self):
        return self.login_status

class grades(jw):


    def __init__(self,username,password,methond, XN = "",XQ = ""):
        jw.__init__(self,username,password)
        self.post_data = {    
            "__VIEWSTATE":"",
            "__VIEWSTATEGENERATOR" : "",
            "ddlXN":XN,
            "ddlXQ":XQ,
            "Button1" : ""#urllib.parse.quote_plus("按学期查询".encode('gb2312'))
        }
        self.grades_url = 'http://202.192.18.184/xscj_gc.aspx?xh='+self.username
        self.methond = methond
    def main(self):
        if self.methond == 'all':
            self.get_all()
        elif self.methond == 'xn':
            self.get_xn()
        elif self.methond == 'xq':
            self.get_xq()
        self.session.get(self.baseUrl)
        __VIEWSTATE , __VIEWSTATEGENERATOR = get__VIEWSTATE(self.session.get(self.grades_url))
        self.post_data["__VIEWSTATE"] = __VIEWSTATE
        self.post_data["__VIEWSTATEGENERATOR"] = __VIEWSTATEGENERATOR
        response = self.session.post(self.grades_url,data=self.post_data)
        grades = getGrade(response)
        return grades

    def get_all(self):
        self.post_data['Button1'] = urllib.parse.quote_plus("在校学习成绩查询".encode('gb2312'))
    def get_xn(self):
        self.post_data['Button1'] = urllib.parse.quote_plus("按学年查询".encode('gb2312'))
    def get_xn(self):
        self.post_data['Button1'] = urllib.parse.quote_plus("按学期查询".encode('gb2312'))

