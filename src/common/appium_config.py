'''
__author__:'shimengqi'
__description__:'重新封装driver为单例模式，避免重复打开微信页面'
__mtime_:2018/8/21
'''

from appium import webdriver
import log

Log=log.Log

class Singleton(object):
    driver = None
    def __new__(cls, *args, **kw):
        if not hasattr(cls, '_instance'):
            orig = super(Singleton, cls)
            # Log.info('-----------------------init driver----------------------')
            config = {
                'platformName': 'Android',
                'platformVersion': '4.4.4',
                'deviceName': 'OPPO R7',
                'app': '',
                'appPackage': 'com.tencent.mm',
                'appActivity': '.ui.LauncherUI',
                'unicodeKeyboard': True,
                'resetKeyboard': True,
                'noReset': True,
                'recreateChromeDriverSessions': True,
                'chromeOptions': {'androidProcess': 'com.tencent.mm:tools'}
                #'newCommandTimeout':'60'  #设置未接受到新命令的超时时间，默认60s，说明：如果60s内没有接收到新命令，appium会自动断开，
                }
            cls._instance = orig.__new__(cls, *args, **kw)
            cls._instance.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',config)
        return cls._instance


class DriverClient(Singleton):

    def getDriver(self):
        # Log.debug('获取driver')
        return self.driver