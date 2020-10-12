from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
import time
from selenium.webdriver.common.by import By

caps = {}
caps["deviceName"] = "micc9"
caps["platformVersion"] = "10.0.0"
caps["automationName"] = "Appium"
caps["platformName"] = "Android"
caps["autoAcceptAlerts"] = "true"
caps["appPackage"] = "com.tima.fawffs.test"
caps["appActivity"] = "com.tima.launch.app.mvp.ui.activity.SplashActivity"
caps["noReset"] = "true"
caps["automationName"]="UiAutomator1"
##登录页定位坐标  手机号》id》com.tima.fawffs.test:id/username_login_et
##登录页定位坐标  密码》id》com.tima.fawffs.test:id/password_login_et
driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
def login(tel,passw):
    time.sleep(3)
##输入手机号
    driver.find_element_by_id("com.tima.fawffs.test:id/username_login_et").send_keys(tel)
##输入密码
    driver.find_element_by_id("com.tima.fawffs.test:id/password_login_et").send_keys(passw)
##点击返回按钮
    driver.back()
##登录
    time.sleep(5)
    driver.find_element_by_id("com.tima.fawffs.test:id/login_btn").click()
    time.sleep(2)
    driver.find_element_by_id("com.tima.fawffs.test:id/action_user").click()
    time.sleep(3)


def loginout():
    time.sleep(4)
##个人中心定位坐标   个人中心 >id >	com.tima.fawffs.test:id/icon
    driver.find_element_by_id("com.tima.fawffs.test:id/action_user").click()
    time.sleep(2)
##设置按钮定位坐标   设置 >id >com.tima.fawffs.test:id/tv_setting_name
    driver.find_element_by_class_name("android.widget.ImageView").click()
    time.sleep(2)
##退出登录定位坐标 退出登录  >id >	com.tima.fawffs.test:id/tv_login_out
    driver.find_element_by_id("com.tima.fawffs.test:id/tv_login_out").click()
    time.sleep(2)
###确定退出按钮  确定  >class > 	android.widget.TextView
    driver.find_element_by_class_name("android.widget.TextView")


##  com.tima.fawffs.test: id / icon

if __name__ == '__main__':
    login("15900842165","123ABCabc")
    ##loginout()
    driver.quit()