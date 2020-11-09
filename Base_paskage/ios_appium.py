from appium import webdriver

def setUp(self):
    desired_caps = {}
    desired_caps['platformName'] = 'ios'  # 设备系统
    desired_caps['platformVersion'] = '14.0'  # 设备系统版本
    desired_caps['deviceName'] = 'iphone XR'  # 设备名称
    desired_caps['bundleId'] = ''  # 测试app包名
    desired_caps['udid'] = '00008020-0001214E1E92002E'
    desired_caps['automationName'] = ''  # 测试appActivity
    self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
