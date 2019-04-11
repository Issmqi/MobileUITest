'''
__author__:'shimengqi'
__description__:'初始化driver'
__mtime_:2018/7/16
'''
from appium import webdriver
import threading
import adbconnect
import log



Log = log.Log()


class InitAppdriver():
    _instance_lock = threading.Lock()

    def __new__(cls, *args, **kwargs):
        if not hasattr(InitAppdriver, "_instance"):
            with InitAppdriver._instance_lock:
                if not hasattr(InitAppdriver, "_instance"):
                    InitAppdriver._instance = object.__new__(cls)
        return InitAppdriver._instance

    def setdriver(self):
        # 配置需读取的机型
        # model="honorADB"
        model = "oppoADB"
        ADB=adbconnect.adbconnect(model)

        # desired_caps=ADB.getAdb()
        desired_caps = ADB.adb()
        driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        driver.implicitly_wait(40)
        Log.debug("%s driver初始化完成"%model)
        return driver


def main():
    appdriver = InitAppdriver()
    appdriver.setdriver()


if __name__ == '__main__':
    main()
