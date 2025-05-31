import unittest
from common.browser_engine import BrowserEngine
from utils.logger import get_logger

log = get_logger()

class UnittestCommon(unittest.TestCase):

        @classmethod
        def setUpClass(cls):
            """
            执行测试用例前的操作
            :return:
            """
            browser =  BrowserEngine (cls)
            cls.driver = browser.open(cls)
            log.info("--------------------开始测试----------------------")

        @classmethod
        def tearDownClass(cls):
            """
            执行完测试用例后的操作
            :return:
            """
            cls.driver.quit ()
            log.info ("-----------------测试结束---------------------------")


if  __name__ =='__main__':
    pass
