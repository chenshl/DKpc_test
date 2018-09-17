# coding:utf-8
# @author : csl
# @date   : 2018/08/25 10:16
"""PC首页"""

import time
from selenium.webdriver.common.by import By
from BaseSe.Selenium3 import Pyse

class DKpc_HomePage(Pyse):

    """定位器"""
    # tab页面
    # C2C
    tab_c2c = (By.XPATH, "//ul[@class='ivu-menu']//a[@href='#/c2c']")
    # 币币交易
    tab_Switch_exchange = (By.XPATH, "//ul[@class='ivu-menu']//a[@href='#/exchange']")
    # 个人中心
    tab_uc_assets = (By.XPATH, "//ul[@class='ivu-menu']//a[@href='#/uc/assets']")
    # 活动中心
    tab_activity_lock = (By.XPATH, "//ul[@class='ivu-menu']//a[@href='#/activity/lock']")
    # SLU生态
    tab_slust = (By.XPATH, "//ul[@class='ivu-menu']//a[@href='#/slust']")
    # 登录按钮
    button_jump_login = (By.XPATH, "//ul[@class='ivu-menu']//a[@href='#/login']")

    def open(self):
        # 调用Selenium3中的_open()方法打开连接
        self._open(self.base_url, self.pagetitle)


    def open_Switch_exchange(self):
        """
        @description: 预览未登录页面
        :return: 
        """
        self.find_element(*self.tab_c2c).click()
        time.sleep(1)
        self.find_element(*self.tab_Switch_exchange).click()
        time.sleep(1)
        self.find_element(*self.tab_activity_lock).click()
        time.sleep(1)
        self.find_element(*self.tab_uc_assets).click()
        time.sleep(1)
        self.find_element(*self.tab_slust).click()
        time.sleep(1)


    def open_loginPage(self):
        """
        @description: 跳转登录页面
        :return: 
        """
        self.find_element(*self.button_jump_login).click()


    def open_uc_assets_page(self):
        """
        @description: 跳转个人中心页面
        :return: 
        """
        self.find_element(*self.tab_uc_assets).click()
