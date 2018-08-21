#!/usr/bin/env python
# -- coding: utf-8 --
from selenium import webdriver
import unittest
import time

class Wanbei( unittest.TestCase ):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait( 30 )
        self.base_url = "http://www.test.gc.xf.io/"
        

    def test_login(self):
        driver = self.driver
        driver.get( self.base_url )
        self.driver.set_window_size( 1920, 1080 )
        #登录
        self.driver.find_element_by_xpath('//*[@id="__layout"]/section/header/div/div[3]/button[2]').click()
        self.driver.find_element_by_name('username').send_keys("17607902616")
        time.sleep(1)
        self.driver.find_element_by_name('password').send_keys("111111")
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="__layout"]/section/div/div/div/div[4]/a').click()
        time.sleep(1)
        username = self.driver.find_element_by_xpath('//*[@id="__layout"]/section/header/div/div[2]/div/div[1]/span').text
        self.assertEqual(username, '@Wy7464', '用户名显示失败')

    def tearDown(self):
        self.driver.quit()
        

if __name__ == "__main__":
    unittest.main()
