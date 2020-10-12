import time
import sys
import uiautomator2 as u2
sys.path.append("C:\soft\Pycharm\workspace\APP_auto\Base_paskage")
# print(sys.path)
# from Base_paskage.Handle_Json import Handle_Json

caps={'deviceName': 'micc9', 'platformVersion': '10.0.0', 'automationName': 'UiAutomator2', 'platformName': 'Android', 'autoAcceptAlerts': 'true', 'appPackage': 'com.tima.gac.passengercar', 'appActivity': 'com.tima.gac.passengercar.ui.splash.SplashActivity', 'noReset': 'true'}
class LoginPage:

    def __init__(self,caps):
        # self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        # self.driver = u2.connect("1ec5b011")
        # self.driver = u2.connect("127.0.0.1")
        self.driver = u2.connect()
        # self.HJ=Handle_Json()
    def get_json_value(self,json_data,key):
        if isinstance(json_data,dict):
            for i in json_data.keys():
                if isinstance(json_data[i],dict):
                    return self.get_json_value(json_data[i],key)
                if i ==key:
                    return json_data[i]
    def oppapp(self):
        self.driver.app_start("com.tima.gac.passengercar")
        # self.driver(resourceId="com.tima.gac.passengercar:id/close").click()
    def login_phone_password(self,phone,yanzhengma):
        self.driver(resourceId="com.tima.gac.passengercar:id/close").click()
        time.sleep(2)
        self.driver(resourceId="com.tima.gac.passengercar:id/iv_left_icon").click()
        time.sleep(2)
        self.driver(resourceId="com.tima.gac.passengercar:id/tv_unlogin").click()
        self.driver(resourceId="com.tima.gac.passengercar:id/indicator_container").click()
        self.driver(resourceId="com.tima.gac.passengercar:id/account_telphone").send_keys(phone)
        self.driver(resourceId="com.tima.gac.passengercar:id/et_login_code").send_keys(yanzhengma)
        time.sleep(1)
        self.driver(resourceId="com.tima.gac.passengercar:id/btn_login_submit").click()
        self.driver.screenshot("C:\soft\Pycharm\workspace\APP_auto\image_screen\login_phone_error.png")
        time.sleep(2)
        self.driver.screenshot("C:\soft\Pycharm\workspace\APP_auto\image_screen\login_phone_error.png")
    def lougin_out(self):
        self.driver(resourceId="com.tima.gac.passengercar:id/rb_about2").click()
        self.driver(resourceId="com.tima.gac.passengercar:id/btn_login_out").click()
        # self.driver.find_element_by_name("确定").click()
        self.driver(text="确定").click()
        time.sleep(1)
        self.driver(text="确定").click()
    def close(self):
        self.driver.app_stop("com.tima.gac.passengercar")
    def leida(self):
        self.driver(resourceId="com.tima.gac.passengercar:id/close").click()
        self.driver(resourceId="com.tima.gac.passengercar:id/iv_radar").click()
        self.driver(resourceId="com.tima.gac.passengercar:id/tv_radar_time").click()
        self.driver(resourceId="com.tima.gac.passengercar: id/options2")
        self.driver(resourceId="com.tima.gac.passengercar: id/options3")
        time.sleep(3)
    def chexing(self):
        self.driver(resourceId="com.tima.gac.passengercar:id/lly_city_name").click()
        self.driver(resourceId="com.tima.gac.passengercar:id/city_name").click()
        self.driver(resourceId="com.tima.gac.passengercar:id/iv_choice").click()
        self.driver(resourceId="com.tima.gac.passengercar:id/cb_item_car_type").click()
        data=self.driver(resourceId="com.tima.gac.passengercar:id/cb_item_car_type").info
        print(data)
        left=self.get_json_value(data,"left")
        top=self.get_json_value(data,"top")
        # time.sleep(2)
        print(left,top)
        self.driver.swipe(left+100,top,left,top)
        self.driver.swipe(left+100,top,left,top)
        self.driver.swipe(left+100,top,left,top)
        # self.driver.swipe(0.794, 0.766,0.254, 0.772)
        time.sleep(2)
        # self.driver.swipe(286, 1960, 902, 1960)
        # self.driver.swipe(902,1960,286,1960)

        # time.sleep(2)
        # self.driver.swipe_ext("right",0.5)
        # self.driver.swipe_ext("left",0.5)

if __name__ == '__main__':
    login=LoginPage(caps)
    login.oppapp()
    # login.chexing()
    # login.leida()
    login.login_phone_password(15900842165,666888)
    # login.lougin_out()
    login.close()

    # driver = u2.connect("127.0.0.1")
    # driver.screenshot("C:\soft\Pycharm\workspace\APP_auto\image_screen\login_phone_error.png")
    # time.sleep(2)
