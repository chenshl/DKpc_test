# coding:utf-8
# @author : csl
# @date   : 2018/09/18 10:06
# 个人中心

from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

from BaseSe.Selenium3 import Pyse
from Conf.connect_redis import Connect_redis
from Conf.connect_mysql import connect_mysql


class DKpc_UcassetsPage(Pyse):

    """
    @description: 个人中心页面
    """

    # 定位器
    # 资产管理
    xpath_asset_Management = (By.XPATH, "//div[@class='ucMenu']//div[contains(text(),'资产管理')]")
    # 账单明细
    xpath_billing_Details = (By.XPATH, "//div[@class='ucMenu']//li[contains(text(),'账单明细')]")
    # 账单明细_下一页
    xpath_billing_Details_nextPage = (By.XPATH, "//div[@class='ucContent']//div[@class='blockpage mt10']//li[@title='下一页']")
    # 账单明细_上一页
    xpath_billing_Details_reviousPage = (By.XPATH, "//div[@class='ucContent']//div[@class='blockpage mt10']//li[@title='上一页']")
    # 账单明细_时间搜索框
    xpath_billing_Details_timeSearchBox = (By.XPATH, "//div[@class='ucContent']//div[@class='billSearch']//div[@class='ivu-date-picker-rel']//input")

    # 我的资产
    xpath_my_assets = (By.XPATH, "//div[@class='ucMenu']//li[contains(text(),'我的资产')]")
    # 充币
    xpath_coin_in = (By.XPATH, "//div[@class='ucMenu']//li[contains(text(),'充币')]")
    # 提币
    xpath_coin_out = (By.XPATH, "//div[@class='ucMenu']//li[contains(text(),'提币')]")

    # 账号安全
    xpath_account_security = (By.XPATH, "//div[@class='ucMenu']//div[contains(text(),'账号安全')]")
    # 账号信息
    xpath_account_information = (By.XPATH, "//div[@class='ucMenu']//li[contains(text(),'账号信息')]")
    # 身份认证
    xpath_authentication = (By.XPATH, "//div[@class='ucMenu']//li[contains(text(),'身份认证')]")
    # 身份认证_姓名输入框
    xpath_name_input = (By.XPATH, "//div[@class='ivu-form-item-content']//input[@placeholder='请输入真实姓名']")
    # 身份认证_身份证号输入框
    xpath_IDCard_num_input = (By.XPATH, "//div[@class='ivu-form-item-content']//input[@placeholder='请输入证件号']")
    # 身份认证_身份证图片上传框，有三个相同属性的元素
    xpath_IDCard_image_input_first = "//div[@class='mt10 uploadCard ivu-row']/div[1]/div[1]/div[1]/input"
    xpath_IDCard_image_input_second = "//div[@class='mt10 uploadCard ivu-row']/div[2]/div[1]/div[1]/input"
    xpath_IDCard_image_input_third = "//div[@class='mt10 uploadCard ivu-row']/div[3]/div[1]/div[1]/input"
    # 身份认证_确定按钮
    xpath_enter_button = (By.XPATH, "//div[@class='ivu-form-item-content']//button[@class='ivu-btn ivu-btn-primary ivu-btn-large']")
    # 安全设置
    xpath_security_Settings = (By.XPATH, "//div[@class='ucMenu']//li[contains(text(),'安全设置')]")
    # 安全设置_设置资金密码
    xpath_security_Settings_fund_password = (By.XPATH, "//ul[@class='accList']/li[1]/div[@class='accInfo']/a")
    # 安全设置_资金密码输入框
    xpath_security_Settings_fund_password_input = (By.XPATH, "//form[@class='formGroup ivu-form ivu-form-label-left']/div[@class='ivu-form-item'][1]//input")
    # 安全设置_短信验证码输入框
    xpath_security_Settings_SMS_code = (By.XPATH, "//form[@class='formGroup ivu-form ivu-form-label-left']/div[@class='ivu-form-item'][2]//input")
    # 安全设置_短信验证码发送按钮
    xpath_security_Settings_SMS_code_button = (By.XPATH, "//form[@class='formGroup ivu-form ivu-form-label-left']/div[@class='ivu-form-item'][2]//button")
    # 安全设置_资金密码提交按钮
    xpath_security_Settings_submit = (By.XPATH, "//form[@class='formGroup ivu-form ivu-form-label-left']/div[@class='ivu-form-item'][3]//button")
    # 支付方式
    xpath_payment_method = (By.XPATH, "//div[@class='ucMenu']//li[contains(text(),'支付方式')]")

    # 注册邀请
    xpath_registration_invitation = (By.XPATH, "//div[@class='ucMenu']//li[contains(text(),'注册邀请')]")

    # JS
    # 移除时间控件输入禁止
    js_remove_time_control = "$(\"//input[@class='ivu-input ivu-input-large']\").removeAttr('readonly')"


    def browse_DKpc_UcassetsPage_elements(self):
        """
        @description: 浏览个人中心页面元素
        :return: 
        """
        self.page_waiting()
        self.find_element(*self.xpath_billing_Details).click()
        self.page_waiting()

        # exchange = self.driver.find_element_by_xpath("//input[@class='ivu-input ivu-input-large']")
        # self.driver.execute_script("removeAttr('readonly')", exchange)
        # exchange.click()

        self.page_waiting()
        self.find_element(*self.xpath_my_assets).click()
        self.page_waiting()
        self.find_element(*self.xpath_coin_in).click()
        self.page_waiting()
        self.find_element(*self.xpath_coin_out).click()
        self.page_waiting()
        self.find_element(*self.xpath_account_security).click()
        self.page_waiting()
        self.find_element(*self.xpath_account_information).click()
        self.page_waiting()
        self.find_element(*self.xpath_authentication).click()
        self.page_waiting()
        self.find_element(*self.xpath_security_Settings).click()
        self.page_waiting()
        self.find_element(*self.xpath_payment_method).click()
        self.page_waiting()
        self.find_element(*self.xpath_registration_invitation).click()


    def revise_user_datas(self):
        """
        @description: 新用户添加及修改用户绑定数据
        :return: 
        """
        # 实名认证
        self.find_element(*self.xpath_account_security).click()
        self.find_element(*self.xpath_authentication).click()
        self.send_keys(self.xpath_name_input, "测试二十四")
        self.send_keys(self.xpath_IDCard_num_input, "500234198412231155")
        self.page_waiting()
        self.driver.find_element_by_xpath(self.xpath_IDCard_image_input_first).send_keys("E:\DKpc_test\Data\Image\quekou.png")
        self.driver.find_element_by_xpath(self.xpath_IDCard_image_input_second).send_keys("E:\DKpc_test\Data\Image\quekou.png")
        self.driver.find_element_by_xpath(self.xpath_IDCard_image_input_third).send_keys("E:\DKpc_test\Data\Image\quekou.png")
        time.sleep(3)
        self.find_element(*self.xpath_enter_button).click()


    def set_fund_password(self):
        """
        @description:设置资金密码
        :return: 
        """
        self.page_waiting()
        self.find_element(*self.xpath_security_Settings).click()
        self.page_waiting()
        self.find_element(*self.xpath_security_Settings_fund_password).click()
        self.send_keys(self.xpath_security_Settings_fund_password_input, "111111")
        self.find_element(*self.xpath_security_Settings_SMS_code_button).click()
        self.page_waiting()

        # 查询用户手机号
        mobile_phone = str(connect_mysql().connect2mysql("SELECT mobile_phone FROM member WHERE mobile_phone LIKE '1770000%' ORDER BY id DESC LIMIT 1;")[0][0])
        security_SMS_code = Connect_redis().get_redis("PHONE_RESET_TRANS_CODE_" + mobile_phone)
        time.sleep(2)
        self.send_keys(self.xpath_security_Settings_SMS_code, security_SMS_code)
        self.find_element(*self.xpath_security_Settings_submit).click()









