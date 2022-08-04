import pytest
import json

from util.readcase import Case_operation

from util.logutil import logger


class Test_method:  # 用例数据处理


    @staticmethod
    def reaDcase(case):
        number = case['用例编号']
        title = case['用例名称']
        method = case['method']
        url = case['url']
        header =json.loads(case['header'])
        data = case['data']
        if data !=None and data!='':
            data = json.loads(case['data'])
        else:
            data = None
        dict_result = {'number': number,
                       'title': title,
                       'method': method,
                       'url': url,
                       'header': header,
                       'data': data}
        return dict_result


