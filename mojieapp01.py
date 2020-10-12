# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python

from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
import time
from selenium.webdriver.common.by import By

caps={'deviceName': 'micc9', 'platformVersion': '10.0.0', 'automationName': 'UiAutomator1', 'platformName': 'Android', 'autoAcceptAlerts': 'true', 'appPackage': 'com.tima.gac.passengercar', 'appActivity': 'com.tima.gac.passengercar.ui.splash.SplashActivity', 'noReset': 'true'}

driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
time.sleep(3)
driver.find_element_by_id("com.tima.gac.passengercar:id/close").click()
driver.find_element_by_id("com.tima.gac.passengercar:id/iv_left_icon").click()
time.sleep(3)
driver.find_element_by_id("com.tima.gac.passengercar:id/tv_unlogin").click()
time.sleep(2)
## driver.find_element_by_class_name("android.widget.TextView").click()
##driver.find_element_by_name("无密码快捷登录").click()
driver.find_element_by_id("com.tima.gac.passengercar:id/indicator_container").click()
driver.find_element_by_id("com.tima.gac.passengercar:id/account_telphone").send_keys("15900842165")
driver.find_element_by_id("com.tima.gac.passengercar:id/et_login_code").send_keys("666888")
driver.find_element_by_id("com.tima.gac.passengercar:id/btn_login_submit").click()
time.sleep(3)
driver.quit()