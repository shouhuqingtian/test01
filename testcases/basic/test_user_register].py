# -*- coding:utf-8 -*-
from time import sleep
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from util import untis


class TestUserRegister(object):
    def __init__(self):
        self.driver = webdriver.Firefox()
        self.driver.get('http://www.jpress.io/user/register')
        self.driver.maximize_window()

    # 测试登录验证码错误
    def test_register_code_error(self):
        username = 'test001'
        email = 'test001@qq.com'
        pwd = '123456'
        confirmPwd = '123456'
        captcha = '666'
        expected = '验证码不正确'

        self.driver.find_element_by_name('username').send_keys(username)
        self.driver.find_element_by_name('email').send_keys(email)

        self.driver.find_element_by_name('pwd').send_keys(pwd)
        self.driver.find_element_by_name('confirmPwd').send_keys(confirmPwd)

        self.driver.find_element_by_name('captcha').send_keys(captcha)
        self.driver.find_element_by_class_name('btn').click()

        WebDriverWait(self.driver, 5).until(EC.alert_is_present())
        alert = self.driver.switch_to.alert
        # python断言
        assert alert.text == expected
        alert.accept()

        sleep(3)

    def test_register_ok(self):
        username = util.gen_random_str()
        email = username + '@qq.com'
        pwd = '123456'
        confimPwd = '123456'
        expected = '注册成功，点击确定进行登录'

        # 输入用户名
        self.driver.find_element_by_name('username').send_keys(username)
        # email
        self.driver.find_element_by_name('email').send_keys(email)
        # 密码
        self.driver.find_element_by_name('pwd').send_keys(pwd)
        # 确认密码
        self.driver.find_element_by_name('confimPwd').send_keys(confimPwd)
        # 自动识别验证码
        captcha = util.get_code(self.driver)
        self.driver.find_element_by_name('captcha').send_keys(captcha)