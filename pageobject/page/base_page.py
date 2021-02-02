# -*- coding:utf-8 -*-
# @Time  :2021/2/1 17:47
# @Author: stevenchen

from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver


class BasePage:
    base_url = ""

    def __init__(self, driver: WebDriver = None):
        if driver is None:
            self.driver = webdriver.Chrome()
        else:
            self.driver = driver
        if self.base_url != "":
            self.driver.get(self.base_url)

    def find(self,by,locator):
        return self.driver.find_element(by,locator)