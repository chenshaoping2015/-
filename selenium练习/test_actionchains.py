# -*- coding:utf-8 -*-
# @Time  :2021/1/18 14:34
# @Author: stevenchen
from time import sleep

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import pytest
from selenium.webdriver.common.keys import Keys


class TestChains:
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(2)

    def teardown(self):
        self.driver.quit()
    @pytest.mark.skip
    def test_case_click(self):
        self.driver.get("http://sahitest.com/demo/clicks.htm")
        element_dbl_click = self.driver.find_element(by=By.XPATH ,value="//input[@value='dbl click me']")
        element_click = self.driver.find_element(by=By.XPATH ,value="//input[@value='click me']")
        element_rgt_click = self.driver.find_element(by=By.XPATH ,value="//input[@value='right click me']")

        action = ActionChains(self.driver)
        action.click(element_click)
        action.double_click(element_dbl_click)
        action.context_click(element_rgt_click)
        action.perform()

        sleep(4)

    @pytest.mark.skip
    def test_move_to_ele(self):
        self.driver.get("http://www.baidu.com")
        element_setting = self.driver.find_element(by=By.XPATH,value="//*[@id='s-usersetting-top']")
        action = ActionChains(self.driver)
        action.move_to_element(element_setting)
        action.perform()
        sleep(2)

    @pytest.mark.skip
    def test_dragdrop(self):
        self.driver.get("http://sahitest.com/demo/dragDropDataTransfer.htm")
        element_start = self.driver.find_element(by=By.XPATH,value="//*[@id='drag1']")
        element_end = self.driver.find_element(by=By.XPATH,value="//*[@id='div1']")
        action = ActionChains(self.driver)
        action.drag_and_drop(element_start,element_end).perform()   #方法1
        # action.click_and_hold(element_start).release(element_end).perform() #方法2
        # action.click_and_hold(element_start).move_to_element(element_end).release().perform()   #方法3

        sleep(2)

    def test_keys(self):
        self.driver.get("http://sahitest.com/demo/label.htm")
        element_user = self.driver.find_element(by=By.XPATH,value="//input[@type='textbox']")
        element_user.click()
        action = ActionChains(self.driver)
        action.send_keys("username").pause(1)
        action.send_keys(Keys.SPACE).pause(1)
        action.send_keys("tom").pause(1)
        action.send_keys(Keys.BACK_SPACE).perform()
        sleep(2)


