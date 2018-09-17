#!/usr/bin/python
# coding:utf-8
# @author : csl
# @date   : 2018/04/20 21:19
# 窝商城搜索页面

from selenium.webdriver.common.by import By
from BaseSe.Selenium3 import Pyse
from selenium.webdriver.common.keys import Keys
import selenium.webdriver.common.action_chains as swcac

class changqing_integral_SearchPage(Pyse):

    """定位器"""
    # 搜索框输入
    search_into = (By.XPATH, '//input[@id="searchKey"]')
    # 搜索按钮
    search_btn = (By.XPATH, '//span[@class="search-btn"]')


    # 搜索商品
    def search_goods(self, text):
        self.find_element(*self.search_into).send_keys(text)

    # 点击搜索按钮
    def click_search_button(self):
        self.find_element(*self.search_btn).click()