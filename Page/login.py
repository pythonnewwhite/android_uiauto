import time
import sys
import random
import uiautomator2 as u2
sys.path.append("C:\soft\Pycharm\workspace\APP_auto\Base_paskage")

class LoginPage:
    def __init__(self,caps):
        self.driver = u2.connect("1ec5b011")
        self.driver = u2.connect()
    def get_json_value(self,json_data,key):
        if isinstance(json_data,dict):
            for i in json_data.keys():
                if isinstance(json_data[i],dict):
                    return self.get_json_value(json_data[i],key)
                if i ==key:
                    return json_data[i]
    def oppapp(self):
        self.driver.app_start("com.tima.gac.passengercar")
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
        print(left,top)
        self.driver.swipe(left+100,top,left,top)
        self.driver.swipe(left+100,top,left,top)
        self.driver.swipe(left+100,top,left,top)
        time.sleep(2)

    def read(self):
        self.driver.app_start("com.cootek.literature")

    def swip_app(self,nub):
        for i in range(nub):
            print("开始第%d次" % i)
            driver.swipe(0.254, 0.766, 0.254, 0.272)
            j = random.randint(3, 6)
            print("等待时间=%d秒"%j)
            time.sleep(j)

if __name__ == '__main__':
    # login=LoginPage(caps)
    # login.oppapp()
    # login.chexing()
    # login.leida()
    # login.login_phone_password(15900842165,666888)
    # login.lougin_out()
    # login.close()

    driver = u2.connect("1ec5b011")
    driver.app_start("com.kuaishou.nebula")
    # driver.screenshot("C:\soft\Pycharm\workspace\APP_auto\image_screen\login_phone_error.png")
    time.sleep(5)
    start_time=time.time()
    for i in range(10000):
        print("开始第%d次"%i)
        driver.swipe(0.254, 0.766,0.254, 0.272)
        # driver.implicitly_wait()
        # #隐式等待
        i =random.randint(3,6)
        time.sleep(i)
        end_time=time.time()
        time_dif = end_time - start_time
        # print("宝箱开始时间间隔",time_dif,"s")
        # if int(time_dif * 10)>10 :
        #     driver(resourceId="com.kuaishou.nebula:id/left_btn").click()
        #     time.sleep(2)
        #     driver(text="去赚钱").click()
        #     time.sleep(3)
        #     if driver.exists(text="开宝箱得金币"):
        #         print(1)
        #         driver(text="开宝箱得金币").click()
        #         time.sleep(2)
        #         driver(text="看今日热门视频").click()
        #         time.sleep(2)
        #     else:
        #         driver(className="android.view.View").click()
        #     start_time = time.time()

    driver.app_stop("com.kuaishou.neb ula")