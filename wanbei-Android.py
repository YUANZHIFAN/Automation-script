# UTF-8
import self as self
import unittest
import time
from appium.webdriver import webdriver


class MyTestCase(unittest.TestCase):
    desired_caps = desired_caps = {
        'platformName': 'Android',
        'platformVersion': '5.1.1',
        'deviceName': '7N2SQL14CT014460',
        'appPackage': 'com.xingfeiinc.app',
        'appActivity': 'activity.MainActivity'
    }
    self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

    self.driver.hide_keyboard()

    time.sleep(3)

    def click_UserNmame(self):
        el = self.driver.find_element_by_id('com.xingfeiinc.app:id/name')
        el.click()

    def input_UserName(self):
        el = self.driver.find_element_by_id('com.xingfeiinc.app:id/name')
        el.send_keys('17611111111')

    def click_PassWord(self):
        el = self.driver.find_element_by_class('android.widget.EditText')
        el.click()

    def input_PassWordName(self):
        el = self.driver.find_element_by_id('com.xingfeiinc.app:id/name')
        el.send_keys('111111')

    def click_submit(self):
        el = el = self.driver.find_element_by_id('com.xingfeiinc.app:id/login')
        el.click()


if __name__ == '__main__':
    unittest.main()
