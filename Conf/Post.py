#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @author : csl
# @date   : 2018/09/17 10:52

import requests
import json
from Data.common_datas import Host, COMMON_TOKEN

class Post(object):

    """
    @:description：封装基础请求及数据库操作
    """

    def request2DKApi(self, server, data={}, requestmethord="POST", header={"access-auth-token":COMMON_TOKEN}):
        """
        :description: 请求后端接口
        :return: request.test转换成json格式
        """
        req_url = Host + server
        if requestmethord == "POST":
            req = requests.post(req_url, data, headers=header)
            return json.loads(req.text)
        elif requestmethord == "GET":
            req = requests.get(req_url)
            return json.loads(req.text)
        else:
            print("请求方式错误，请核对。。。")

    #使用post请求方式对手机号码进行删除请求
    #举个栗子：删除测试服务器上的手机号码
    def Dele(self, phone):
        url = 'http://112.74.29.84:***/api/User/deleteuser'
        teph = {'phone': phone}
        headers = {'content-type': 'application/json'}
        r = requests.post(url,json=teph,headers=headers)
        token_str = r.text
        token_dict = json.loads(token_str)
        if token_dict['success']==True:
            return True
        else:
            return False


if __name__ == "__main__":
    # r = input("请输入手机号码:",)
    # print(Post().Dele(r))
    r = Post().request2DKApi("uc/check/login",{})
    print(r["data"])
    print(type(r))
