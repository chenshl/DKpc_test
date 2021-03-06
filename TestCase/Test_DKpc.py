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
from Conf.connect_mysql import connect_mysql
from Conf.request2DKApi import request2DKApi
import time

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

        # 修改实名身份证号
        connect_mysql().connect2mysql("UPDATE member SET id_number = 'auto111111' WHERE id_number = '500234198412231155';")

        time.sleep(5)
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
        # 登录
        self.DKpc_startPage.open_loginPage()
        self.DKpc_login = DKpc_LoginPage(self.driver, self.url, self.title)
        self.DKpc_login.login_put()

        # 个人中心
        self.DKpc_startPage.open_uc_assets_page()
        self.DKpc_Ucassets = DKpc_UcassetsPage(self.driver, self.url, self.title)
        self.DKpc_Ucassets.browse_DKpc_UcassetsPage_elements()

    def test_3_registAndLogin(self):
        """
        @description: 新用户注册及实名绑定设置资金密码等操作
        :return: 
        """
        # 注册登录
        self.DKpc_startPage.open_registerPage()
        self.DKpc_register = DKpc_LoginPage(self.driver, self.url, self.title)
        self.DKpc_register.register_put()
        time.sleep(2)

        # time.sleep(15)

        # 实名认证
        self.DKpc_startPage.open_uc_assets_page()
        self.DKpc_Ucassets = DKpc_UcassetsPage(self.driver, self.url, self.title)
        self.DKpc_Ucassets.revise_user_datas()

        # 调用后台接口完成实名认证审核
        user_mobile = self.DKpc_register.register_mobile
        time.sleep(2)
        member_application = connect_mysql().connect2mysql("SELECT id FROM member_application WHERE member_id = (SELECT id FROM member WHERE mobile_phone = '{}') AND audit_status = 0;".format(user_mobile))
        request2DKApi("admin/member/member-application/{}/pass".format(member_application[0][0])).send("PATCH")

        # 设置资金密码
        self.DKpc_Ucassets.set_fund_password()


if __name__ == "__main__":
    unittest.main()