# coding:utf-8
# @author : csl
# @date   : 2018/09/29 16:20
# 连接Redis

import redis
import json

class Connect_redis(object):

    """
    @description: 实时获取Redis缓存数据
    """

    def __init__(self):
        """
        @description: 建立数据库连接池
        """
        pool = redis.ConnectionPool(host='172.16.0.91', password="Credit2016Admin",  port=6379, db=0)
        self.con_redis = redis.Redis(connection_pool=pool)

    def get_redis(self, key):

        """
        @description: 查询对应键的values  --bytes.decode(s) or str.encode(s) 
        :param key: 查询键值
        :return: values
        """
        return json.loads(bytes.decode(self.con_redis.get(key)))

    def set_redis(self, key, values):

        """
        @description: 设置Redis键值对
        :param key: 
        :param values: 
        :return: 
        """
        self.con_redis.set(key, values)


if __name__ == "__main__":
    r = Connect_redis().get_redis("entity:appRevision:ANDROID")
    print(r)
    print(type(r))
    print(r[1]["downloadUrl"])
