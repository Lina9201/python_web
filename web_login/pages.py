#! /usr/bin/env/python3
# coding=utf-8
# @Time : 2022/4/10 19:54
# @Author : zhuxuefei
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.expected_conditions import *


class BasePage:
    def __init__(self, driver):
        self._driver = driver
        self._wait = WebDriverWait(driver, 10)

    def __getattr__(self, item):
        key = f'_loc_' + item
        xpath = getattr(self, key, None)
        if xpath:
            return self.get_element(xpath)
        raise AttributeError("元素不存在")

    def get_element(self, xpath):
        """
        元素定位自动等待到元素出现
        :param xpath:
        :return:
        """
        el = self._wait.until(
            visibility_of_element_located(
                (
                    By.XPATH,
                    xpath,
                )
            )
        )

        return el


class LoginPage(BasePage):
    _loc_username = '//input[@placeholder="登录id/手机号码/邮箱"]'
    _loc_password = '//input[@placeholder="密码"]'
    _loc_btn = '//span[text()= "登 录"]'

    def login(self, username, password):
        self.username.send_keys(username)
        self.password.send_keys(password)
        self.btn.click()


