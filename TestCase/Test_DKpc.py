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

    @classmethod
    def setUpClass(cls):
        # 选择默认浏览器
        cls.driver = Pyse.browser()
        # 获取Excel表格中的url
        cls.url = DKpcData.UrlXlsx()
        # 获取Excel表格中的title
        cls.title = DKpcData.titleXlsx()

        # 打开测试主页
        cls.DKpc_startPage = DKpc_HomePage(cls.driver, cls.url, cls.title)
        cls.DKpc_startPage.open()

    @classmethod
    def tearDownClass(cls):
        driver = cls.driver
        sleep(5)
        driver.quit()


    def test_DKpc_HomePage_view(self):
        """测试预览页面,未登录状态"""
        self.DKpc_startPage.open_Switch_exchange()

    def test_login(self):
        """用户登录"""
        self.DKpc_startPage.open_loginPage()
        DKpc_login = DKpc_LoginPage(self.driver, self.url, self.title)
        DKpc_login.login_put()
        self.DKpc_startPage.open_uc_assets_page()




if __name__ == "__main__":
    unittest.main()