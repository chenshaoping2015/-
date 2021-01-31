# -*- coding:utf-8 -*-
# @Time  :2021/1/31 10:50
# @Author: stevenchen
from time import sleep

from auto_testing_prace.selenium练习.selenium_frame_windows.base import Base
from selenium.webdriver.common.by import By


class TestFile(Base):
    def test_file(self):
        profileDir = r'D:\pics\20171116110253542.jpg'
        self.driver.get("https://www.baidu.com")
        self.driver.find_element(by=By.XPATH,value="//span[@class='soutu-btn']").click()
        self.driver.find_element(by=By.XPATH,value="//input[@type='file']").send_keys(profileDir)
        sleep(3)