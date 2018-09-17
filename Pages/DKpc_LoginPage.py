# coding:utf-8
# @author : csl
# @date   : 2018/08/25 15:30
# 登录页面

from selenium.webdriver.common.by import By
from BaseSe.Selenium3 import Pyse
import time
from selenium.webdriver.common.action_chains import ActionChains
from BaseSe.Base import Base_image_move_distance as Bimd
import random

class DKpc_LoginPage(Pyse):

    """定位器"""
    # 用户名输入框
    user_input_xpath = (By.XPATH, "//div[@class='ivu-form-item-content']//input[@class='ivu-input' and @name='user']")
    # 密码输入框
    password_input_xpath = (By.XPATH, "//div[@class='ivu-form-item-content']//input[@class='ivu-input' and @type='password']")
    # 登录按钮
    login_button_xpath = (By.XPATH, "//div[@class='ivu-form-item-content']//button[@id='loginBut']")
    # 忘记密码
    find_pwd_xpath = (By.XPATH, "//form[@autocomplete='off']//p//a")
    # 跳转回登录页面登录按钮
    back_login_page_xpath = (By.XPATH, "//ul[@class='ivu-menu']/a/li[contains(text(),'登录')]")
    # 点击滑块
    slider_button_xpath = "//div[@class='geetest_slider geetest_ready']//div[@class='geetest_slider_button']"
    # 滑块未重合页面标识
    # sign_slider_xpath = "//div[@class='geetest_panel_next']//div[@class='geetest_slider_button']"
    # 图片刷新按钮
    refresh_button_xpath = "//div[@class='geetest_panel_next']//div[@class='geetest_panel']//a[@class='geetest_refresh_1']"

    """用户参数"""
    # 用户名密码
    user = "17700000006"
    password = "cs111111"
    # 截图保存路径
    save_image_path = "E:\DKpc_test\Data\Image\quekou.png"

    def open(self):
        # 调用Selenium3中的_open()方法打开连接
        self._open(self.base_url, self.pagetitle)

    def login_put(self):
        """登录"""

        def move_slider():
            """
            登录页面滑动滑块方法，便于失败后重试
            :return: 
            """
            # 拖动验证滑块,注：拖动定位不能使用（By.XPATH,""），否则报元组参数错误，使用基础的定位方法
            time.sleep(1)
            self.driver.save_screenshot(self.save_image_path)  # 屏幕截图
            move_distance = Bimd(self.save_image_path).move_distance()
            tracks = Bimd().get_tracks(move_distance)
            dragger = self.driver.find_element_by_xpath(self.slider_button_xpath)

            ActionChains(self.driver).click_and_hold(dragger).perform()
            for track in tracks:
                ActionChains(self.driver).move_by_offset(xoffset=track, yoffset=0).perform()
            else:
                ActionChains(self.driver).move_by_offset(xoffset=3, yoffset=0).perform()  # 先移过一点
                ActionChains(self.driver).move_by_offset(xoffset=-3, yoffset=0).perform()  # 再退回来，是不是更像人了

            time.sleep(0.5)  # 0.5秒后释放鼠标
            ActionChains(self.driver).release().perform()


        self.send_keys(self.user_input_xpath, self.user)
        self.send_keys(self.password_input_xpath, self.password)
        time.sleep(1)
        self.find_element(*self.login_button_xpath).click()

        move_slider()
        time.sleep(3)
        try:
            while True:
                dra = self.driver.find_element_by_xpath(self.refresh_button_xpath)
                if dra:
                    self.driver.find_element_by_xpath(self.refresh_button_xpath).click()
                    move_slider()
                    time.sleep(3)
                else:
                    break
        except Exception as e:
            print("滑块验证错误：{}".format(e))
            pass



