'''
__author__:'shimengqi'
__description__:'重写元素操作基本方法'
__mtime_:2018/8/3
'''
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class ElementOperate():
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, locator):

        '''
        定位元素，参数locator为元祖类型
        locator = ('id','xxx')
        driver.find_element(locator)

        '''
        try:
            element = WebDriverWait(
                self.driver, 20
            ).until(EC.presence_of_element_located(locator))
            # logger.info('Positioning to the %s%s element.' % locator)
            return element
        except:
            print(u"页面中未能找到 %s 元素" % locator)


