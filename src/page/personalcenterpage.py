'''
__author__:'shimengqi'
__description__:'个人中心页面'
__mtime_:2018/8/22
'''
import elementoperate
from  appium_config import DriverClient
import wechataction
import openurl


driver=DriverClient.driver
class PersonalCenterPage():
    def __init__(self):
        self.driver=driver
        self.EO=elementoperate.ElementOperate(self.driver)

    def enterHomePage(self):
        '''进入主页'''
        ele=self.EO.find_element(('xpath','//*[@id="wmContainer"]/div[1]/div[1]/div[1]/div[1]/a'))
        ele.click()

    def enterShoppingcar(self):
        '''进入购物车'''
        ele=self.EO.find_element(('xpath','//*[@id="wmContainer"]/div[1]/div[1]/div[1]/ul/li[2]/a'))
        ele.click()
    def orderList_ele(self):
        # 展开查看所有订单
        ele=self.EO.find_element(('xpath','//*[@id="wmContainer"]/div[2]/div/div[2]/div[1]/i'))
        return ele

    def withoutPay_ele(self):
        # 待付款订单
        ele=self.EO.find_element(('xpath','//*[@id="wmContainer"]/div[2]/div/div[2]/div[2]/div[1]'))
        element=self.driver.find_elements_by_class_name('ws-m-goods-sku-list-item')
        return ele

    def withoutPayNum(self):
        # 待付款订单数目
        ele=self.EO.find_element(('xpath','//*[@id="wmContainer"]/div[2]/div/div[2]/div[2]/div[1]/div[2]'))
        num=ele.text
        return num

    def withoutSend_ele(self):
        # 待发货订单
        ele=self.EO.find_element(('xpath','//*[@id="wmContainer"]/div[2]/div/div[2]/div[2]/div[2]'))
        return ele

    def withoutSendNum(self):
        # 待发货订单数目
        ele=self.EO.find_element(('xpath','//*[@id="wmContainer"]/div[2]/div/div[2]/div[2]/div[2]/div[2]'))
        num=ele.text
        return num

    def withoutReceive_ele(self):
        # 待收货订单
        ele=self.EO.find_element(('xpath','//*[@id="wmContainer"]/div[2]/div/div[2]/div[2]/div[3]'))
        return ele

    def withoutReceiveNum(self):
        # 待收货订单数目
        ele=self.EO.find_element(('xpath','//*[@id="wmContainer"]/div[2]/div/div[2]/div[2]/div[3]/div[2]'))
        return ele

    def refound_ele(self):
        # 售后订单
        ele=self.EO.find_element(('xpath','//*[@id="wmContainer"]/div[2]/div/div[2]/div[2]/div[4]'))
        return ele

    def cart_ele(self):
        # 会员卡按钮
        ele=self.EO.find_element(('xpath','//*[@id="wmContainer"]/div[2]/div/div[3]/div[1]/i'))
        return ele

    def coupon_ele(self):
        # 优惠券按钮
        ele=self.EO.find_element(('xpath','//*[@id="wmContainer"]/div[2]/div/div[3]/div[2]/i'))
        return ele

    def address_ele(self):
        # 收货地址按钮
        ele=self.EO.find_element(('xpath','//*[@id="wmContainer"]/div[2]/div/div[3]/div[3]/i'))
        return ele

def main():
    Wechat=wechataction.WechatAction(driver)
    Page=openurl.pageAction(driver)

    p=PersonalCenterPage()
    Wechat.wechatLogin()
    Page.opentestPage()
    Page.enterPersonalCentrol()





