import unittest
from appium_config import DriverClient
import time
import log
import wechataction
import openurl
import HTMLTestRunner
import sys,os
driver = DriverClient().getDriver()
Log=log.Log()
Wechat=wechataction.WechatAction(driver)
Page=openurl.pageAction(driver)

class TestAllCase:
    def testsuit(self):
        suite=unittest.TestSuite()
        suite.addTests(unittest.TestLoader().loadTestsFromName('goodsdetailtest.GoodsDetailTset'))
        suite.addTests(unittest.TestLoader().loadTestsFromName('shoppingcarttest.ShoppingCartTest'))
        return suite
        # now = time.strftime("%Y-%m-%d %H_%M_%S", time.localtime())
        # resultpath = "D:\\work\\MobileUItest\\result\\report\\" + now + "_result.html"
        # fp = open(resultpath, 'wb')
        # runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title=u'h5测试报告',description=u'用例执行情况：')
        # runner.run(suite)
        # fp.close()

def main():
    Wechat.wechatLogin()
    Page.opentestPage()
    Log.info("开始测试")
    start = time.time()
    start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(start))
    Log.info("当前时间是%s" % start_time)
    now = time.strftime("%Y-%m-%d %H_%M_%S", time.localtime())
    resultpath = "D:\\work\\MobileUItest\\result\\report\\" + now + "_result.html"
    fp = open(resultpath, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u'h5测试报告', description=u'用例执行情况：')
    runner.run(TestAllCase().testsuit())
    fp.close()
    # Runner = TestAllCase()
    # Runner.testsuit()
    end = time.time()
    end_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(start))
    Log.info("当前时间是%s" % end_time)
    Log.info("耗时是%s" % (end - start))
    Log.info("测试完毕")


if __name__ == '__main__':
    main()








