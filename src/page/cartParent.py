'''
__author__:'shimengqi'
__description__:'购物车页面'
__mtime_:2018/7/30
'''
import time

import initappdriver
import openurl
import scrollaction
import wechataction
import log
import elementoperate

Log=log.Log()
appdriver=initappdriver.InitAppdriver()

class cartParent():

    def __init__(self,driver):
        # self.driver = appdriver.setdriver()
        self.driver=driver
        self.Scroll = scrollaction.ScrollAction(self.driver)
        self.EO=elementoperate.ElementOperate(self.driver)

    def getItemNum(self):
        '''
        获取购物车中sku个数
        :return:
        '''
        time.sleep(10)
        elements = self.driver.find_elements_by_class_name('ws-m-goods-sku-list-item')
        itemNum = len(elements)
        print('商品数量是', itemNum)
        return itemNum

    def item(self,i):
        '''
        获取商品的根节点
        :param i:
        :return:
        '''
        path='//*[@id="wmContainer"]/div/div[2]/div[1]/div/ul/li['+str(i)+']'
        element=self.EO.find_element(('xpath',path))
        return element

    def skuSelectBtn_ele(self,i):
        element=self.item(i).find_element_by_xpath("/div/div[1]")
        return element

    def skuCheckbox_ele(self,i):
        element = self.item(i).find_element_by_tag_name("input")
        return element

    def getCheckboxAttr(self,i):
        print(self.skuCheckbox_ele(i).get_attribute("disabled"))
        print(self.skuCheckbox_ele(i).get_attribute("checked"))




def main():
    appdriver = initappdriver.InitAppdriver()
    driver = appdriver.setdriver()
    wechat = wechataction.WechatAction(driver)
    wechat.wechatLogin()
    page = openurl.pageAction(driver)
    page.opentestPage()
    page.enterShopingCart()
    a = cartParent(driver)
    # a.skuSelectBtn_ele(1).click()
    a.getCheckboxAttr(1)




if __name__ == '__main__':
    main()
