# coding:utf-8
# @author : csl
# @date   : 2018/08/25 10:16
"""PC首页"""

import time
from selenium.webdriver.common.by import By
from BaseSe.Selenium3 import Pyse

class DKpc_HomePage(Pyse):

    """定位器"""
    # 顶部TAB页面
    # LOGO
    xpath_logo = (By.XPATH, "//div[@class='silkContainer']//div[@class='logo']")
    # C2C
    xpath_tab_c2c = (By.XPATH, "//ul[@class='ivu-menu']//a[@href='#/c2c']")
    # 币币交易
    xpath_tab_Switch_exchange = (By.XPATH, "//ul[@class='ivu-menu']//a[@href='#/exchange']")
    # 个人中心
    xpath_tab_uc_assets = (By.XPATH, "//ul[@class='ivu-menu']//a[@href='#/uc/assets']")
    # 活动中心
    xpath_tab_activity_lock = (By.XPATH, "//ul[@class='ivu-menu']//a[@href='#/activity/lock']")
    # SLU生态
    xpath_tab_slust = (By.XPATH, "//ul[@class='ivu-menu']//a[@href='#/slust']")

    # 登录按钮
    xpath_button_jump_login = (By.XPATH, "//ul[@class='ivu-menu']//a[@href='#/login']")

    # 上部滚动广告
    # 公告通知列表
    xpath_Announcement_list = (By.XPATH, "//div[@class='bulletin xs-hide']//span[@class='head']")
    # 第一条公告，公告页面归入主页
    xpath_first_Announcement = (By.XPATH, "//div[@class='mode']//a[1]/div/p")

    # 中部涨幅榜
    # CNYT交易区
    xpath_CNYT_Trading_area = (By.XPATH, "//div[@class='currencyTab']//li[contains(text(), 'CNYT交易区')]")
    # USDT交易区
    xpath_USDT_Trading_area = (By.XPATH, "//div[@class='currencyTab']//li[contains(text(), 'USDT交易区')]")
    # ETH交易区
    xpath_ETH_Trading_area = (By.XPATH, "//div[@class='currencyTab']//li[contains(text(), 'ETH交易区')]")
    # 自选交易区
    xpath_Optional_Trading_area = (By.XPATH, "//div[@class='currencyTab']//li[contains(text(), '自选交易区')]")
    # 币种搜索框
    xpath_Currency_search_box = (By.XPATH, "//div[@class='currencyTab']//div[@class='search']//input")

    # 底部导航
    # 关于我们
    xpath_about_us = (By.XPATH, "//div[@class='ivu-row']//a[contains(text(), '关于我们')]")
    # 公告中心
    xpath_Announcement_center = (By.XPATH, "//div[@class='ivu-row']//a[contains(text(), '公告中心')]")
    # 帮助中心
    xpath_Help_center = (By.XPATH, "//div[@class='ivu-row']//a[contains(text(), '帮助中心')]")
    # 上币申请
    xpath_Coin_application = (By.XPATH, "//div[@class='ivu-row']//a[contains(text(), '上币申请')]")
    # 用户协议
    xpath_User_Agreement = (By.XPATH, "//div[@class='ivu-row']//a[contains(text(), '用户协议')]")
    # 资费说明
    xpath_Tariff_description = (By.XPATH, "//div[@class='ivu-row']//a[contains(text(), '资费说明')]")
    # 交易规则
    xpath_Trading_Rules = (By.XPATH, "//div[@class='ivu-row']//a[contains(text(), '交易规则')]")
    # 币种资料
    xpath_Currency_information = (By.XPATH, "//div[@class='ivu-row']//a[contains(text(), '币种资料')]")

    # 传入参数
    # 搜索币种
    currency_search_box_value = "SLU"

    def open(self):
        # 调用Selenium3中的_open()方法打开连接
        self._open(self.base_url, self.pagetitle)


    def switch_homePage_unlogin(self):
        """
        @description: 预览未登录页面
        :return: 
        """
        self.find_element(*self.xpath_tab_c2c).click()
        self.page_waiting()
        self.find_element(*self. xpath_tab_Switch_exchange).click()
        self.page_waiting()
        self.find_element(*self.xpath_tab_activity_lock).click()
        self.page_waiting()
        self.find_element(*self.xpath_tab_uc_assets).click()
        self.page_waiting()
        self.find_element(*self.xpath_tab_slust).click()
        self.page_waiting()

        # 浏览涨幅榜
        self.find_element(*self.xpath_logo).click()
        self.page_waiting()
        self.find_element(*self.xpath_USDT_Trading_area).click()
        self.send_keys(self.xpath_Currency_search_box, self.currency_search_box_value)
        self.page_waiting()
        self.find_element(*self.xpath_ETH_Trading_area).click()
        self.send_keys(self.xpath_Currency_search_box, self.currency_search_box_value)
        self.page_waiting()
        self.find_element(*self.xpath_Optional_Trading_area).click()
        self.page_waiting()
        self.back()
        self.page_waiting()
        self.find_element(*self.xpath_CNYT_Trading_area).click()
        self.send_keys(self.xpath_Currency_search_box, self.currency_search_box_value)
        self.page_waiting()

        # 浏览公告列表
        self.find_element(*self.xpath_Announcement_list).click()
        self.page_waiting()
        # 点击公告列表第一条公告
        self.find_element(*self.xpath_first_Announcement).click()
        self.page_waiting()
        self.back()
        self.page_waiting()
        self.back()

        # 浏览底部导航
        self.js_scroll_end()
        self.find_element(*self.xpath_about_us).click()
        self.page_waiting()
        self.find_element(*self.xpath_Announcement_center).click()
        self.page_waiting()
        self.find_element(*self.xpath_Help_center).click()
        self.page_waiting()
        self.find_element(*self.xpath_Coin_application).click()
        self.page_waiting()
        self.find_element(*self.xpath_User_Agreement).click()
        self.page_waiting()
        self.find_element(*self.xpath_Tariff_description).click()
        self.page_waiting()
        self.find_element(*self.xpath_Trading_Rules).click()
        self.page_waiting()
        self.find_element(*self.xpath_Currency_information).click()
        self.js_scroll_top()



    def open_loginPage(self):
        """
        @description: 跳转登录页面
        :return: 
        """
        self.find_element(*self. xpath_button_jump_login).click()


    def open_uc_assets_page(self):
        """
        @description: 跳转个人中心页面
        :return: 
        """
        self.find_element(*self.xpath_tab_uc_assets).click()
