import unittest
# import initappdriver
import openurl
import goodsdetailpage
import log
import wechataction
import basepage
from appium_config import DriverClient
driver = DriverClient().getDriver()

Log=log.Log()
Wechat=wechataction.WechatAction(driver)
Page = openurl.pageAction(driver)
GoodsDetailPage = goodsdetailpage.GoodsDetailPage(driver)
BasePage=basepage.BasePage(driver)


class GoodsDetailTset(unittest.TestCase):


    @classmethod
    def setUpClass(self):
        GoodsDetailPage = goodsdetailpage.GoodsDetailPage(driver)
        BasePage = basepage.BasePage(driver)
        Page.enterGoodsDetail()
        Log.debug("*************开始测试商详页面*************")

    @classmethod
    def tearDownClass(self):
        Log.debug("*************商详页面测试结束！*************")
        GoodsDetailPage.enterHomePage()
        # driver.quit()

    def setUp(self):
        Log.debug("开始执行测试用例！")

    def tearDown(self):
        Log.debug("测试用例执行完成")
        driver.refresh()

    def test_getCoupon_emptystock(self):
        '''测试优惠券库存为空，即第一个优惠券'''
        GoodsDetailPage.getCoupon(1)
        self.assertEqual(GoodsDetailPage.getNotifications(),"优惠券已被领光")

    def test_getCoupon_reachlimit(self):
        '''测试已达到优惠券上限，即第二个优惠券'''
        GoodsDetailPage.getCoupon(2)
        self.assertEqual(GoodsDetailPage.getNotifications(),"超出限领额")
    def test_getCoupon_success(self):
        '''测试领取优惠券成功，即第三个优惠券'''
        GoodsDetailPage.getCoupon(3)
        self.assertEqual(GoodsDetailPage.getNotifications(), "领取成功")

    def test_getPromotion(self):
        '''打开促销详情'''
        GoodsDetailPage.getPromotion()

    def test_addShoppingcart(self):
        '''测试加入购物车'''
        GoodsDetailPage.addShoppingCart()
        self.assertEqual(GoodsDetailPage.getNotifications(),"添加购物车成功")

    def test_PurchaseGoods(self):
        '''测试立即购买'''
        GoodsDetailPage.buyNow()
        # self.assertTrue(GoodsDetailPage.checkBuy())
        # GoodsDetailPage.returnGoosGetail()



def main():
    GoodsDetailTset()

if __name__=='__main__':
    main()






