# -*- coding:utf-8 -*-
# @Time  :2021/2/1 22:36
# @Author: stevenchen
from auto_testing_prace.pageobject.page.base_page import BasePage
from selenium.webdriver.common.by import By

from auto_testing_prace.pageobject.page.register import Register


class Login(BasePage):
    def scan(self):
        pass

    def goto_register(self):
        self.find(By.CSS_SELECTOR,".login_registerBar_link").click()
        return Register(self.driver)