import os
import sys
sys.path.append('C:\\soft\\Pycharm\\workspace\\new_mojie\\venv\\lib\\site-packages')
import pytest
import uiautomator2
import allure
from Page.login import LoginPage

from Page import mojie_login
#1、打开APP 实现账号密码登录、验证码登录
#2、错误账号登录，错误密码登录，截图
#3、每条用例执行后截图；

from  Base_paskage.handle_yaml import HandleYaml
yaml_data=HandleYaml().read_yaml()
paramss=yaml_data["loginpage"][0]["params"]

# @pytest.mark.parametrize("d1",paramss)
@allure.feature("摩捷出行-登录")
class Test_MJapp:
    # mj=mojie_login.MobJie_login()
    def setup(self):
        print("方法级别预制条件")
        # self.mj.close_app()
    def teardown(self):
        print("方法级别后置条件")
        # self.mj.close_app()
    def test01(self):
        a=1+1
        pytest.assume(1)

    # @allure.story("密码登录")
    # def test_MojieLogin1(self,d1):
    #     print("密码登录")
    #     print(d1)
        # self.mj.test_codelogin(d1["phone"],d1["pw"],d1["name"])
        # self.mj.login_for_pw(d1["phone"],d1["pw"],d1["name"])
    # @allure.story("验证码登录")
    # def test_MojieLogin2(self):
    #     print('验证吗登录')
    #     self.mj.test_passwordlogin(15900842165,666888)
    # @allure.story("退出登录")
    # def test_MojieLogin3(self):
    #     print('测试注册模块')
    #     self.mj.lougin_out()
    # def test(self,d1):
    #     print(d1["name"])
    #     print(type(d1))


if __name__ == '__main__':
    pytest.main(['-s','test_pytest.py','--alluredir=./Report/xml'])
    os.system('allure generate ./Report/xml/ -o ./Report/all/ --clean')
    # print(os.getcwd())
    # pytest.main(["-s"])