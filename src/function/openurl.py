'''
__author__:'shimengqi'
__description__:'进入不同页面’
__mtime_:2018/7/18
'''
import time

import initappdriver
import log
import wechataction
import elementoperate
import basepage

Log = log.Log()



class pageAction():
    def __init__(self, driver):
        self.driver = driver
        self.EO = elementoperate.ElementOperate(driver)

    def opentestPage(self):
        '''
        在聊天窗口中打开指定url，切换webiew
        :return:
        '''
        # 搜索文件传输助手
        search=self.EO.find_element(('accessibility id','搜索'))
        search.click()
        searchRe=self.EO.find_element(('id','com.tencent.mm:id/hk'))
        searchRe.send_keys("文件")
        time.sleep(3)
        # 打开聊天窗口
        self.driver.find_element_by_id("com.tencent.mm:id/k_").click()
        time.sleep(3)
        # 点击聊天窗口中的链接
        # self.driver.find_element_by_id("com.tencent.mm:id/j_").click()
        self.driver.find_element_by_id("com.tencent.mm:id/nu").click()
        time.sleep(10)
        # 打开h5链接，切换webview
        self.driver.switch_to.context('WEBVIEW_com.tencent.mm:tools')  # 切换进入webview
        time.sleep(10)
        all_handles = self.driver.window_handles
        # print(len(all_handles))
        for handle in all_handles:
            try:
                self.driver.switch_to_window(handle)
                # print("在句柄中查找购物车按钮")
                self.driver.find_element_by_xpath('//*[@id="wmContainer"]/ul/li[1]/div/div[1]/div[1]/ul/li[2]/a')
                Log.debug("句柄切换成功")
                break

            except Exception as e:
                Log.debug("寻找句柄中")

    def enterhomePage(self):
        try:
            homePageBtn=self.EO.find_element(
                ('xpath','//*[@id="wmContainer"]/div[1]/div[1]/div[1]/div[1]/a'))

            homePageBtn.click()
            Log.debug("进入到主页！")
        except:
            Log.debug("进入主页失败！")

    def enterPersonalCentrol(self):
        '''进入个人中心页面'''
        # self.driver.find_element_by_xpath('//*[@id="wmContainer"]/ul/li[1]/div/div[1]/div[1]/ul/li[1]/a').click()
        try:
            PersonalCentrol = self.EO.find_element(
                ('xpath', '//*[@id="wmContainer"]/ul/li[1]/div/div[1]/div[1]/ul/li[1]/a'))
            PersonalCentrol.click()
            Log.debug("进入到个人中心页面！")
        except:
            Log.error("进入个人中心失败！")

    def enterShopingCart(self):
        '''进入购物车页面'''
        try:
            catrbutton = self.EO.find_element(('xpath', '//*[@id="wmContainer"]/ul/li[1]/div/div[1]/div[1]/ul/li[2]/a'))
            catrbutton.click()
            Log.debug("进入到购物车页面！")
        except:
            Log.error("进入购物车失败！")
        # self.driver.find_element_by_xpath('//*[@id="wmContainer"]/ul/li[1]/div/div[1]/div[1]/ul/li[2]/a').click()

    def enterGoodsDetail(self):
        '''进入商详页面'''
        # 单个sku商品岁岁平安
        # self.driver.find_element_by_xpath('//*[@id="wmContainer"]/ul/li[4]/div/div/div[1]/ul/li[1]/a').click()
        # 多个一层sku商品黑森林
        goodsPriceStr=self.driver.find_element_by_xpath('//*[@id="wmContainer"]/ul/li[4]/div/ul/li[4]/a/div[2]/p[2]').text
        goodsPrice=goodsPriceStr[1:]
        print(goodsPrice)
        goodsName = self.driver.find_element_by_xpath('//*[@id="wmContainer"]/ul/li[4]/div/ul/li[4]/a/div[2]/p[1]').text
        print(goodsName)
        try:
            self.EO.find_element(('xpath', '//*[@id="wmContainer"]/ul/li[4]/div/ul/li[4]/a')).click()
            Log.debug("进入商品%s详情"%goodsName)

        except:
            Log.debug("进入商品%s详情失败！"%goodsName)
        return goodsPrice

    def swipeUP(self):

        width = self.driver.get_window_size()['width']
        height = self.driver.get_window_size()['height']

        # while循环10次
        i = 0
        while i < 10:
            try:
                self.driver.find_element_by_xpath("path").click()  # 尝试点击元素
                break
            except Exception as e:
                self.driver.swipe(width / 2, height * 0.8, width / 2, height * 0.2)  # 滑动屏幕
                i = i + 1

def main():
    appdriver = initappdriver.InitAppdriver()
    driver = appdriver.setdriver()
    wechatLogin = wechataction.WechatAction(driver)
    BasePage = basepage.BasePage(driver)
    wechatLogin.wechatLogin()
    a = pageAction(driver)
    a.opentestPage()
    # a.enterShopingCart()
    a.enterGoodsDetail()
    time.sleep(20)
    BasePage = basepage.BasePage(driver)
    BasePage.homepage_ele().click()
    time.sleep(10)


if __name__ == '__main__':
    main()
