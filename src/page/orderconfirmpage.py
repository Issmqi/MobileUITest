
class OrderConfirmPage:
    def __init__(self,driver):
        self.driver=driver

    def homepage_ele(self):
        '''主页入口'''

        element=self.driver.find_element_by_xpath('//*[@id="wmContainer"]/div[1]/div[1]/div[1]/div[1]/a')
        return element

    def personal_ele(self):
        '''个人中心入口'''
        element = self.driver.find_element_by_xpath('//*[@id="wmContainer"]/div[1]/div[1]/div[1]/ul/li[1]/a')
        return element

    def shoppingCart_ele(self):
        '''购物车入口'''
        element = self.driver.find_element_by_xpath('//*[@id="wmContainer"]/div[1]/div[1]/div[1]/ul/li[2]/a')
        return element