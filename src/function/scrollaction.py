'''
__author__:'shimengqi'
__description__:'滚动条操作'
__mtime_:2018/7/27
'''

class ScrollAction():
    def __init__(self,driver):
        self.driver=driver

    def scroll_topping(self):
        '''
        滑动到页面最底部
        :return:
        '''
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    def scrollup_by_element(self,element):
        '''
        移动到元素element对象的“顶端”与当前窗口的“顶部”对齐
        :param element:
        :return:
        '''
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        # 滚动条向下滚动滑动导航栏的高度
        self.driver.execute_script("window.scrollBy(0, -50)")
        # self.driver.execute_script("arguments[0].scrollIntoView(true);", element)#备选
    def scrolldown_by_element(self,element):
        '''
        移动到元素element对象的“底部”与当前窗口的“底部”对齐
        :param element:
        :return:
        '''
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

    def scroll_until_view(self,element):
        '''
        循环操作滚动条直到元素可点击
        :param element:
        :return:
        '''
        height = 1920
        width = 1080

        # while循环10次
        i = 1
        while i < 10:
            try:
                element.click()  # 尝试点击元素
                print("元素点击成功")
                # self.driver.find_element_by_xpath(path)
                break
            except Exception as e:
                print("这是第", i, "次尝试！")
                self.driver.execute_script("window.scrollBy(0, 20)")
                i = i + 1

    def scroll_by(self,y):
        '''
        相对当前位置滚动条向上滚动，即页面向下滚动，可传负数
        :return:
        '''
        js="window.scrollBy(0, "+str(y)+")"
        self.driver.execute_script(js)
        # self.driver.execute_script("window.scrollBy(0, 50)")


    def scroll_to(self):
        '''
        滚动条移动到绝对位置坐标
        :return:
        '''
        self.driver.execute_script("window.scrollTo(0, 1200)")




