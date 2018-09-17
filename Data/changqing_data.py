#!/usr/bin/python
# coding:utf-8
# @author : csl
# @date   : 2018/04/19 21:39
# 读取页面打开数据，后面可以根据情况优化

import openpyxl

wb = openpyxl.load_workbook("Data/changqing.xlsx")
sheet = wb["Sheet1"]

def StrXlsx():
    """
    :return:从excel文件中读取数据
    """
    text = sheet['C']
    # for i in random.choices(text):
    for i in text:
        return i.value

def UrlXlsx():
    """
    :return:从excel中读取url
    """
    url = sheet['B']
    for i in url:
        return i.value
def titleXlsx():
    """
    :return:从文件中读取标题
    """
    title = sheet['A']
    for i in title:
        return i.value