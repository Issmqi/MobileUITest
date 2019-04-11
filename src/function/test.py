import wechataction
import initappdriver
import time

appdriver=initappdriver.initappdriver()

class test():
    def __init__(self):
        self.driver=appdriver.setdriver()
    def Test(self):
        print(self.driver.find_element_by_id("com.tencent.mm:id/hk"))
def mian():
    a=test()
    a.Test()
if __name__=='__main__':
    mian()