# -*- coding:utf-8 -*-
# @Time  :2021/1/30 21:52
# @Author: stevenchen
from time import sleep

from selenium练习.selenium_frame_windows.base import Base
from selenium.webdriver.common.by import By


class TestFrame(Base):
    def test_frame(self):
        self.driver.get("https://www.douban.com/")
        self.driver.switch_to.frame(0)
        self.driver.find_element(by=By.XPATH,value="//input[@type='phone']").send_keys("111")
        sleep(2)
        self.driver.find_element(by=By.XPATH,value="//input[@id='code']").send_keys("222")
        sleep(2)
        #self.driver.switch_to.default_content()
        self.driver.switch_to.parent_frame()
        self.driver.find_element(by=By.LINK_TEXT,value="豆瓣读书").click()
        sleep(2)