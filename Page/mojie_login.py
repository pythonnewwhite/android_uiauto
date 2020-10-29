import time
import sys
import pytest
import allure
import uiautomator2 as u2
import logging
from  Base_paskage.handle_yaml import HandleYaml
# sys.path.append("C:\soft\Pycharm\workspace\APP_auto\Base_paskage")
yaml_data=HandleYaml().read_yaml()
yaml_data1 = yaml_data["loginpage"][0]["case"]
yaml_data2 = yaml_data["loginpage"][0]["params"]
@pytest.mark.parametrize('element',yaml_data1)
class MobJie_login:
    def __init__(self,sn=None):
        if sn==None:
            self.driver=u2.connect("1ec5b011")
        else:
            self.driver=u2.connect(sn)


    def close_app(self):
        self.driver.app_stop("com.tima.gac.passengercar")

    def open_app(self):
        try:
            self.driver.app_stop("com.tima.gac.passengercar")
        except:
            print("APP打开失败")

    def click_app(self,app_resourceId,nub):
        """app_resourceId参数：定位的元素id，nub:查询元素次数,每次查询0.5秒"""
        for i in range(nub):
            time.sleep(0.5)

            s=(i+1)*0.5
            if self.driver.exists(resourceId=app_resourceId):
                self.driver(resourceId=app_resourceId).click()
                print("查找元素%s等待时间："%app_resourceId,s)
                return
        print(app_resourceId,"元素未找到")
    def to_login_page(self,title):
        allure.dynamic.title(title)
        print("开始执行摩捷出行登录")
        with allure.step("打开APP"+yaml_data1[0]["value"]):
            self.driver.app_start(yaml_data1[0]["value"])
        with allure.step("关闭广告页"):
            self.click_app(yaml_data1[1]["value"], 4)
        self.click_app(yaml_data1[2]["value"], 4)
        print("进入个人中心")
        self.click_app(yaml_data1[3]["value"], 4)
        print("进入登录页面")
    def login_for_pw(self,phone,pw,title):
        self.to_login_page(title)
        self.driver(resourceId=yaml_data1[4]["value"]).send_keys(phone)
        self.driver(resourceId=yaml_data1[5]["value"]).send_keys(pw)
        self.driver.screenshot("C:\soft\Pycharm\workspace\APP_auto\image_screen\login1.jpg")
        self.driver(resourceId=yaml_data1[6]["value"]).click()
        allure.attach("./image_screen/login1.jpg","密码登录异常截图",attachment_type=allure.attachment_type.JPG)
        print("点击登录按钮")
        self.driver.screenshot("C:\soft\Pycharm\workspace\APP_auto\image_screen\login2.jpg")
        with open(self.driver.screenshot("C:\soft\Pycharm\workspace\APP_auto\image_screen\login2.jpg"),'rb') as file:
            filebayes = file.read()
        with allure.step('登录截图'):
            allure.attach(filebayes,"密码登录异常截图",attachment_type=allure.attachment_type.JPG)
            print("登录页面截屏")
        self.driver.app_stop("com.tima.gac.passengercar")

    def test_codelogin(self,phone,yanzhengma,title):
        """需要传递phone,：用户手机号，yanzhengma：用户验证码"""
        allure.dynamic.title(title)
        print("开始执行摩捷出行登录")
        with allure.step("打开APP"):
            print('打开APP')
            self.driver.app_start("com.tima.gac.passengercar")
        with allure.step("关闭广告页"):
            print('关闭广告页')
            self.click_app("com.tima.gac.passengercar:id/close", 4)
        self.click_app("com.tima.gac.passengercar:id/iv_left_icon",4)
        print("进入个人中心")
        self.click_app("com.tima.gac.passengercar:id/tv_unlogin",4)
        print("进入登录页面")
        self.driver(resourceId="com.tima.gac.passengercar:id/account_telphone").send_keys(phone)
        self.driver(resourceId="com.tima.gac.passengercar:id/et_login_code").send_keys(yanzhengma)
        self.driver.screenshot("C:\soft\Pycharm\workspace\APP_auto\image_screen\login1.jpg")
        self.driver(resourceId="com.tima.gac.passengercar:id/btn_login_submit").click()
        allure.attach("./image_screen/login1.jpg","密码登录异常截图",attachment_type=allure.attachment_type.JPG)
        print("点击登录按钮")
        self.driver.screenshot("C:\soft\Pycharm\workspace\APP_auto\image_screen\login2.jpg")
        with open(self.driver.screenshot("C:\soft\Pycharm\workspace\APP_auto\image_screen\login2.jpg"),'rb') as file:
            filebayes = file.read()
        allure.attach(filebayes,"密码登录异常截图",attachment_type=allure.attachment_type.JPG)
        print("登录页面截屏")
        self.driver.app_stop("com.tima.gac.passengercar")

    def test_passwordlogin(self,phone,password):
        allure.dynamic.title("验证码登录")
        """需要传递phone,：用户手机号，password：用户密码"""
        with allure.step("打开APP"):
            print("打开APP")
            self.driver.app_start("com.tima.gac.passengercar")
        with allure.step("关闭广告页"):
            self.click_app("com.tima.gac.passengercar:id/close", 4)
        self.click_app("com.tima.gac.passengercar:id/iv_left_icon", 4)
        print("进入个人中心")
        self.click_app("com.tima.gac.passengercar:id/tv_unlogin", 4)
        print("进入登录页面")
        self.click_app("com.tima.gac.passengercar:id/indicator_container",4)
        print("切换到验证码登录")
        self.driver(resourceId="com.tima.gac.passengercar:id/account_telphone").send_keys(phone)
        self.driver(resourceId="com.tima.gac.passengercar:id/et_login_code").send_keys(password)
        self.driver(resourceId="com.tima.gac.passengercar:id/btn_login_submit").click()
        print("点击登录按钮")
        time.sleep(2)
        with allure.step("点击登录"):
            with open(self.driver.screenshot("C:\soft\Pycharm\workspace\APP_auto\image_screen\login_phone_error.jpg"),
                      'rb') as file:
                filebayes = file.read()
            allure.attach(filebayes,"验证码登录截图","login_phone_error.jpg")
        print("登录页面截屏")
        self.driver.app_stop("com.tima.gac.passengercar")
    def lougin_out(self):
        allure.dynamic.title("退出登录")
        with allure.step("打开APP"):
            self.driver.app_start("com.tima.gac.passengercar")
        with allure.step("关闭广告页"):
            self.click_app("com.tima.gac.passengercar:id/close", 4)
        print("关闭广告页")
        self.click_app("com.tima.gac.passengercar:id/iv_left_icon", 4)
        print("进入个人中心")
        self.click_app("com.tima.gac.passengercar:id/rb_about2",6)
        self.click_app("com.tima.gac.passengercar:id/btn_login_out",4)
        try:
            self.driver(text="确定").click()
            time.sleep(1)
            self.driver(text="确定").click()
        except:
            print("元素未找到，跳过此条case")
        # self.driver.screenshot("C:\soft\Pycharm\workspace\APP_auto\image_screen\login_out.jpg")
        with open(self.driver.screenshot("C:\soft\Pycharm\workspace\APP_auto\image_screen\login_out.jpg"), 'rb') as file:
            filebayes = file.read()
        allure.attach(filebayes,name="退出登录截图",attachment_type=allure.attachment_type.JPG)
        print("退出登录页面截屏")
        self.driver.app_stop("com.tima.gac.passengercar")
if __name__ == '__main__':
    # sn="127.0.0.1"
    # mj=MobJie_login()
    # mj.close_app()
    # mj.close_app()
    # mj.to_login_page()
    # mj.login_for_pw(1,2,'登录调试')
    # mj.test_codelogin(1,2)
    # mj.test_passwordlogin(15900842165,666888)
    # mj.lougin_out()
    # driver = u2.connect("1ec5b011")
    # driver.app_start("com.tima.gac.passengercar")
    # time.sleep(3)
    # driver.screenshot("C:\soft\Pycharm\workspace\APP_auto\image_screen\login_phone_error.jpg")
    # yaml_data=HandleYaml().read_yaml()
    # yaml_data1=yaml_data["loginpage"][0]["case"]
    # yaml_data2=yaml_data["loginpage"][0]["params"]
    # print(yaml_data1)
    # print(yaml_data2)
    start_time=time.time()
    time.sleep(2)
    end_time = time.time()
    time_dif = end_time - start_time
    print(int(time_dif)*10)