# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class NetwealthLogin(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.blazedemo.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_netwealth_login(self):
        driver = self.driver
        # Label: Test
        # ERROR: Caught exception [ERROR: Unsupported command [resizeWindow | 1920,912 | ]]
        driver.get("https://dev.id.netwealth.com/Account/RegisterCompleted?ReturnUrl=https%3A%2F%2Fdev.netwealth.com%2Flogin")
        driver.find_element_by_link_text("Log In").click()
        driver.find_element_by_id("Password").click()
        driver.find_element_by_id("Password").clear()
        driver.find_element_by_id("Password").send_keys("Akwasi1!")
        driver.find_element_by_css_selector("button.btn.btn-primary").click()
        driver.get("https://dev.app.netwealth.com/app/dashboard")
        # ERROR: Caught exception [Error: unknown strategy [shadow] for locator [shadow=nw-root, ng-component, nw-navbar, nw-navbar-menu:nth-of-type(1), li:nth-of-type(1) > a:nth-of-type(1) > span:nth-of-type(1)]]
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
