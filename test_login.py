import pytest
import sys
import uiautomator2
from Page.login import LoginPage

class Test_MJapp:
    def setup(self):
        print("方法级别预制条件")
        pass
    def teardown(self):
        print("方法级别后置条件")

    def login_phone_error(self,phone,password):
        LoginPage().login_phone_password()
