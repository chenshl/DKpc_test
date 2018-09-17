#!/usr/bin/python
# coding:utf-8
# @author : csl
# @date   : 2018/04/19 22:04
# 测试用例

import unittest
from Pages.changqing_HomePage import changqing_HomePage
from Pages.changqing_integral_SearchPage import changqing_integral_SearchPage
from BaseSe.Selenium3 import Pyse
import Data.changqing_data as cqdata
from time import sleep

class ChangqingCase(unittest.TestCase):

    # 前置处理
    def setUp(self):
        # 选择默认浏览器
        self.driver = Pyse.browser()
        # 获取Excel表格中的url
        self.url = cqdata.UrlXlsx()
        # 获取Excel表格中的title
        self.title = cqdata.titleXlsx()


    # 测试用例
    def test_changqing1(self):
        # Page继承自Pyse的构造方法
        changqing = changqing_HomePage(self.driver, self.url, self.title)
        changqing.open()
        changqing.open_search()
        changqing = changqing_integral_SearchPage(self.driver, self.url, self.title)
        changqing.search_goods(cqdata.StrXlsx())
        changqing.click_search_button()


    # 后置处理
    def tearDown(self):
        driver = self.driver
        sleep(3)
        driver.quit()
