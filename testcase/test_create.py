import pytest
import json
from util.logutil import logger
from util.mysqlutil import Pysql_util
from util.readcase import Case_operation
from util.requestsutil import Requests
from config.pathdata import case_path
from common.supermrthod import Test_method
import allure

@allure.feature("新增")
@pytest.mark.run(order = 2)
class Test_create(Test_method):
    res = Case_operation().get_case(case_path, 'create')

    @pytest.mark.parametrize("case",res)
    def test_creat(self,case,get_token):
        result = Test_create.reaDcase(case)
        res = Requests().send(url=result['url'],
                              data=result['data'],
                              method=result['method'],
                              header=get_token)
        Case_operation().write_result(res=result['title'][0:4], xulie=1)
        logger.info("{}{}{},".format(result['number'], result['title'], res))
        assert res['code'] == 200
