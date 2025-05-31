"""
页面基类，封装一些浏览器操作常用方法
"""

import os
import sys
import time

from selenium.webdriver.common import by

from utils.logger import get_logger
from selenium.common.exceptions import NoSuchElementException

log = get_logger()

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    # 退出浏览器
    def close_broswer(self):
        try:
            if self.driver:
                self.driver.quit()

        except Exception as e:
            log.error(f"关闭浏览器失败: {e}")

    # 浏览器前进操作
    def forward (self):
        try:
            self.driver.forward()

        except Exception as e:
            log.error(f"浏览器前进操作失败: {e}")


    # 浏览器返回操作
    def back (self):
        try:
            self.driver.back()
        except Exception as e:
            log.error (f"浏览器后退失败: {e}")

    # 关闭当前窗口
    def close_current_window(self):
        try:
            self.driver.close()
        except Exception as e:
            log.error (f"关闭窗口失败: {e}")

    # 保存截图操作
    def get_windows_img (self):

        try:
            root_path =  os.path.dirname(os.path.realpath(sys.argv[0]))
            screenshots_dir = os.path.join(root_path,'res','screenshots')
            os.mkdir(screenshots_dir,exist_ok=True)

            current_time = time.strftime('%Y-%m-%d-%H%M%S')
            screenshots_name = os.path.join(root_path,'res','screenshots',f'{current_time}-screenshots.png')
            self.driver.get_screenshots_as_file(screenshots_name)
            log.info (f"截图成功，保存于: {screenshots_name}")
        except Exception as e:
            log.error(f"截图失败：{e}")

    #元素定位操作
    def find_element (self,selector):

        # 默认使用id查找
        if '=>' not in selector:
            return self.driver.find_element("id", selector)

        # 分割定位方式和定位值
        selector_by, selector_value = selector.split ('=>',1)

        # 映射定义查找方式
        by_mapping = {
            'id': 'id',
            'name': 'name',
            'class': 'class name',
            'tag': 'tag name',
            'link_text': 'link text',
            'partial_link_text': 'partial link text',
            'xpath': 'xpath',
            'css': 'css selector'
        }

        if selector_by not in by_mapping:
            raise ValueError (f"定位方式不支持: {selector_by}. 请使用 {list(by_mapping.keys())}之一")

        by = by_mapping[selector_by]
        try:
            element = self.driver.find_element(by, selector_value)
            log.info(f"成功定位元素: [{by}] = '{selector_value}'")
            return element

        except NoSuchElementException as e:
            log.error(f"无法定位元素:[{by}] = '{selector_value}', 原因：{e}")
            raise

    # 文本输入
    def type (self, selector, text):
        element = self.find_element(selector)
        element.clear ()

        try:
            element.send_keys (text)
            log.info (f"输入成功，内容为: {text}")
        except Exception as e:
            log.error(f"输入失败，原因为{e}")

    # 清除文本框内容
    def clear (self, selector):
        element = self.find_element(selector)

        try:
            element.clear()
            log.info (f" 成功清除文本框内容,文本框为{element}")
        except Exception as e:
            log.error(f"清除文本框内容失败，文本框为{element}")

    # 点击元素事件
    def click (self,selector):
        element = self.find_element(selector)

        try:
            element.click()
            log.info (f"成功点击{element}")
        except Exception as e:
            log.error (f"点击{element} 失败")


    # 获取网页标题
    def get_title(self):
        try:
            title = self.driver.title
            log.info (f"成功获取标题： {title}")
            return title

        except Exception as e:
            log.error (f"获取标题失败")

    # 等待
    def sleep (seconds):
        time.sleep(seconds)


