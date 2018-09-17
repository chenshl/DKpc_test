# coding:utf-8
# @author : csl
# @date   : 2018/08/25 14:47
# 测试用例

import unittest
from BaseSe.Selenium3 import Pyse
from Pages.DKpc_HomePage import DKpc_HomePage
from Pages.DKpc_LoginPage import DKpc_LoginPage

from selenium.webdriver.common.action_chains import ActionChains

import Data.DKpc_data as DKpcData
from time import sleep

class DKpcCase(unittest.TestCase):

    def setUp(self):
        # 选择默认浏览器
        self.driver = Pyse.browser()
        # 获取Excel表格中的url
        self.url = DKpcData.UrlXlsx()
        # 获取Excel表格中的title
        self.title = DKpcData.titleXlsx()

    def tearDown(self):
        driver = self.driver
        sleep(5)
        driver.quit()


    def test_DKpc_HomePage_view(self):
        """测试预览页面"""
        DKpc_click = DKpc_HomePage(self.driver, self.url, self.title)
        DKpc_click.open()
        DKpc_click.open_Switch_exchange()

    def test_login(self):
        """用户登录"""
        DKpc_click = DKpc_HomePage(self.driver, self.url, self.title)
        DKpc_click.open()
        DKpc_click.open_loginPage()
        DKpc_login = DKpc_LoginPage(self.driver, self.url, self.title)
        DKpc_login.login_put()




if __name__ == "__main__":
    unittest.main()