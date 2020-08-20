# coding=utf-8
import os
from common.readconfig import ini
import pytest
import allure
from page_object.Createplan import *
from faker import Faker

from page_object.upload import upload
from tools.logger import Log

log = Log().logger
fake = Faker(locale='zh_CN')
name = fake.name()


@allure.feature("jzyx-基准流程")
# @pytest.mark.flaky(reruns=2, reruns_delay=5)
class TestCreatpl:

    @pytest.fixture(scope='function', autouse=True)
    def create(self, drivers):
        Create = Createpl(drivers)
        Create.get_url(ini.url)

    # @pytest.mark.skip(reason="no way of currently testing this")

    @pytest.mark.run(order=1)
    @allure.story("创建计划-输入内容-提交计划")
    def test_001(self, drivers):
        """点击营销
            创建计划
            选择人群包-输入计划内容"""

        Create = Createpl(drivers)
        Create.login()
        Create.clickprecision()
        Create.Selectcrowd()
        Create.Fillplan()

    # @pytest.mark.skip(reason="no way of currently testing this")
    @allure.story("创建人群包-搜索")
    def test_002(self, drivers):
        uploading = upload(drivers)
        Create = Createpl(drivers)
        Create.login()
        uploading.up()
        uploading.search_r()
        result = uploading.text()
        log.info(result)
        assert result


if __name__ == '__main__':
    pytest.main(['testcase/Test_yx'])
    print(name)