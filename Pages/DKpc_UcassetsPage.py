# coding:utf-8
# @author : csl
# @date   : 2018/09/18 10:06
# 个人中心

from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

from BaseSe.Selenium3 import Pyse

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
    # 安全设置
    xpath_security_Settings = (By.XPATH, "//div[@class='ucMenu']//li[contains(text(),'安全设置')]")
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