# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class NetwealthOpenAnAccount(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.blazedemo.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_netwealth_open_an_account(self):
        driver = self.driver
        # Label: Test
        # ERROR: Caught exception [ERROR: Unsupported command [resizeWindow | 1920,912 | ]]
        driver.get("https://dev.app.netwealth.com/app/dashboard")
        # ERROR: Caught exception [Error: unknown strategy [shadow] for locator [shadow=nw-root, ng-component, nw-navbar, nw-navbar-menu:nth-of-type(1), li:nth-of-type(1) > a:nth-of-type(1) > span:nth-of-type(1)]]
        # ERROR: Caught exception [Error: unknown strategy [shadow] for locator [shadow=nw-root, div:nth-of-type(1) > ng-component:nth-of-type(1), nw-currencyandgoal, nw-investment-goal, div:nth-of-type(1) > div:nth-of-type(1) > div:nth-of-type(3) > button[type="submit"]]]
        # ERROR: Caught exception [Error: unknown strategy [shadow] for locator [shadow=nw-root, div:nth-of-type(1) > ng-component:nth-of-type(1), nw-portfolio-steps, nw-target-retirement-edit, nw-currency-input, input]]
        # ERROR: Caught exception [Error: unknown strategy [shadow] for locator [shadow=nw-root, div:nth-of-type(1) > ng-component:nth-of-type(1), nw-portfolio-steps, nw-target-retirement-edit, nw-currency-input, input]]
        # ERROR: Caught exception [Error: unknown strategy [shadow] for locator [shadow=nw-root, div:nth-of-type(1) > ng-component:nth-of-type(1), nw-portfolio-steps, nw-target-retirement-edit, nw-percentage-input, input]]
        # ERROR: Caught exception [Error: unknown strategy [shadow] for locator [shadow=nw-root, div:nth-of-type(1) > ng-component:nth-of-type(1), nw-portfolio-steps, nw-target-retirement-edit, nw-percentage-input, input]]
        # ERROR: Caught exception [Error: unknown strategy [shadow] for locator [shadow=nw-root, div:nth-of-type(1) > ng-component:nth-of-type(1), nw-portfolio-steps, nw-target-retirement-edit, div:nth-of-type(3) > nw-years-input:nth-of-type(1), input]]
        # ERROR: Caught exception [Error: unknown strategy [shadow] for locator [shadow=nw-root, div:nth-of-type(1) > ng-component:nth-of-type(1), nw-portfolio-steps, nw-target-retirement-edit, div:nth-of-type(3) > nw-years-input:nth-of-type(1), input]]
        # ERROR: Caught exception [Error: unknown strategy [shadow] for locator [shadow=nw-root, div:nth-of-type(1) > ng-component:nth-of-type(1), nw-portfolio-steps, nw-target-retirement-edit, div:nth-of-type(3) > nw-years-input:nth-of-type(1), input]]
        # ERROR: Caught exception [Error: unknown strategy [shadow] for locator [shadow=nw-root, div:nth-of-type(1) > ng-component:nth-of-type(1), nw-portfolio-steps, nw-target-retirement-edit, div:nth-of-type(4) > nw-years-input:nth-of-type(1), input]]
        # ERROR: Caught exception [Error: unknown strategy [shadow] for locator [shadow=nw-root, div:nth-of-type(1) > ng-component:nth-of-type(1), nw-portfolio-steps, nw-target-retirement-edit, div:nth-of-type(4) > nw-years-input:nth-of-type(1), input]]
        # ERROR: Caught exception [Error: unknown strategy [shadow] for locator [shadow=nw-root, div:nth-of-type(1) > ng-component:nth-of-type(1), nw-portfolio-steps, nw-target-retirement-edit, div:nth-of-type(5) > nw-years-input:nth-of-type(1), input]]
        # ERROR: Caught exception [Error: unknown strategy [shadow] for locator [shadow=nw-root, div:nth-of-type(1) > ng-component:nth-of-type(1), nw-portfolio-steps, nw-target-retirement-edit, div:nth-of-type(5) > nw-years-input:nth-of-type(1), input]]
        # ERROR: Caught exception [Error: unknown strategy [shadow] for locator [shadow=nw-root, div:nth-of-type(1) > ng-component:nth-of-type(1), nw-portfolio-steps, nw-target-retirement-edit, div:nth-of-type(5) > nw-years-input:nth-of-type(1), div:nth-of-type(2) > span:nth-of-type(1)]]
        # ERROR: Caught exception [Error: unknown strategy [shadow] for locator [shadow=nw-root, div:nth-of-type(1) > ng-component:nth-of-type(1), nw-portfolio-steps, nw-target-retirement-edit, button]]
        # ERROR: Caught exception [Error: unknown strategy [shadow] for locator [shadow=nw-root, div:nth-of-type(1) > ng-component:nth-of-type(1), nw-portfolio-steps, nw-account-type-edit, div:nth-of-type(1) > div:nth-of-type(1) > label:nth-of-type(1)]]
        # ERROR: Caught exception [Error: unknown strategy [shadow] for locator [shadow=nw-root, div:nth-of-type(1) > ng-component:nth-of-type(1), nw-portfolio-steps, nw-account-type-edit, select]]
        # ERROR: Caught exception [Error: unknown strategy [shadow] for locator [shadow=nw-root, div:nth-of-type(1) > ng-component:nth-of-type(1), nw-portfolio-steps, nw-account-type-edit, select]]
        # ERROR: Caught exception [Error: unknown strategy [shadow] for locator [shadow=nw-root, div:nth-of-type(1) > ng-component:nth-of-type(1), nw-portfolio-steps, nw-account-type-edit, form:nth-of-type(1) > div:nth-of-type(1) > div:nth-of-type(4)]]
        # ERROR: Caught exception [Error: unknown strategy [shadow] for locator [shadow=nw-root, div:nth-of-type(1) > ng-component:nth-of-type(1), nw-portfolio-steps, nw-account-type-edit, button]]
        # ERROR: Caught exception [Error: unknown strategy [shadow] for locator [shadow=nw-root, div:nth-of-type(1) > ng-component:nth-of-type(1), nw-portfolio-steps, nw-contributions-edit, div:nth-of-type(1) > nw-currency-input:nth-of-type(1), input]]
        # ERROR: Caught exception [Error: unknown strategy [shadow] for locator [shadow=nw-root, div:nth-of-type(1) > ng-component:nth-of-type(1), nw-portfolio-steps, nw-contributions-edit, div:nth-of-type(1) > nw-currency-input:nth-of-type(1), input]]
        # ERROR: Caught exception [Error: unknown strategy [shadow] for locator [shadow=nw-root, div:nth-of-type(1) > ng-component:nth-of-type(1), nw-portfolio-steps, nw-contributions-edit, div:nth-of-type(2) > nw-currency-input:nth-of-type(1), input]]
        # ERROR: Caught exception [Error: unknown strategy [shadow] for locator [shadow=nw-root, div:nth-of-type(1) > ng-component:nth-of-type(1), nw-portfolio-steps, nw-contributions-edit, div:nth-of-type(2) > nw-currency-input:nth-of-type(1), input]]
        # ERROR: Caught exception [Error: unknown strategy [shadow] for locator [shadow=nw-root, div:nth-of-type(1) > ng-component:nth-of-type(1), nw-portfolio-steps, nw-contributions-edit, button]]
        # ERROR: Caught exception [Error: unknown strategy [shadow] for locator [shadow=nw-root, div:nth-of-type(1) > ng-component:nth-of-type(1), nw-portfolio-steps, nw-risk-level-edit, nw-risk-level-input, div:nth-of-type(4)]]
        # ERROR: Caught exception [Error: unknown strategy [shadow] for locator [shadow=nw-root, div:nth-of-type(1) > ng-component:nth-of-type(1), nw-portfolio-steps, nw-risk-level-edit, button]]
    
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
