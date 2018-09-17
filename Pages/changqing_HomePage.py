#!/usr/bin/python
# coding:utf-8
# @author : csl
# @date   : 2018/04/19 21:50
# 窝商城首页

from selenium.webdriver.common.by import By
from BaseSe.Selenium3 import Pyse
from selenium.webdriver.common.keys import Keys
import selenium.webdriver.common.action_chains as swcac

class changqing_HomePage(Pyse):

    """定位器"""
    # 窝商城首页搜索框
    jfsc_search = (By.XPATH, '//div[@class="jfsc-search"]')



    #操作
    #通过集成覆盖（overriding）方法:如果子类和父类的方法名相同，优先用子类自己的方法
    #打开网页
    def open(self):
        # 调用Selenium2中的_open()方法打开连接
        self._open(self.base_url, self.pagetitle)

    # 点击搜索框进入搜索页面
    def open_search(self):
        self.find_element(*self.jfsc_search).click()






