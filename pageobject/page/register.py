# -*- coding:utf-8 -*-
# @Time  :2021/2/1 22:28
# @Author: stevenchen
from auto_testing_prace.pageobject.page.base_page import BasePage
from selenium.webdriver.common.by import By


class Register(BasePage):
    def register(self):
        self.find(By.ID,"corp_name").send_keys("自动化测试教程")
        self.find(By.ID,"manager_name").send_keys("chenshaoping")
        return True
