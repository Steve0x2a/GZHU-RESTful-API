# GZHU-RESTful-API接口文档
用Requests + Flask + Flask-restful实现的广州大学部分网站第三方API
- 更新时间: 2014.02.23
- 返回数据格式: JSON
- 练手项目 不保证效率
- 此项目仅供学习 一切后果使用者负责

# 目录


# 教务类
### 查询个人信息
- 功能<br>从正方系统查询个人信息
- 接口地址<br>[/jw/info](http://api.0x2a.in/jw/info)
- 请求方式<br>`POST`
- POST请求示例
``` json
{
		"username" : "17xxxxxxx",
		"password" : "123456"
 }
 
 ``` 
- 请求结果示例
 
 ``` json
{
    "data": {
        "birthsday": "生日",
        "classname": "班级",
        "college": "学院",
        "enterSchoolTime": "入学时间",
        "gradeClass": "级",
        "highschool": "高中",
        "hometown": "户籍地址",
        "idCardNumber": "身份证号码",
        "major": "专业",
        "name": "姓名",
        "nationality": "民族",
        "politicsStatus": "政治面貌",
        "sex": "性别",
        "studentnumber": "学号",
    },
    "status": 200
}
``` 

### 查询成绩
接口可查询学期成绩、学年成绩、在校成绩。

#### 按学期查询
- 功能
 <br> 从正方系统直接查询当前学期成绩
 
- 接口地址<br>[/jw/grade/term](http://api.0x2a.in/jw/grade/term)
- 请求方式<br>`POST`
- POST请求示例 
``` json
{
		"username" : "17xxxxxxx",
		"password" : "123456"
 }
 
 ``` 
 
- 请求结果示例
 
 ``` json
{
    "data": 
        {
            "credit": "1.0",
            "grade": "94",
            "gradePonit": "4.4",
            "name": "专业导论",
            "term": "1",
            "type": "学科基础课程",
            "year": "2017-2018"
        },
    "status": 200
},
``` 

#### 按学年查询
- 接口地址<br>[/jw/grade/year](http://api.0x2a.in/jw/grade/year)
- 请求方式<br>`POST`
 - POST请求示例 
``` json
{
		"username" : "17xxxxxxx",
		"password" : "123456"
 }
 
 ```
 
- 请求结果示例
 
 ``` json
{
    "data": 
        {
            "credit": "1.0",
            "grade": "94",
            "gradePonit": "4.4",
            "name": "专业导论",
            "term": "1",
            "type": "学科基础课程",
            "year": "2017-2018"
        },
    "status": 200
},
``` 

#### 在校成绩查询
- 接口地址<br>[/jw/grade/all](http://api.0x2a.in/jw/grade/all)
- 请求方式<br>`POST`
 - POST请求示例 
``` json 
{
		"username" : "17xxxxxxx",
		"password" : "123456"
 }
 
 ```
 
- 请求结果示例
 
 ``` json
{
    "data": 
        {
            "credit": "1.0",
            "grade": "94",
            "gradePonit": "4.4",
            "name": "专业导论",
            "term": "1",
            "type": "学科基础课程",
            "year": "2017-2018"
        },
    "status": 200
},
``` 

# 图书馆类
### 图书馆进馆人数
接口可查询当日图书馆进馆总人数以及各学院人数、制定日期进馆总人数以及学院人数。
#### 当日进馆总人数
- 接口地址：<br>[/lib/num/now/total](http://api.0x2a.in/lib/num/now/total)
- 请求方式<br>`GET`
- 请求结果示例： 
 ``` json
{
		"data": {
        	"TotalNum": "114"
    	},
    	"status": 200
}
```

#### 当日进馆各学院人数
- 接口地址：<br>[/lib/num/now/all](http://api.0x2a.in/lib/num/now/all)
- 请求方式<br>`GET`
- 请求结果示例： 
 ``` json
{
        "data": {
            "FacultyNum": {
                "人文学院": "13",
                "信息与机电工程学院": "2",
                "公共事业管理（高水平运动员）": "6",
                "动画": "2",
                "化学化工学院": "5",
                "国际教育学院": "8",
                "土木工程学院": "9",
                "外国语学院": "2",
                "学前教育": "1",
                "建筑学(景观建筑)": "4",
                "数学与信息科学学院": "1",
                "新闻与传播学院": "1",
                "机械与电气工程学院": "10",
                "法学院": "8",
                "生物技术": "2",
                "社会体育指导与管理": "4",
                "经济与统计学院": "2",
                "自然地理与资源环境": "4",
                "计算机科学与教育软件学院": "3"
            },
            "TotalNum": "114"
        },
        "status": 200
}
``` 

#### 指定日期进馆总人数
注意：只有2016.12后的数据
- 接口地址：<br>[/lib/num/date/total](http://api.0x2a.in/lib/num/now/total)
- 请求方式<br>`POST`
- POST请求实例 
``` json
{
		"begin" : "2018-1-3",
		"password" : "2018-1-03",
 }
 
 ```
 
- 请求结果示例： 
 
 ``` json
{
        "data": {
            "TotalNum": "5492"
        },
        "status": 200
}
```

同理 想获得指定日期的各学院进馆人数只需要把接口地址的total改为all即可

### 图书馆借书管理
接口可获得当前所借书的借出日期、归还日期，以及提供一次性续借接口并返回续借状态

#### 获得当前所借书籍
- 接口地址：<br>[/lib/books/borrowed](http://api.0x2a.in/lib/books/borrowed)
- 请求方式：<br>`POST`
 - POST请求示例
 ``` json
{
		"username" : "17xxxxxxx",
		"password" : "123456"
 }
 
 ```
 
- 请求结果示例
 
  ``` json
  {
        "data": {
            "数据科学入门": {
                "LoanDate": "20171226",
                "RenewTimes": "1",
                "ReturnDate": "20180418"
            },
            "集体智慧编程": {
                "LoanDate": "20171129",
                "RenewTimes": "1",
                "ReturnDate": "20180319"
            }
        },
        "status": 200
}
```
 #### 获得当前所借书籍
- 接口地址：<br>[/lib/books/borrowed](http://api.0x2a.in/lib/books/borrowed)
- 请求方式：<br>`POST`
- POST请求示例
 ``` json
{
		"username" : "17xxxxxxx",
		"password" : "123456"
 }
 
 ```
 
- 请求结果示例
 
  ``` json
  {
        "data": {
            "数据科学入门": {
                "LoanDate": "20171226",
                "RenewTimes": "1",
                "ReturnDate": "20180418"
            },
            "集体智慧编程": {
                "LoanDate": "20171129",
                "RenewTimes": "1",
                "ReturnDate": "20180319"
            }
        },
        "status": 200
}
```
 
#### 续借当前所借书籍
- 接口地址：<br>[/lib/books/renew](http://api.0x2a.in/lib/books/renew)
- 请求方式：<br>`POST`
- POST请求示例
 ``` json
{
		"username" : "17xxxxxxx",
		"password" : "123456"
 }
 
 ``` 


- 请求结果示例
 
  ``` json
{
    "data": {
        "数据科学入门": "This book can not be renewed!",
        "集体智慧编程": "This book can not be renewed!"
    },
    "status": 200
}
``` 
例子中的书籍因都续借过所以无法续借。