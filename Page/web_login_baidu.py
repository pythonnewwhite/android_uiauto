import sys
import os
import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

yamldata=""
@pytest.mark.parametrize("ele",yamldata)
class BaiduLogin:

    def login(self,ele):
        #打开网页
        wd=webdriver.Chrome()
        wd.find_element_by_name("tj_login").click()



if __name__ == '__main__':
    wd = webdriver.Chrome()
    ss=time.time()
    wd.get("https://www.baidu.com/")
    # wd.find_element_by_id("kw").click()
    # wd.find_element_by_id("kw").send_keys("selenium")
    # wd.find_element_by_id("su").click()
    wd.find_elements_by_name('tj_login')[1].click()
    # move =wd.find_element_by_id()
    # ActionChains(wd).move_to_element(move).perform()
    # wd.find_element_by_class_name("bg s_btn btnhover").click()
    time.sleep(3)
    wd.close()