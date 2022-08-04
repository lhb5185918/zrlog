
import requests

name = '中文'.encode('utf-8')


from config.pathdata import case_path

from util.readcase import Case_operation\


from util.requestsutil import Requests
def get_token():
    url = 'http://124.70.94.252:8000/api/admin/login'
    data = {"userName":"admin","password":"0bf439abd5791b36a5d5e61cd326617b","https":"false"}
    header = {"Content-Type":"application/json;charset=UTF-8"}
    res = requests.post(url=url,json=data,headers=header)
    token = {"Cookie": "JSESSIONID.c4969281=node010xqj5ae7gbpe194g7j7aicunv8.node0; td_cookie=1578469797;" + res.headers['Set-Cookie']}
    header1  = {"Content-Type":"application/json;charset=UTF-8","Cookie": "JSESSIONID.c4969281=node010xqj5ae7gbpe194g7j7aicunv8.node0; td_cookie=1578469797;" + res.headers['Set-Cookie']}
    return header1
url  = 'http://124.70.94.252:8000/api/admin/article/create'
data = {"keywords":"","rubbish":'true',"title":"新增测试用例00","alias":"新增测试00","markdown":"新增测试用例","content":"<p>新增测试用例1</p>\n","typeId":1}
method = 'post'

