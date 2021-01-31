# -*- coding:utf-8 -*-
# @Time  :2021/1/30 21:19
# @Author: stevenchen
from selenium import webdriver


class Base:
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(2)


    def teardown(self):
        self.driver.quit()