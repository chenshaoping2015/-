# -*- coding:utf-8 -*-
# @Time  :2021/1/14 13:31
# @Author: stevenchen
from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestWait:
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://testerhome.com/topics")
        self.driver.implicitly_wait(3)

    def teardown(self):
        pass

    def test_wait(self):
        WebDriverWait.until()
        expected_conditions.x
