# -*- coding:utf-8 -*-
# @Time  :2021/2/1 17:45
# @Author: stevenchen
from auto_testing_prace.pageobject.page.base_page import BasePage
from selenium.webdriver.common.by import By

from auto_testing_prace.pageobject.page.login import Login
from auto_testing_prace.pageobject.page.register import Register


class Main(BasePage):

    base_url = "https://work.weixin.qq.com/"

    def goto_register(self):
        self.find(By.CSS_SELECTOR,".index_head_info_pCDownloadBtn").click()
        return Register(self.driver)

    def goto_login(self):
        self.find(By.CSS_SELECTOR,".index_top_operation_loginBtn").click()
        return Login(self.driver)
