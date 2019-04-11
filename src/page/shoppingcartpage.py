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

class ShoppingcartPage():

    def __init__(self, driver):
        self.driver = driver
        self.Scroll = scrollaction.ScrollAction(driver)
        self.EO=elementoperate.ElementOperate(driver)

    def getItemNum(self):
        '''
        获取购物车中sku个数
        :return:
        '''
        time.sleep(10)
        elements = self.driver.find_elements_by_class_name('ws-m-goods-sku-list-item')
        itemNum = len(elements)
        Log.debug("购物车中有%s个商品"%itemNum)
        return itemNum

    def skuSelectBtn_ele(self, i):
        '''

        :return: 购物车中第i个商品前复选框
        '''
        # elements=self.driver.find_elements_by_class_name('select-btn')

        path = '//*[@id="wmContainer"]/div/div[2]/div[1]/div/ul/li[' + str(i) + ']/div/div[1]'
        # print('这是第', i, '个商品的xpath', path)
        element = self.EO.find_element(('xpath',path))
        return element

    def skuCheckbox_ele(self,i):
        '''购物车中第i个商品前复选框icon'''
        # 商品根目录
        path = '//*[@id="wmContainer"]/div/div[2]/div[1]/div/ul/li[' + str(i) + ']'
        element=self.EO.find_element(('xpath',path)).find_element_by_tag_name("input")
        return element



    def skuAddBtn_ele(self):
        '''第一个sku数量减少按钮'''
        element = self.driver.find_element_by_xpath(
            '//*[@id="wmContainer"]/div/div[2]/div[1]/div/ul/li[1]/div/div[3]/div[3]/div[2]/div/div[1]/button')
        return element

    def skuQuantityEdit_ele(self,i):
        '''第i个sku数量输入框'''
        path='//*[@id="wmContainer"]/div/div[2]/div[1]/div/ul/li['+str(i)+']/div/div[3]/div[3]/div[2]/div/div[2]/input'
        element = self.driver.find_element_by_xpath(path)
        return element

    def skuMinusBtn_ele(self):
        '''第一个sku数量增加按钮'''
        element = self.driver.find_element_by_xpath(
            '//*[@id="wmContainer"]/div/div[2]/div[1]/div/ul/li[1]/div/div[3]/div[3]/div[2]/div/div[3]/button')
        return element

    def skuDelBtn_ele(self):
        '''第一个sku删除按钮'''
        element = self.driver.find_element_by_xpath(
            '//*[@id="wmContainer"]/div/div[2]/div[1]/div/ul/li[1]/div/div[3]/div[4]')
        return element

    def getSkuQuantity(self,i):
        '''第i个商品数量'''
        text=self.skuQuantityEdit_ele(i).get_attribute("value")
        quantity=int(text)
        # Log.debug("第%s个商品的数量是%s"%(i,quantity))
        return quantity


    def getSkuPrice_text(self,i):
        '''第i个商品价格'''
        path='//*[@id="wmContainer"]/div/div[2]/div[1]/div/ul/li['+str(i)+']/div/div[3]/div[3]/div[1]/div/span[2]'
        # path='//*[@id="wmContainer"]/div/div[2]/div[1]/div/ul/li['+str(i)+']/div/div[3]/div[3]/div[1]'
        element=self.EO.find_element(('xpath',path)).text
        price=float(element)
        # Log.debug("第%s个商品的价格是%s"%(i,element))
        return price


    def selectAllBtn_ele(self):
        '''全选按钮'''
        element=self.EO.find_element(('xpath','//*[@id="wmContainer"]/div/div[2]/div[2]/div[1]'))
        # element = self.driver.find_element_by_xpath('//*[@id="wmContainer"]/div/div[2]/div[2]/div[1]')
        return element
    def selectAllChechbox_ele(self):
        '''全选按钮前复选框icon'''
        element=self.selectAllBtn_ele().find_element_by_tag_name("input")
        return element

    def getMoneyTotal(self):
        element=self.driver.find_element_by_xpath('//*[@id="wmContainer"]/div/div[2]/div[2]/div[2]/p[1]/span[2]').text
        MoneyTotal=float(element)
        Log.debug("结算合计金额是%s"%MoneyTotal)
        return MoneyTotal

    def checkoutBtn_ele(self):
        '''结算按钮'''
        element = self.driver.find_element_by_xpath('//*[@id="wmContainer"]/div/div[2]/div[2]/button')
        return element

    def alertCofirmBtn_ele(self):
        '''alert确定按钮'''
        element = self.driver.find_element_by_xpath('/html/body/div[3]/div/div[2]/button[1]')
        return element

    def alertCancelBtn_ele(self):
        '''alert取消按钮'''
        element = self.driver.find_element_by_xpath('/html/body/div[3]/div/div[2]/button[2]')
        return element

    def getSkuNum_total(self):
        '''
        计算购物车中sku总数
        :return:
        '''
        num=self.getItemNum()
        total=0
        for i in range(1,num+1):
            quantity=self.getSkuQuantity(i)
            total=total+quantity
        Log.debug("购物车中sku总数是%s"%total)
        return total


    def validItem_totalmoney(self):
        '''
        计算购物车中选中sku总额
        :return:
        '''
        num=self.getItemNum()
        money = float(0.00)
        print(money)
        for i in range(1,num+1):
            price=self.getSkuPrice_text(i)
            quantity=self.getSkuQuantity(i)
            ele_checkbox=self.skuCheckbox_ele(i)

            if ele_checkbox.get_attribute("checked")=="true":
                money=money+price*quantity
            self.Scroll.scroll_by(112)
        Log.debug("购物车中已选中sku总额是%s"%money)
        # money=round(money,2)
        return money

    def selectAllSku(self):
        '''
        点击购物车中所有sku前选中按钮
        :return:
        '''
        num = self.getItemNum()
        for i in range(1, num + 1):
            ele = self.skuSelectBtn_ele(i)
            ele_checkbox=self.skuCheckbox_ele(i)
            # 复选框未禁用且未选中
            if ele_checkbox.get_attribute("disabled") == "true":
                Log.debug("购物车中第" + str(i) + "个商品已失效")
                self.Scroll.scroll_by(112)
                continue
            if ele_checkbox.get_attribute("checked") == "true":
                Log.debug("购物车中第" + str(i) + "个商品已选中")
                self.Scroll.scroll_by(112)
                continue
            else:
                ele.click()
                time.sleep(20)
                self.Scroll.scroll_by(112)



    def checkSelectAll(self):
        '''判断全选按钮选中状态'''
        selectAllChechbox=self.selectAllChechbox_ele()
        return selectAllChechbox.get_attribute("checked")

    def selectAll(self):
        '''
        点击全选按钮
        :return:
        '''
        selectAllBtn = self.selectAllBtn_ele()
        selectAllBtn.click()


    def skuNumEdit(self,i):
        '''第i个sku输入框编辑操作'''
        skuEdit = self.skuQuantityEdit_ele(i)
        skuEdit.clear()
        skuEdit.send_keys('5')

    def Add_Minus(self):
        self.skuMinusBtn_ele()
        self.skuAddBtn_ele()

    def enterHomePage(self):
        time.sleep(3)
        element = self.EO.find_element(('xpath', '//*[@id="wmContainer"]/div/div[1]/div[1]/div[1]/div[1]/a'))
        # element = self.EO.find_element(('xpath', '//*[@id="wmContainer"]/ul/li[1]/div/div[1]/div[1]/div[1]/a'))
        element.click()

    def enterPersonalCenter(self):
        element = self.EO.find_element(('xpath','//*[@id="wmContainer"]/div/div[1]/div[1]/div[1]/ul/li[1]/a'))
        element.click()

    def enterShippingcart(self):
        element = self.EO.find_element(('xpath', '//*[@id="wmContainer"]/div/div[1]/div[1]/div[1]/ul/li[2]/a'))
        element.click()





def main():
    appdriver = initappdriver.InitAppdriver()
    driver = appdriver.setdriver()
    wechat = wechataction.WechatAction(driver)
    wechat.wechatLogin()
    page = openurl.pageAction(driver)
    page.opentestPage()
    page.enterShopingCart()
    a = ShoppingcartPage(driver)
    # a.selectAllSku()
    a.getMoneyTotal()
    a.validItem_totalmoney()
    # a.getSkuPrice_text(2)


if __name__ == '__main__':
    main()
