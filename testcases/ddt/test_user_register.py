# -*- coding:utf-8 -*-
import time
from time import sleep
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from util import utils
import pytest
from testcases.ddt.test_excel import get_excel_data


class TestUserRegister:
    # @classmethod
    def setup_class(self):
        self.driver = webdriver.Firefox()
        self.driver.get('http://159.75.96.188:18080/jpress/user/register')
        self.driver.maximize_window()
        time.sleep(1)

    # login_data = [
    #     ('test01', 'test01@qq.com', '123456', '123456', '666', '验证码不正确'),
    #     ('test07', 'test06@qq.com', '123456', '123456', '111', '注册成功，点击确定进行登录')
    # ]

    # 测试登录验证码错误
    @pytest.mark.parametrize('username, email, pwd, confirmPwd, captcha, expected', get_excel_data())
    # @pytest.mark.parametrize('username, email, pwd, confirmPwd, captcha, expected', get_excel_data())
    def test_register_code_error(self, username, email, pwd, confirmPwd, captcha, expected):
        # username = 'test001'
        # email = 'test001@qq.com'
        # pwd = '123456'
        # confirmPwd = '123456'
        # captcha = '666'
        # expected = '验证码不正确'

        self.driver.find_element_by_name('username').send_keys(username)
        self.driver.find_element_by_name('email').send_keys(email)

        self.driver.find_element_by_name('pwd').send_keys(pwd)
        self.driver.find_element_by_name('confirmPwd').send_keys(confirmPwd)

        self.driver.find_element_by_name('captcha').send_keys(captcha)
        self.driver.find_element_by_class_name('btn-primary').click()

        WebDriverWait(self.driver, 5).until(EC.alert_is_present())
        alert = self.driver.switch_to.alert
        # python断言
        assert alert.text == expected
        # self.assertEqual(alert.text, expected, '登录验证码断言失败')
        alert.accept()
        sleep(10)

    def test_register_ok(self):
        username = utils.gen_random_str()
        email = username + '@qq.com'
        pwd = '123456'
        confirmPwd = '123456'
        expected = '注册成功，点击确定进行登录。'

        # 输入用户名
        self.driver.find_element_by_name('username').clear()
        self.driver.find_element_by_name('username').send_keys(username)
        # email
        self.driver.find_element_by_name('email').clear()
        self.driver.find_element_by_name('email').send_keys(email)
        # 密码
        self.driver.find_element_by_name('pwd').clear()
        self.driver.find_element_by_name('pwd').send_keys(pwd)
        # 确认密码
        self.driver.find_element_by_name('confirmPwd').clear()
        self.driver.find_element_by_name('confirmPwd').send_keys(confirmPwd)
        # 自动识别验证码
        self.driver.find_element_by_name('captcha').clear()
        captcha = utils.get_code(self.driver, 'captchaimg')
        self.driver.find_element_by_name('captcha').send_keys(captcha)
        self.driver.find_element_by_class_name('btn-primary').click()
        # 等待alert出现
        WebDriverWait(self.driver, 5).until(EC.alert_is_present())
        alert = self.driver.switch_to.alert
        # 验证
        assert alert.text == expected
        # self.assertEqual(alert.text, expected, '登录断言失败')
        alert.accept()


if __name__ == '__main__':
    pytest.main(['test_user_register.py'])
