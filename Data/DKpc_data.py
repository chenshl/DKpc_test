# coding:utf-8
# @author : csl
# @date   : 2018/08/25 10:27
# 读取页面打开数据，后面可以根据情况优化

import openpyxl

wb = openpyxl.load_workbook("Data/DKpc_data.xlsx")
sheet = wb["Sheet1"]

def titleXlsx():
    """
    :return:从文件中读取标题
    """
    title = sheet["A"]
    for i in title:
        return i.value

def UrlXlsx():
    """
    :return:从文件中读取访问地址
    """
    url = sheet["B"]
    for i in url:
        return i.value

def StrXlsx():
    """
    :return:从文件中读取文本内容
    """
    text = sheet["C"]
    for i in text:
        return i.value