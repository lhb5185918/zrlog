import json

import pytest
import requests
@pytest.fixture(scope='function')
def get_token():
    url = 'http://124.70.94.252:8000/api/admin/login'
    data = {"userName":"admin","password":"0bf439abd5791b36a5d5e61cd326617b","https":"false"}
    header = {"Content-Type":"application/json;charset=UTF-8"}
    res = requests.post(url=url,json=data,headers=header)
    token = {"Cookie": "JSESSIONID.c4969281=node010xqj5ae7gbpe194g7j7aicunv8.node0; td_cookie=1578469797;" + res.headers['Set-Cookie']}
    header1  = {"Content-Type":"application/json;charset=UTF-8","Cookie": "JSESSIONID.c4969281=node010xqj5ae7gbpe194g7j7aicunv8.node0; td_cookie=1578469797;" + res.headers['Set-Cookie']}
    return header1

