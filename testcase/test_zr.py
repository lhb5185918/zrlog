import pytest
import json
from util.logutil import logger
from util.mysqlutil import Pysql_util
from util.readcase import Case_operation
from util.requestsutil import Requests
from config.pathdata import case_path
from common.supermrthod import Test_method
import allure


@pytest.mark.run(order = 1)
@allure.feature("登录模块")
class Test_zrlog(Test_method):
    res = Case_operation().get_case(case_path, 'login')


    @pytest.mark.parametrize("case", res)
    def test_Login(self, case):
        result = Test_zrlog.reaDcase(case)
        res = Requests().send(url=result['url'],
                              data=result['data'],
                              method=result['method'],
                              header=result['header'])
        Case_operation().write_result(res=result['title'][0:4], xulie=0)
        logger.info("{}{}{},".format(result['number'], result['title'], res))
        assert res['code'] == 200

