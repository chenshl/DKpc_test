# coding:utf-8
# @author : csl
# @date   : 2018/07/26 09:03
# 数据库查询封装

import pymysql

class connect_mysql():
    """数据库查询类"""

    def __init__(self):

        """
        @description:连接数据库
        """
        try:
            self.connect = pymysql.Connect(
                host='172.16.0.66',
                port=3306,
                user='bjxy_db',
                passwd='Credit2016Admin',
                db='otc_sync',
                charset='utf8'
            )
        except Exception as e:
            print("连接数据库失败", e)


    def connect2mysql(self, complySql):

        """
        @description: 数据库连接操作
        :param complySql: 
        :return: 
        """
        try:
            # 获取游标
            self.cursor = self.connect.cursor()
            self.cursor.execute(complySql)
        except Exception as e:
            self.connect.rollback()
            print("数据库事务处理失败。。。", e)
        else:
            self.connect.commit()
            self.mysql_result = self.cursor.fetchall()
            # print("执行SQL：{}".format(complySql))
            # print("数据库事务处理成功。。。")

            return self.mysql_result
        finally:
            # 关闭游标，关闭连接
            self.cursor.close()
            self.connect.close()


    def mysqlResultFormat(self, data=((),), parameter_name=[]):

        """
        @description: 格式化mysql查询结果,将元组转换为字典格式
        :param self: 
        :param data: 查询结果
        :param parameter_name: 结果值对应的键值 
        :return: 字典格式
        """
        result = []
        if isinstance(data, tuple) and data:  # 判断data是一个元组并且不为空
            for tuple_data in data:
                if isinstance(tuple_data, tuple) and tuple_data:  # 判断元组中的参数不为空
                    chid_result = {}
                    if len(tuple_data) == len(parameter_name):
                        if isinstance(parameter_name, list) and parameter_name:  # 判断parameter_name是一个列表并且不为空
                            for i in range(len(parameter_name)):
                                chid_result[parameter_name[i]] = tuple_data[i]
                        else:
                            print("{}为空".format(parameter_name))
                            break
                        result.append(chid_result)
                    else:
                        print("{}和{}的参数长度不一致，请核对后传入！！！".format(tuple_data, parameter_name))
                        break
                else:
                    print("{}中有为空的参数".format(data))
                    break
        else:
            print("{}为空或者不为一个元组，请核对后传入！！！".format(data))

        return result



if __name__ == "__main__":
    sql = '''SELECT coin_id, balance, frozen_balance, lock_balance 
    FROM member_wallet 
    WHERE member_id = (SELECT id FROM member WHERE token = '754e216e9de6eca2a8bf9749797b29c2') AND coin_id IN('Silubium', 'USDT');
    '''
    result = connect_mysql().connect2mysql(sql)
    print(type(result))
    print(result)
    print(result[1][1])
    resultformat = connect_mysql().mysqlResultFormat(result, ["coin_id", "balance", "frozen_balance", "lock_balance"])
    print(resultformat)
    print(resultformat[0]["coin_id"])
