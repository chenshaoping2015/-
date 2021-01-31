# -*- coding:utf-8 -*-
# @Time  :2021/1/13 22:26
# @Author: stevenchen
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By


class TestTesterHome:
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    def test_testerhome(self):
        self.driver.get("https://testerhome.com/")
        self.driver.find_element(by=By.LINK_TEXT, value="社团").click()
        self.driver.find_element(by=By.LINK_TEXT,value="求职面试圈").click()
        sleep(5)
        # self.driver.find_element(by=By.LINK_TEXT,value="给你一张 (含满分答案的) 数据库面试题试卷").click()