# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class NetwealthRegister(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.blazedemo.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_netwealth_register(self):
        driver = self.driver
        # Label: Test
        # ERROR: Caught exception [ERROR: Unsupported command [resizeWindow | 1920,912 | ]]
        driver.get("https://dev.id.netwealth.com/account/register?returnUrl=https://dev.netwealth.com/login")
        driver.find_element_by_id("FirstName").click()
        driver.find_element_by_id("FirstName").clear()
        driver.find_element_by_id("FirstName").send_keys("Philip")
        driver.find_element_by_id("LastName").click()
        driver.find_element_by_id("LastName").clear()
        driver.find_element_by_id("LastName").send_keys("Debrah")
        driver.find_element_by_id("Email").click()
        driver.find_element_by_id("Email").clear()
        driver.find_element_by_id("Email").send_keys("Pdebrah32@yahoo.com")
        driver.find_element_by_id("Email").click()
        driver.find_element_by_id("Email").clear()
        driver.find_element_by_id("Email").send_keys("phildebrah32@gmail.com")
        driver.find_element_by_id("Password").click()
        driver.find_element_by_id("Password").clear()
        driver.find_element_by_id("Password").send_keys("Akwasi1!")
        driver.find_element_by_id("ReferralSource").click()
        Select(driver.find_element_by_id("ReferralSource")).select_by_visible_text("Newspaper Advert")
        driver.find_element_by_id("HasOptedOutOfMarketingMaterial").click()
        driver.find_element_by_name("RegistrationForm").click()
    
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
