# -*- coding:utf-8 -*-
# @Time  :2021/1/25 19:44
# @Author: stevenchen
from selenium import webdriver
from selenium.webdriver import TouchActions
from selenium.webdriver.common.by import By
import time


class Test_TouchAction:
    def setup(self):
        option = webdriver.ChromeOptions()
        option.add_experimental_option('w3c', False)
        self.driver = webdriver.Chrome(options=option)
        self.driver.maximize_window()
        self.driver.implicitly_wait(2)

    def teardown(self):
        self.driver.quit()

    def test_case_click(self):
        self.driver.get("http://www.baidu.com")
        element_click = self.driver.find_element(by=By.ID,value="kw")
        element_search = self.driver.find_element(by=By.ID ,value="su")

        element_click.send_keys("selenium测试")
        action = TouchActions(self.driver)
        action.tap(element_click)
        action.perform()

        action.scroll(0,10000).perform()
        time.sleep(2)