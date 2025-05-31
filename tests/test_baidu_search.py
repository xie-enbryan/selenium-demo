import time

from common.unittest_common import UnittestCommon
from utils.logger import get_logger
from pages.baidu_search_page import BaiduSearchPage
from common.base_page import BasePage

log = get_logger()

class TestBaiduSearch (UnittestCommon):

        def search_and_verify (self,search_keywords):
            """
            抽取测试代码公共的部分，形成一个单独的方法
            :param search_keywords: 搜索输入的关键字
            :return:
            """
            bsp = BaiduSearchPage(self.driver)
            bsp.type_search(search_keywords)
            bsp.send_submit_button()
            bsp.get_windows_img()
            time.sleep(3)

            try:
                assert search_keywords in bsp.get_title()
                log.info (f"测试通过，搜索标题含搜索关键字：{search_keywords}")
            except Exception as e:
                log.error(f"测试失败，搜索标题不含搜索关键字： {search_keywords}")


        def test_baidu_search_001 (self):
            "测试中文关键字"
            self.search_and_verify('中国')

        def test_baidu_search_002 (self):
            "测试英文关键字"
            self.search_and_verify('python')

        def test_baidu_search_003 (self):
            "测试不正常的关键字"
            self.search_and_verify('xxxyyyy')

        def test_baidu_search_004 (self):
            "测试空字符"
            self.search_and_verify('')

if __name__ == "__main__":
    pass
