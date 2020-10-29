#coding=utf-8
import pytest
from Base_paskage import screenshot_error
from Base_paskage import open_browser
import time
from selenium import webdriver

class login_all:
    def __init__(self):
        self.driver=open_browser.selenium_driver("chrome")
    def login_success(self):
        url = "https://www.baidu.com/"
        self.driver.get_url(url)
        self.driver.find_elemants("name","tj_login",1).click()

paramss={1:(1,2,3,4,5),2:{1:2},3:3}
@pytest.mark.parametrize('login_data',paramss)
class Test_login:
    def test_login(self,login_data):
        print(login_data)
        # pytest.assume(1)
        # pytest.assume(0)
        # pytest.assume(0)


if __name__ == '__main__':
    # url = "https://www.baidu.com/"
    # driver=open_browser.selenium_driver("chrome")
    # print(type(driver))
    # driver
    pytest.main(['-s','testcase2.py'])

    '''
    url = "https://www.baidu.com/"
    driver=webdriver.Chrome()
    driver.get(url)
    time.sleep(2)
    driver.find_elements_by_name("tj_login")[1].click()
    time.sleep(2)
    driver.find_element_by_id("TANGRAM__PSP_11__footerULoginBtn").click()
    time.sleep(2)
    driver.find_element_by_id("TANGRAM__PSP_11__userName").send_keys(1111)
    driver.find_element_by_id ("TANGRAM__PSP_11__password").send_keys("123123")
    driver.find_element_by_id("TANGRAM__PSP_11__submit").click()
    print (type(driver.find_element_by_id("TANGRAM__PSP_11__error")))
    print(type(driver.find_element_by_id("TANGRAM__PSP_11__error")))
    if driver.find_element_by_id("TANGRAM__PSP_11__error"):
        print("打印错误截图")
        driver.save_screenshot("C:/soft/pycharm/workspace/Appium_Mj/image_screen/login_error.png")
            #save_screenshort("C:/soft/pycharm1/workspace/Appium_Mj/image_screen")
    time.sleep(2)
    driver.close()
    '''

    '''
    browser_name = "chrome"
    driver =open_browser.selenium_driver(browser_name)
    driver.get_url(url)
    time.sleep(5)
    #driver.screenshort_error()
    driver.find_element_class_name()
    driver.find_elemant_name("tj_login").click()
    driver.find_element_id("TANGRAM__PSP_11__userName").send_keys(1111)
    driver.find_element_id ("TANGRAM__PSP_11__password").send_keys("123123")
    time.sleep(2)
    driver.close_driver()
'''
