from common.base_page import BasePage
from utils.get_yaml_utils import GetElements

class BaiduSearchPage(BasePage):
    baidu_search_ele = GetElements ('baidu_search_element.yaml').get_elements()
    baidu_search_input = baidu_search_ele['baidu_search_input']
    baidu_search_button = baidu_search_ele['baidu_search_button']

    def type_search (self, text):
        self.type(self.baidu_search_input, text)

    def send_submit_button (self):
        self.click(self.baidu_search_button)
