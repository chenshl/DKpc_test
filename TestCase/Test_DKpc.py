# coding:utf-8
# @author : csl
# @date   : 2018/08/25 14:47
# 测试用例

import unittest
from BaseSe.Selenium3 import Pyse
from Pages.DKpc_HomePage import DKpc_HomePage
from Pages.DKpc_LoginPage import DKpc_LoginPage
from Pages.DKpc_UcassetsPage import DKpc_UcassetsPage

from selenium.webdriver.common.action_chains import ActionChains

import Data.DKpc_data as DKpcData
from time import sleep

class DKpcCase(unittest.TestCase):
    """
    @description: 用户登录状态页面元素浏览
    """

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


    def test_1_switch_unlogin(self):
        """
        @description: 测试预览页面,未登录状态
        :return: 
        """
        self.DKpc_startPage.switch_homePage_unlogin()

    def test_2_switch_login(self):
        """
        @description: 用户登录and个人中心浏览
        :return: 
        """
        self.DKpc_startPage.open_loginPage()
        self.DKpc_login = DKpc_LoginPage(self.driver, self.url, self.title)
        self.DKpc_login.login_put()
        self.DKpc_startPage.open_uc_assets_page()
        self.DKpc_Ucassets = DKpc_UcassetsPage(self.driver, self.url, self.title)
        self.DKpc_Ucassets.browse_DKpc_UcassetsPage_elements()


if __name__ == "__main__":
    unittest.main()