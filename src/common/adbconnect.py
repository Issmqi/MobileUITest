'''
__author__:'shimengqi'
__description__:'adb连接信息'
__mtime_:2018/7/16
'''
import confparser

ReadConfig = confparser.ReadConfig()


class adbconnect():
    def __init__(self,model):
        self.model=model
        # self.model=ReadConfig.get_config("Model","model")
        self.platformName=ReadConfig.get_config(self.model,"platformName")
        self.platformVersion = ReadConfig.get_config(self.model, "platformVersion")
        self.deviceName = ReadConfig.get_config(self.model, "deviceName")
        self.app = ReadConfig.get_config(self.model, "app")
        self.appPackage = ReadConfig.get_config(self.model, "appPackage")
        self.appActivity = ReadConfig.get_config(self.model, "appActivity")
        self.unicodeKeyboard = ReadConfig.get_config(self.model, "unicodeKeyboard")
        self.resetKeyboard = ReadConfig.get_config(self.model, "resetKeyboard")
        self.noReset = ReadConfig.get_config(self.model, "noReset")
        self.recreateChromeDriverSessions = ReadConfig.get_config(self.model, "recreateChromeDriverSessions")
        self.newCommandTimeout=ReadConfig.get_config(self.model,"newCommandTimeout")
        self.chromeOptions = ReadConfig.get_config(self.model, "chromeOptions")



    def getAdb(self):
        desired_caps = {
            'platformName': self.platformName,
            'platformVersion': self.platformVersion,
            'deviceName':self.deviceName,
            'app': self.app,
            'appPackage': self.appPackage,
            'appActivity': self.appActivity,
            'unicodeKeyboard': self.unicodeKeyboard,
            'resetKeyboard': self.resetKeyboard,
            'noReset': self.noReset,
            'recreateChromeDriverSessions': self.recreateChromeDriverSessions,
            'chromeOptions': self.chromeOptions
        }
        return desired_caps


    def adb(self):
        desired_caps = {
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
        }
        return desired_caps
