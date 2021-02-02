# -*- coding:utf-8 -*-
# @Time  :2021/2/1 22:44
# @Author: stevenchen
from auto_testing_prace.pageobject.page.main import Main


class TestRegister:
    def setup(self):
        self.main = Main()

    def test_register(self):
        assert self.main.goto_register().register()