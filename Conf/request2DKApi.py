# coding:utf-8
# @author : csl
# @date   : 2018/07/24 13:35
# 请求封装


import requests
import time
# from common.writelog_up import WriteLogger

# logger = WriteLogger().getLogger()

class request2DKApi(object):
    """
    @description: 封装接口请求
    """

    # 请求路径配置
    REQUESTS_URL = "http://api.400.pro/"  # 前端
    REQUESTS_URL_ADMIN = "http://api.dkadmin.400.pro/"  # 后台

    # 用户token
    COMMON_TOKEN = "1000000000001"  # 常用用户token

    def __init__(self, server, datas={}, header={"access-auth-token":COMMON_TOKEN}):

        # 判断后台路径
        if "admin/" in server:
            self.url = self.REQUESTS_URL_ADMIN  # 后台
        else:
            self.url = self.REQUESTS_URL
        # self.url = "http://172.16.0.79:6003/"  # 撮合exchange-api
        # self.url = "http://172.16.0.79:6001/"  # ucenter-api
        # self.url = "http://172.16.0.79:6002/"  # otc-api
        # self.url = "http://172.16.1.84:6003/"  # 撮合exchange-api田波本机

        self.server = server
        self.requrl = self.url + self.server
        self.data = datas
        self.header = header  # 定义请求头信息，用户token
        # self.cookie = {'key': 'value'}  # 定义cookie


    def send(self, requestMark="POST"):
        """
        @description: 发送请求
        :param requestMark: 
        :return: 
        """
        try:
            # logger.info("请求地址：{}  请求方式：{}--请求参数：{}".format(self.url + self.server, requestMark, self.data))
            self.beforetime = time.time()
            if requestMark == "GET":
                print("请求地址：{}  请求方式：{}--请求参数{}".format(self.url + self.server, requestMark, self.data))
                self.req = requests.get(self.requrl)
            elif requestMark == "POST":
                print("请求地址：{}  请求方式：{}--请求参数{}".format(self.url + self.server, requestMark, self.data))
                self.req = requests.post(self.requrl, self.data, headers=self.header)
            elif requestMark == "PATCH":
                print("请求地址：{}  请求方式：{}--请求参数{}".format(self.url + self.server, requestMark, self.data))
                self.req = requests.patch(self.requrl,self.data)
            self.aftertime = time.time()
            self.reqtime = str(round((self.aftertime - self.beforetime) * 1000, 3))
            # logger.info("响应时长：{}--响应状态:{}--响应结果：{}".format(self.reqtime,self.req.status_code, self.req.text))
        except Exception as e:
            print("请求异常")
            print(e)
            # logger.error("请求异常{}".format(e))
        return self.req.status_code, self.reqtime, self.req.text


if __name__ == "__main__":
    id = "2185"
    server = "admin/member/member-application/{}/pass".format(id)
    r = request2DKApi(server).send("PATCH")
    print(r)