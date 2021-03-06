import os
import sys
import time
import unittest

from report.Runner.HTMLTestRunner3 import HTMLTestRunner

def create_suite():

    TestSuite = unittest.TestSuite()#测试集
    test_dir = os.getcwd()+'\\TestCase\\'
    # print(test_dir)

    discover = unittest.defaultTestLoader.discover(
        start_dir=test_dir,
        pattern='Test_DKpc.py',  # 指定执行文件
        top_level_dir=None
    )
 
    # print (discover)

    for test_case  in discover:
        TestSuite.addTests(test_case)
    return TestSuite

def report():
    if len(sys.argv) > 1:
        report_name = os.getcwd() + '\\report\\' + sys.argv[1] + '_result.html'
    else:
        now = time.strftime("%Y-%m-%d_%H_%M_%S_")
        #需要查看每段时间的测试报告，可以这样写：
        # report_name = os.getcwd() + '\\report\\'+now+'result.html'
        report_name = os.getcwd()+'\\report\\result.html'
    return report_name

fp = open(report(),'wb')
Runner = HTMLTestRunner(
        stream=fp,
        title='PC_UI自动化测试报告',
        description='测试用例执行情况'
            )

if __name__ == '__main__':
    TestSuite = create_suite()
    Runner.run(TestSuite)
    fp.close()
