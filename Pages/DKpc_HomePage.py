# coding:utf-8
# @author : csl
# @date   : 2018/08/25 10:16
"""PC首页"""

from selenium.webdriver.common.by import By
from BaseSe.Selenium3 import Pyse

class DKpc_HomePage(Pyse):

    """定位器"""
    # 币币交易tab页面
    tab_Switch_exchange = (By.XPATH, "//ul[@class='ivu-menu']//a[@href='#/exchange']/li[contains(text(),'币币交易')]")
    # 登录按钮
    # button_jump_login = (By.XPATH, "//ul[@class='ivu-menu']//a[@href='#/login']//li[contains(text(),'登录')]")
    button_jump_login = (By.XPATH, "//ul[@class='ivu-menu']//a[@href='#/login']")

    def open(self):
        # 调用Selenium3中的_open()方法打开连接
        self._open(self.base_url, self.pagetitle)

    # 未登录状态页面预览
    def open_Switch_exchange(self):
        self.find_element(*self.tab_Switch_exchange).click()

    # 跳转登录页面
    def open_loginPage(self):
        self.find_element(*self.button_jump_login).click()
