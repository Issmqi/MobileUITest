import initappdriver
import elementoperate

# appdriver=initappdriver.InitAppdriver()
# driver=appdriver.setdriver()

class BasePage:
    def __init__(self,driver):
        self.driver = driver
        self.EO=elementoperate.ElementOperate(driver)

    def homepage_ele(self):
        '''主页入口'''

        # element = self.EO.find_element(('xpath', '//*[@id="wmContainer"]/ul/li[1]/div/div[1]/div[1]/div[1]/a'))
        element = self.EO.find_element(('xpath', '//*[@id="wmContainer"]/div[1]/div[1]/div[1]/div[1]/a'))

        # element = self.driver.find_element_by_xpath('//*[@id="wmContainer"]/div[1]/div/div[1]/div[1]/div[1]/a')
        return element

    def personal_ele(self):
        '''个人中心入口'''
        element=self.EO.find_element(('xpath','//*[@id="wmContainer"]/div[1]/div/div[1]/div[1]/ul/li[1]/a'))
        # element = self.driver.find_element_by_xpath('//*[@id="wmContainer"]/div[1]/div/div[1]/div[1]/ul/li[1]/a')
        return element

    def shoppingCart_ele(self):
        '''购物车入口'''
        element=self.EO.find_element(('xpath','//*[@id="wmContainer"]/div[1]/div/div[1]/div[1]/ul/li[2]/a'))
        # element = self.driver.find_element_by_xpath('//*[@id="wmContainer"]/div[1]/div/div[1]/div[1]/ul/li[2]/a')
        return element

    def enterHomePage(self):
        self.homepage_ele().click()

    def enterPersonalCenter(self):
        self.personal_ele().click()

    def enterShoppingCart(self):
        self.shoppingCart_ele().click()
