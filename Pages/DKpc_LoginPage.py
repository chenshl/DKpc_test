# coding:utf-8
# @author : csl
# @date   : 2018/08/25 15:30
# 登录页面

from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

from BaseSe.Selenium3 import Pyse
from BaseSe.Base import Base_image_move_distance as Bimd

class DKpc_LoginPage(Pyse):

    """定位器"""
    # 用户名输入框
    xpath_user_input = (By.XPATH, "//div[@class='ivu-form-item-content']//input[@class='ivu-input' and @name='user']")
    # 密码输入框
    xpath_password_input = (By.XPATH, "//div[@class='ivu-form-item-content']//input[@class='ivu-input' and @type='password']")
    # 登录按钮
    xpath_login_button = (By.XPATH, "//div[@class='ivu-form-item-content']//button[@id='loginBut']")

    # 忘记密码
    xpath_find_pwd = (By.XPATH, "//form[@autocomplete='off']//p//a")
    # 跳转回登录页面登录按钮
    xpath_back_login_page = (By.XPATH, "//ul[@class='ivu-menu']/a/li[contains(text(),'登录')]")
    # 点击滑块
    xpath_slider_button = "//div[@class='geetest_slider geetest_ready']//div[@class='geetest_slider_button']"
    # 滑块未重合页面标识
    # sign_slider_xpath = "//div[@class='geetest_panel_next']//div[@class='geetest_slider_button']"
    # 图片刷新按钮
    xpath_refresh_button = "//div[@class='geetest_panel_next']//div[@class='geetest_panel']//a[@class='geetest_refresh_1']"
    # 超过图片次数刷新
    xpath_error_refresh_button = "//div[@class='geetest_panel_box']//div[@class='geetest_panel_error_content']"

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
            dragger = self.driver.find_element_by_xpath(self.xpath_slider_button)

            ActionChains(self.driver).click_and_hold(dragger).perform()
            for track in tracks:
                ActionChains(self.driver).move_by_offset(xoffset=track, yoffset=0).perform()
            else:
                ActionChains(self.driver).move_by_offset(xoffset=3, yoffset=0).perform()  # 先移过一点
                ActionChains(self.driver).move_by_offset(xoffset=-3, yoffset=0).perform()  # 再退回来，是不是更像人了

            time.sleep(0.5)  # 0.5秒后释放鼠标
            ActionChains(self.driver).release().perform()

        # 输入登录用户信息
        self.send_keys(self.xpath_user_input, self.user)
        self.send_keys(self.xpath_password_input, self.password)
        time.sleep(1)
        self.find_element(*self.xpath_login_button).click()

        # 加载页面后先滑动一次滑块，如未成功再重试
        move_slider()
        time.sleep(3)
        # 重试滑块
        try:
            while True:
                try:
                    # 先查找滑块页面下部的刷新按钮，找到后刷新，如页面为找到该刷新按钮则找加载过多的刷新按钮
                    dra = self.driver.find_element_by_xpath(self.xpath_refresh_button)
                    if dra:
                        dra.click()
                        move_slider()
                        time.sleep(3)
                except:
                    try:
                        # 未找到滑块下部的刷新按钮时，优先查找加载过多的刷新按钮
                        self.error_button_element = self.driver.find_element_by_xpath(self.xpath_error_refresh_button)
                        self.error_button_element.click()
                        time.sleep(3)
                    except:
                        # 都未找到则跳出循环
                        break
        except Exception as e:
            print("页面找不到刷新按钮或滑块验证失败：{}".format(e))
            self.driver.quit()



