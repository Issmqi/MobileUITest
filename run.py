from appium_config import DriverClient
import time
import log
import wechataction
import openurl
from testrunner import TestAllCase
import HTMLTestRunner

Log=log.Log()
driver = DriverClient().getDriver()
Wechat=wechataction.WechatAction(driver)
Page=openurl.pageAction(driver)

class Running():
    def run(self):
        Wechat.wechatLogin()
        Page.opentestPage()
        Log.info("开始测试")
        start = time.time()
        start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(start))
        Log.info("当前时间是%s" % start_time)
        now = time.strftime("%Y-%m-%d %H_%M_%S", time.localtime())
        resultpath = "C:\\python\\MobileUItest\\result\\report\\" + now + "_result.html"
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



def main():
    running=Running()
    running.run()
if __name__ == '__main__':
    main()



