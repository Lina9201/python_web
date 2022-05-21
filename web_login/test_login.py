#! /usr/bin/env/python3
# coding=utf-8
# @Time : 2022/4/24 22:03
# @Author : zhuxuefei
import pytest

from PythonWeb.pages import *
from selenium import webdriver


@pytest.fixture()
def driver():
    webdriver.Chrome("http://www172168000041.pinwheel.qycloud.com.cn:39000/home/login")


def test_login(driver):
    page = LoginPage(driver)
    page.login("apitest", "111111")


if __name__ == "__main__":
    test_login(driver)

