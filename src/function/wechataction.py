'''
__author__:'shimengqi'
__description__:'微信操作'
__mtime_:2018/7/17
'''

import time
import initappdriver
from appium_config import DriverClient
import log
import elementoperate

Log = log.Log()


class WechatAction():
    def __init__(self, driver):
        self.driver = driver
        self.EO=elementoperate.ElementOperate(driver)

    def wechatLogin(self):

        try:
            # pwd = self.driver.find_element_by_id("com.tencent.mm:id/hk")
            pwd=self.EO.find_element(('id','com.tencent.mm:id/hk'))
            pwd.click()
            pwd.send_keys("***")
            # loginBtn = self.driver.find_element_by_id("com.tencent.mm:id/bvq")
            loginBtn=self.EO.find_element(('id','com.tencent.mm:id/bvq'))
            loginBtn.click()
            Log.debug("微信登录成功")
        except:
            Log.debug("微信已登录，请直接操作！")

    def wechatLogout(self):
        personalCentral = self.driver.find_element_by_android_uiautomator(
            'new UiSelector().className("android.widget.RelativeLayout")[4])')
        personalCentral.click()
        time.sleep(10)
        setIcon = self.driver.find_element_by_id("com.tencent.mm:id/a91")
        setIcon.click()
        logoutButton = self.driver.find_element_by_id("android:id/title")
        logoutButton.click()


def main():
    # appdriver = initappdriver.InitAppdriver()
    # driver = appdriver.setdriver()
    driver = DriverClient.getDriver()
    a = WechatAction(driver)

    a.wechatLogin()
    # a.wechatLogout()


if __name__ == '__main__':
    main()
