'''
__author__:'shimengqi'
__description__:'商详页面'
__mtime_:2018/7/27
'''

import time

import basepage
import elementoperate
from appium_config import DriverClient
import log
import openurl
import wechataction
import scrollaction
import orderconfirmpage

Log=log.Log()



class GoodsDetailPage():
    '''商详页面'''

    def __init__(self, driver):
        self.driver = driver
        self.Page = openurl.pageAction(self.driver)
        self.EO=elementoperate.ElementOperate(self.driver)
        self.BasePage=basepage.BasePage(self.driver)
        self.ConfirmPage=orderconfirmpage.OrderConfirmPage(self.driver)
        self.Scroll=scrollaction.ScrollAction(self.driver)


    def mainPtoto_ele(self):
        '''商品图片'''
        elemrnt = self.driver.find_element_by_xpath('//*[@id="js-product-images-container"]')
        return elemrnt

    def goodsprice_ele(self):
        goodsPriceStr=self.driver.find_element_by_xpath('//*[@id="wmContainer"]/div[2]/div[2]/div[2]/span[1]').text
        goodsPrice=goodsPriceStr[1:]
    def promotion_and_sku(self):
        element = self.driver.find_element_by_xpath('//*[@id="wmContainer"]/div[2]/div[3]')
        return element

    def couponList_ele(self):
        '''优惠券列表'''
        element=self.EO.find_element(('xpath','//*[@id="wmContainer"]/div[2]/div[3]/div[1]/div[2]/div[1]'))
        return element

    def Coupon_ele(self,i):
        '''列表中第i个优惠券'''
        path='//*[@id="wmContainer"]/div[2]/div[3]/div[1]/div[2]/div[2]/div/div[2]/ul/li['+str(i)+']/div/div[1]/div[3]/button'
        # element=self.driver.find_element_by_xpath(path)
        element=self.EO.find_element(('xpath',path))
        return element

    def couponClose_ele(self):
        '''关闭优惠券列表'''
        element=self.EO.find_element(('xpath','//*[@id="wmContainer"]/div[2]/div[3]/div[1]/div[2]/div[2]'))
        return element

    def promotionList_ele(self):
        '''活动列表'''
        element=self.EO.find_element(('xpath','//*[@id="wmContainer"]/div[2]/div[3]/div[2]/div[2]/div[1]'))
        return element

    def promotionClose_ele(self):
        '''关闭活动列表'''
        element=self.EO.find_element(('xpath','//*[@id="wmContainer"]/div[2]/div[3]/div[2]/div[2]/div[2]'))
        return element

    def skuSelector_ele(self):
        '''sku选择器'''
        element=self.EO.find_element(('xpath','//*[@id="js-sku-selector-line"]/i'))
        return element

    def skuTypeNum(self):
        '''获取sku层级数目'''
        elements = self.driver.find_elements_by_class_name('ws-m-sku-values')
        skuTypeNum = len(elements)
        # print('sku层级数是：',skuTypeNum)
        return skuTypeNum

    def skuValueFirst_ele(self, i):
        '''sku选择器中每个层级中第一个sku'''
        path = '//*[@id="js-ws-selector"]/div[2]/div[2]/div[' + str(i * 2) + ']/span[1]'
        element=self.EO.find_element(('xpath',path))
        return element

    def skuSelectorClose_ele(self):
        '''sku选择器关闭按钮'''
        element = self.driver.find_element_by_xpath('//*[@id="js-ws-selector"]/div[2]/div[1]/span')
        return element

    def goodsdetail_ele(self):
        '''商品详情'''
        element = self.driver.find_element_by_xpath('//*[@id="wmContainer"]/div[2]/div[4]')

    def customerSer_ele(self):
        '''客服按钮'''
        element = self.driver.find_element_by_xpath('//*[@id="wmContainer"]/div[3]/div[1]')
        return element

    def addshoppingCartButton_ele(self):
        '''加入购物车按钮'''
        element=self.EO.find_element(('xpath','//*[@id="wmContainer"]/div[3]/div[2]/div[1]'))
        return element

    def buyButton_ele(self):
        '''立即购买按钮'''

        element=self.EO.find_element(('xpath','//*[@id="wmContainer"]/div[3]/div[2]/div[2]'))
        # element = self.driver.find_element_by_xpath('//*[@id="wmContainer"]/div[3]/div[2]/div[2]')
        return element


    def getNotifications(self):
        '''获取div弹窗内容'''

        Notification_ele=self.EO.find_element(('class name','wm-notifications'))
        Notification=Notification_ele.text
        return Notification

    def getCoupon(self,i):
        '''领取优惠券操作'''
        self.couponList_ele().click()
        self.Coupon_ele(i).click()


    def getPromotion(self):
        '''展开促销活动详情'''
        self.Scroll.scrollup_by_element(self.promotionList_ele())
        self.promotionList_ele().click()
        print("展开活动详情")
        # self.promotionClose_ele().click()

    def scroll(self):
        self.driver.execute_script("window.scrollBy(0, 700)")
    def selectFirstSku(self):
        '''
        点击sku选择器中每个层级第一个sku值
        :return:
        '''
        num=self.skuTypeNum()
        for i in range(1,num+1):
            ele=self.skuValueFirst_ele(i)
            ele.click()


    def getSkuList(self):
        '''打开sku选择器'''
        self.skuSelector_ele().click()

    def addShoppingCart(self):
        '''加入购物车操作'''
        self.addshoppingCartButton_ele().click()
        self.selectFirstSku()
        self.addshoppingCartButton_ele().click()

    def buyNow(self):
        '''立即购买操作'''
        openSku = self.buyButton_ele()
        # 打开sku选择器
        openSku.click()
        self.selectFirstSku()
        time.sleep(3)
        buyButton = self.buyButton_ele()
        # 点击立即购买
        buyButton.click()
        time.sleep(10)
        self.ConfirmPage.homepage_ele().click()
        time.sleep(10)
        self.Page.enterGoodsDetail()

    def returnGoosGetail(self):
        self.BasePage.homepage_ele().click()
        self.Page.enterGoodsDetail()

    def checkBuy(self):
        try:
            self.driver.find_element_by_xpath('//*[@id="wmContainer"]/div[2]/div[2]/div[1]/i')
            return True
        except:
            return False

    def enterHomePage(self):
        element=self.EO.find_element(('xpath','//*[@id="wmContainer"]/div[1]/div/div[1]/div[1]/div[1]/a'))
        # element=self.EO.find_element(('xpath','//*[@id="wmContainer"]/div[1]/div/div[1]/div[1]/div[1]/a'))
        element.click()

    def enterPersonalCenter(self):
        element = self.EO.find_element(('xpath','//*[@id="wmContainer"]/div[1]/div/div[1]/div[1]/ul/li[1]/a'))
        element.click()

    def enterShippingcart(self):
        element = self.EO.find_element(('xpath', '//*[@id="wmContainer"]/div[1]/div/div[1]/div[1]/ul/li[2]/a'))
        element.click()



def main():
    # appdriver=initappdriver.InitAppdriver()
    # driver = appdriver.setdriver()
    driver=DriverClient.getDriver()
    wechat = wechataction.WechatAction(driver)
    wechat.wechatLogin()
    page = openurl.pageAction(driver)
    page.opentestPage()
    page.enterGoodsDetail()
    a = GoodsDetailPage(driver)


    # a.getCoupon()
    # target = a.promotion_and_sku()
    # scroll.scroll_by_element(target)
    # a.getPromotion()
    # time.sleep(10)
    # driver.refresh()
    # a.getSkuList()
    # driver.refresh()
    # a.addShoppingCart()
    # Log.debug("加入购物车成功")
    a.buyNow()





if __name__ == '__main__':
    main()
