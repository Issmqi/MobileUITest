import shoppingcartpage
import unittest
import  initappdriver
import openurl
import wechataction
import log
import basepage
from appium_config import DriverClient
driver = DriverClient().getDriver()

Log=log.Log()
# appdriver=initappdriver.InitAppdriver()
# driver=appdriver.setdriver()

wechat=wechataction.WechatAction(driver)
page=openurl.pageAction(driver)

BasePage=basepage.BasePage(driver)
cart=shoppingcartpage.ShoppingcartPage(driver)

class ShoppingCartTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        page.enterShopingCart()
        Log.debug("*************开始测试购物车*************")

    @classmethod
    def tearDownClass(self):
        Log.debug("*************购物车测试完成*************")
        cart.enterHomePage()
        # driver.quit()

    def setUp(self):
        Log.debug("开始执行测试用例!")

    def tearDown(self):
        Log.debug("测试用例执行完成！")

    def test_SelectAll(self):
        '''点击所有可选sku后全选按钮选中'''
        cart.selectAllSku()
        cart.checkSelectAll()
        self.assertEqual(cart.checkSelectAll(),"true","选择所有sku后全选按钮自动选中")

    def test_TotalMoney(self):
        '''计算结算金额是否正确'''
        calMoneyTotal=cart.validItem_totalmoney()
        totalMoney=cart.getMoneyTotal()
        self.assertEqual(calMoneyTotal,totalMoney,"合计金额正确")




if __name__=='__main__':
    unittest.main()








