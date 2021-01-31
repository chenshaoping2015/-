# -*- coding:utf-8 -*-
# @Time  :2021/1/30 21:17
# @Author: stevenchen
from time import sleep

from selenium练习.selenium_frame_windows.base import Base
from selenium.webdriver.common.by import By


class TestWindows(Base):
    def test_windows(self):
        self.driver.get("https://www.baidu.com")
        print(self.driver.current_window_handle)
        self.driver.find_element(by=By.LINK_TEXT,value="学术").click()
        sleep(3)
        print(self.driver.current_window_handle)
        print(self.driver.window_handles)

        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[-1])
        print(self.driver.current_window_handle)

        self.driver.find_element(by=By.ID,value="kw").send_keys("selenium")
        self.driver.find_element(by=By.ID,value="su").click()
        sleep(2)

        self.driver.switch_to.window(windows[0])
        print(self.driver.current_window_handle)
        self.driver.find_element(by=By.ID,value="kw").send_keys("appium")
        self.driver.find_element(by=By.ID,value="su").click()
        sleep(2)



