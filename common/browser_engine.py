import yaml
import  os
import sys

from selenium import webdriver
from time import sleep
from utils.logger import get_logger

log = get_logger()

class BrowserEngine:

    # 读取配置文件的路径
    config_path = os.path.join(os.path.dirname(os.path.realpath(__file__)),'config','config.yaml')

     #读取chrome driver的路径
    chrome_driver_path = os.path.join(os.path.dirname(os.path.realpath(__file__)),'driver', 'chromedriver.exe')
    #edegdriver 的路径
    edge_driver_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'driver', 'msedgedriver.exe')

    def __init__(self, driver):
        self.driver = driver


    def open (self,driver):
        # 读取配置文件
        with open (self.config_path) as f:
            config = yaml.load(f,Loader=yaml.FullLoader)

            # 获取浏览器
        driver = config["browserType"]["browserName"]
            # 获取要访问的地址
        url = config ["baseUrl"]["url"]

        if driver == "chrome":
            driver = webdriver.chrome (self.chrome_driver_path)

        elif driver == "edge":
            driver = webdriver.edge(self.edge_driver_path)

        driver.get (url)

        driver.maximize_window ()
        log.info (f"成功打开 {driver} 浏览器")

        sleep(5)
        return driver

        # 关闭浏览器
    def close_browser (self):

        self.driver.quit ()










