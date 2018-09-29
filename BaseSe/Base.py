# coding:utf-8
# @author : csl
# @date   : 2018/08/29 09:42
# Selenium以外的基础方法

from PIL import Image
import requests

class Base_image_move_distance(object):
    """
    v1.0
    date : 2018/08/10
    登录页面获取极验滑块验证码滑动距离类
    处理方式：暂时将无缺口的原图保存在本地，通过有缺口的截图同原图对比方式获得滑动位移距离
    :param   login_image_path="E:\DKpc_test\Data\Image\quekou.png"
    :return  lens
    
    v1.1
    date : 2018/09/29
    优化登录滑块处理方式：
    页面弹出滑块验证后，修改页面JS隐藏缺口及滑块，截图保存作为对照；修改页面JS还原缺口及滑块，截图保存后计算对比缺口位移
    :param   截图：login_image_path="E:\DKpc_test\Data\Image\quekou.png";  对照：login_image_path_control_path
    :return  lens
    """

    def __init__(self, login_image_path="E:\DKpc_test\Data\Image\quekou.png"):
        try:
            self.login_image_path = login_image_path
            # 打开原图
            self.original_image_1 = Image.open("E:\DKpc_test\Data\Image\OriginalImage\OriginalImage_1.png")
            self.original_image_2 = Image.open("E:\DKpc_test\Data\Image\OriginalImage\OriginalImage_2.png")
            self.original_image_3 = Image.open("E:\DKpc_test\Data\Image\OriginalImage\OriginalImage_3.png")
            self.original_image_4 = Image.open("E:\DKpc_test\Data\Image\OriginalImage\OriginalImage_4.png")
            self.original_image_5 = Image.open("E:\DKpc_test\Data\Image\OriginalImage\OriginalImage_5.png")
            self.original_image_6 = Image.open("E:\DKpc_test\Data\Image\OriginalImage\OriginalImage_6.png")
            self.original_image_list = [self.original_image_1, self.original_image_2, self.original_image_3, self.original_image_4, self.original_image_5, self.original_image_6]
            # print(self.original_image_list)
            self.login_image = Image.open(self.login_image_path)
            # print(self.login_image)
        except Exception as e:
            print("图片打开失败：{}".format(e))

    def move_distance(self):
        """
        极验验证滑块滑动距离处理
        :return lens = 缺口位置 - 起始位置
        """
        orimage = self.contrast_OriginalImage()
        lens = self.get_diff_location(self.login_image, orimage)
        return lens - 827 - 5  # -10为根据实际定位效果往回退10个像素

    def contrast_OriginalImage(self):
        """
        截图同原图对照，获得原图
        :return original_image_list
        返回原图对象
        """
        try:
            for i in self.original_image_list:
                # 对比两张图片同一点位上的像素值大小
                pixel1 = self.login_image.getpixel((1045, 344))
                pixel2 = i.getpixel((1045, 344))
                # pixel[0]代表R值，pixel[1]代表G值，pixel[2]代表B值
                if abs(pixel1[0] - pixel2[0]) < 5 and abs(pixel1[1] - pixel2[1] < 5) and abs(pixel1[2] - pixel2[2] < 5):
                    return i
        except Exception as e:
            print("未匹配到原图：{}".format(e))
            return False


    def get_diff_location(self, image1,image2):
        """
        计算位移距离
        （880,1082）（385,420）为滑块图片区域，可能会受到一些清晰度的影响，可根据实际情况修改
        :return x 像素点横坐标
        """
        for i in range(882,1082):
            for j in range(385,420):
                #遍历原图与缺口图像素值寻找缺口位置
                if self.is_similar(image1,image2,i,j)==False:
                   return i
        return -1


    def is_similar(self, image1,image2,x,y):
        """
        对比RGB值，如果两个点RGB值相似度超过50，返回两个点不相同False，否则返回两个点相同True
        :return False or True
        """
        pixel1 = image1.getpixel((x, y))
        pixel2 = image2.getpixel((x, y))
        # 截图像素也许存在误差，50作为容差范围
        if abs(pixel1[0]-pixel2[0])>=10 and abs(pixel1[1]-pixel2[1])>=10 and abs(pixel1[2]-pixel2[2])>=10:
            return False
        return True

    def get_tracks(self, distance):
        '''
        拿到移动轨迹，模仿人的滑动行为，先匀加速后匀减速
        匀变速运动基本公式：
        ①v=v0+at
        ②s=v0t+½at²
        ③v²-v0²=2as
        :param distance: 需要移动的距离
        :return: 存放每0.3秒移动的距离
        '''
        # 初速度
        v = 0
        # 单位时间为0.2s来统计轨迹，轨迹即0.2内的位移
        t = 0.3
        # 位移/轨迹列表，列表内的一个元素代表0.2s的位移
        tracks = []
        # 当前的位移
        current = 0
        # 到达mid值开始减速
        mid = distance * 4 / 5

        while current < distance:
            if current < mid:
                # 加速度越小，单位时间的位移越小,模拟的轨迹就越多越详细
                a = 2
            else:
                a = -3

            # 初速度
            v0 = v
            # 0.2秒时间内的位移
            s = v0 * t + 0.5 * a * (t ** 2)
            # 当前的位置
            current += s
            # 添加到轨迹列表
            tracks.append(round(s))

            # 速度已经达到v,该速度作为下次的初速度
            v = v0 + a * t
        return tracks


if __name__ == "__main__":
    print(Base_image_move_distance().move_distance())
    dd = Base_image_move_distance().get_tracks(85)
    print(dd)
    r = 0
    for x in dd:
        r += x
    print(r)
    # 5 12 15 24 25 8