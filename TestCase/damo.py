# coding:utf-8
from PIL import Image

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time


class image_test1(object):
    # 计算滑块位移距离
    def get_diff_location(self, image1,image2):
        #（880,1082）（344,490）为滑块图片区域，可能会受到一些清晰度的影响，可根据实际情况修改
        for i in range(880,1082):
            for j in range(400,444):
                #遍历原图与缺口图像素值寻找缺口位置
                if is_similar(image1,image2,i,j)==False:
                   return i
        return -1
    # 对比RGB值得到缺口位置
    def is_similar(self, image1,image2,x,y):
        pixel1 = image1.getpixel((x, y+88))
        pixel2 = image2.getpixel((x, y))
        # 截图像素也许存在误差，50作为容差范围
        if abs(pixel1[0]-pixel2[0])>=50 and abs(pixel1[1]-pixel2[1])>=50 and abs(pixel1[2]-pixel2[2])>=50:
            return False
        return True

    # 将缺口图片缺口背景全部替换为前面的白色背景
    def exchange_collor(self, image3):
        for ii in range(880, 1080):
            for jj in range(400,444):
                data = (image3.getpixel((ii, jj)))  # 打印该图片的所有点
                print(data)  # 打印每个像素点的颜色RGBA的值(r,g,b,alpha)
                print(data[0])  # 打印RGBA的r值
                if (data[0] >= 170 and data[1] >= 170 and data[2] >= 170):  # RGBA的r值大于170，并且g值大于170,并且b值大于170
                    image3.putpixel((ii, jj), (234, 53, 57, 255))  # 则这些像素点的颜色改成大红色
        image3.save("E:\DKpc_test\Data\Image\quekou_exchange.png")
#
#
#     quekouimg = Image.open("E:\DKpc_test\Data\Image\quekou.png")
#     # print(quekouimg.size)
#     sourceimg = Image.open("E:\DKpc_test\Data\Image\quekou1.png")
#     # print(sourceimg.size)
#     image3 = Image.open("E:\DKpc_test\Data\Image\quekou_copy.png")
#     # 获取缺口位置
#     visualstack = get_diff_location(sourceimg,quekouimg)
#     print("缺口位置：{}".format(visualstack))
#     # 获取移动距离loc，827为滑块起点位置
#     loc = visualstack-832
#     print("拖动水平位移：{}".format(loc))
#     exchange_collor(image3)
#

# class image_test2(object):
#     """截取登陆原图和带缺口的图"""
#
#     driver = webdriver.Chrome()
#     driver.get("http://www.400.pro/#/login")
#     driver.maximize_window()
#
#     # 用户名输入框
#     user_input_xpath = "//div[@class='ivu-form-item-content']//input[@class='ivu-input' and @name='user']"
#     # 密码输入框
#     password_input_xpath = "//div[@class='ivu-form-item-content']//input[@class='ivu-input' and @type='password']"
#     # 登录按钮
#     login_button_xpath = "//div[@class='ivu-form-item-content']//button[@id='loginBut']"
#     # 忘记密码
#     find_pwd_xpath = "//form[@autocomplete='off']//p//a"
#     # 跳转回登录页面登录按钮
#     back_login_page_xpath = "//ul[@class='ivu-menu']/a/li[contains(text(),'登录')]"
#     # 点击滑块
#     slider_button_xpath = "//div[@class='geetest_slider geetest_ready']//div[@class='geetest_slider_button']"
#
#     # 用户名密码
#     user = "17700000006"
#     password = "cs111111"
#
#     element_username = driver.find_element_by_xpath(user_input_xpath)
#     element_username.send_keys(user)
#     element_pass = driver.find_element_by_xpath(password_input_xpath)
#     element_pass.send_keys(password)
#     element_login = driver.find_element_by_xpath(login_button_xpath).click()
#     # time.sleep(3)
#
#     # js = """var q=driver.find_element_by_xpath("//div[@class='geetest_canvas_img geetest_absolute']/div[@class='geetest_slicebg geetest_absolute']");q.style.opacity = 0;"""
#     # driver.execute_script(js)
#
#     # time.sleep(120)
#     # driver.save_screenshot('E:\DKpc_test\Data\Image\OriginalImage\OriginalImage_6.png')
#
#     time.sleep(3)
#     driver.quit()

class image_test3(object):
    """selenium运行js修改页面参数"""

    driver = webdriver.Chrome()
    driver.get("https://www.baidu.com/")
    # 给搜索输入框标红javascript脚本
    js = "var q=document.getElementById(\"kw\");q.style.border=\"2px solid red\";"
    # 调用给搜索输入框标红js脚本
    driver.execute_script(js)
    time.sleep(3)
    # 单独执行js脚本
    driver.execute_script('alert("输入框标红了!")')
    time.sleep(3)
    # 接受提示信息
    driver.switch_to_alert().accept()
    time.sleep(3)
    # js隐藏元素,将获取的图片元素隐藏
    img1 = driver.find_element_by_xpath("//*[@id='lg']/img")
    driver.execute_script('$(arguments[0]).fadeOut()', img1)
    time.sleep(3)
    driver.find_element_by_xpath("//*[@id='kw']").send_keys("selenium")
    driver.find_element_by_xpath("//*[@id='su']").click()
    time.sleep(3)
    driver.quit()



if __name__ == "__main__":
    image_test3()