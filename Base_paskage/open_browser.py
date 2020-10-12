#coding=utf-8
from selenium import webdriver
import configparser
#from util.read.idriverni import ReadIni

class selenium_driver(object):
    def __init__(self,browser_namme):
        self.driver=self.open_browsers(browser_namme)
    #根据传入的value的值来打开用户期望的浏览器
    def open_browsers(self,browser_namme):
        if browser_namme=="chrome":
            self.driver=webdriver.Chrome()
        elif browser_namme=="firefox":
            self.driver=webdriver.firefox()
        else:
            self.drver=webdriver.ie()
        return self.driver
    #根据输入的url地址打开网页
    def get_url(self,url):
        self.driver.get(url)

    #根据传入值value与错误值code_error对比判断是否要截图
    def screenshor(self,value,code_error):
        if value ==None:
            pass
        elif value==code_error:
            self.driver.save_screenshort("C:/soft/pycharm1/workspace/Appium_Mj/image_screen")
        else:
            self.driver
    def find_element_id(self,id):
        self.driver.find_element_by_class_id(id)

    def find_elemant(self,by,value):
        if by=="id":
            self.driver.find_element_by_id(value)
        elif by=="name":
            self.driver.find_element_by_name(value)
        elif by =="class_name":
            self.driver.find_element_by_class_name(value)
        elif by==None:
            return None


    def find_elemants(self,by,value,nub):
        if by=="id":
            return self.driver.find_elements_by_id(value)[nub]
        elif by=="name":
            return self.driver.find_elements_by_name(value)[nub]
        elif by =="class_name":
            return self.driver.find_elements_by_class_name(value)[nub]
        elif by==None:
            return None
    #读取配置文件
    def get_element(self):
        read_ini=configparser.ConfigParser()
        read_ini.read("LocalElement.ini")
        print (read_ini.sections())
        print (read_ini.options("test1"))
    #关闭浏览器二次封装
    def close_driver(self):
        self.driver.close()


if __name__ == '__main__':
    driver=selenium_driver("chrome")
    driver.get_url("https://www.baidu.com/")
    driver.find_elemants("name", "tj_login",1).click()

    '''
    browser_namme="chrome"
    driver=selenium_driver("chrome")
    driver.get_url("https://www.baidu.com/")
    driver.find_elemant_name("tj_login").click()

'''




