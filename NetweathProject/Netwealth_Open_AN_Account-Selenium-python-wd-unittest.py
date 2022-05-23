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
        driver.get("https://dev.id.netwealth.com/account/login?returnUrl=%2Fconnect%2Fauthorize%2Fcallback%3Fclient_id%3Dumbraco%26redirect_uri%3Dhttps%253A%252F%252Fdev.netwealth.com%26response_type%3Did_token%26scope%3Dopenid%2520profile%2520email%26state%3DOpenIdConnect.AuthenticationProperties%253D3MRoQqBl6oxf7OJkFjr3gp-ewk1zOCK3lzi1lIaHJZ-xF0ynV2gV6wn3WW-wNNeyg5Q3Y1u9vR5D7JdHjHBsjXirA_ja7zBUycxIDRZPZRAG3TBhCU-ePdKVBduYp7uC1oZYW54rbYlvJ0z0GjLtFqF1O_YpwlpQmxcXCRry6r7K43Bby5OGIvAYrLZoy_89rewvWY6SboWR_PpHU_qZ2fiSCZo65INBi9_PB602OINwhicjtY7I_tpPV1f1puFokduDyISwy5ZdyVv0S3n-0b8TFDJ-S846wVAuo1m8SxVzm6laIOXMy8ZTcH2qfpsaAVPSuiKcVgitUuBJHhD30ya5VCqW-QMlxGdGYh3ATqytGJr2MAR01bnCANKmegvaLdUva_oVqK2XsthISx6zP8zfrhbhjsvstYE1l2ISqk97jlJ6jeCXULCBfMkRq387xJiG85s5dM5Fv_8BovATcL4HofeyhLFhOHA8R1G0kEZQEXMqF-10kiMuns-wDgB_f8yDeiDk2Zcw1wP5GeOdZUvG1vu_PW7a5Xjf4eDikEPo1sFh-WnC3RMZ9A_9r9r2jsexkuxXtAhio-_oh6RVikKGvRSjhC9VYIggJHmgKjDxmCGg1hnWcbT5QZRgVdwlFscLPFkWqkTjrFJnrg_Mj8meZaQjj4Z94GuPC8bKVDYHfhAGjXYBemPiYWbUdsXM-fm8fFnoys4Zyg6ceLgvdviT6WYc3s_LJgTlt7JMrzM3gXlb63s38PH_yF8o7dfwwc8P2PJjiDDzLSCeAUQknw%26response_mode%3Dform_post%26nonce%3D637888146140202080.MGUxMWE0MjAtMjkxOS00ODE1LTgwZDAtZWI1ZDIxMGMzOGRiZTc4ZGViMzQtZmJjOC00MDkzLWJhNTEtYWZlODI3MmY3ZGRk%26x-client-SKU%3DID_NET461%26x-client-ver%3D5.3.0.0")
        driver.find_element_by_id("Email").click()
        driver.find_element_by_id("Password").click()
        driver.find_element_by_id("Password").clear()
        driver.find_element_by_id("Password").send_keys("Akwasi1!")
        driver.find_element_by_css_selector("button.btn.btn-primary").click()
        driver.get("https://dev.app.netwealth.com/app/dashboard")
        # ERROR: Caught exception [Error: unknown strategy [shadow] for locator [shadow=nw-root, ng-component, nw-navbar, nw-navbar-menu:nth-of-type(1), li:nth-of-type(1) > a:nth-of-type(1) > span:nth-of-type(1)]]
        # ERROR: Caught exception [Error: unknown strategy [shadow] for locator [shadow=nw-root, div:nth-of-type(1) > ng-component:nth-of-type(1), nw-currencyandgoal, nw-base-currency, div:nth-of-type(2) > label:nth-of-type(1)]]
        # ERROR: Caught exception [Error: unknown strategy [shadow] for locator [shadow=nw-root, div:nth-of-type(1) > ng-component:nth-of-type(1), nw-currencyandgoal, nw-base-currency, div:nth-of-type(3) > label:nth-of-type(1)]]
        # ERROR: Caught exception [Error: unknown strategy [shadow] for locator [shadow=nw-root, div:nth-of-type(1) > ng-component:nth-of-type(1), nw-currencyandgoal, nw-base-currency, div:nth-of-type(1) > label:nth-of-type(1)]]
        # ERROR: Caught exception [Error: unknown strategy [shadow] for locator [shadow=nw-root, div:nth-of-type(1) > ng-component:nth-of-type(1), nw-currencyandgoal, nw-investment-philosophy, div:nth-of-type(2) > label:nth-of-type(1)]]
        # ERROR: Caught exception [Error: unknown strategy [shadow] for locator [shadow=nw-root, div:nth-of-type(1) > ng-component:nth-of-type(1), nw-currencyandgoal, nw-investment-goal, div:nth-of-type(1) > div:nth-of-type(1) > div:nth-of-type(3) > button[type="submit"]]]
        # ERROR: Caught exception [Error: unknown strategy [shadow] for locator [shadow=nw-root, div:nth-of-type(1) > ng-component:nth-of-type(1), nw-portfolio-steps, nw-target-retirement-edit, nw-currency-input, input]]
        # ERROR: Caught exception [Error: unknown strategy [shadow] for locator [shadow=nw-root, div:nth-of-type(1) > ng-component:nth-of-type(1), nw-portfolio-steps, nw-target-retirement-edit, nw-currency-input, input]]
        # ERROR: Caught exception [Error: unknown strategy [shadow] for locator [shadow=nw-root, div:nth-of-type(1) > ng-component:nth-of-type(1), nw-portfolio-steps, nw-target-retirement-edit, nw-percentage-input, input]]
        # ERROR: Caught exception [Error: unknown strategy [shadow] for locator [shadow=nw-root, div:nth-of-type(1) > ng-component:nth-of-type(1), nw-portfolio-steps, nw-target-retirement-edit, nw-percentage-input, input]]
        # ERROR: Caught exception [Error: unknown strategy [shadow] for locator [shadow=nw-root, div:nth-of-type(1) > ng-component:nth-of-type(1), nw-portfolio-steps, nw-target-retirement-edit, div:nth-of-type(3) > nw-years-input:nth-of-type(1), input]]
        # ERROR: Caught exception [Error: unknown strategy [shadow] for locator [shadow=nw-root, div:nth-of-type(1) > ng-component:nth-of-type(1), nw-portfolio-steps, nw-target-retirement-edit, div:nth-of-type(3) > nw-years-input:nth-of-type(1), input]]
        # ERROR: Caught exception [Error: unknown strategy [shadow] for locator [shadow=nw-root, div:nth-of-type(1) > ng-component:nth-of-type(1), nw-portfolio-steps, nw-target-retirement-edit, div:nth-of-type(4) > nw-years-input:nth-of-type(1), input]]
        # ERROR: Caught exception [Error: unknown strategy [shadow] for locator [shadow=nw-root, div:nth-of-type(1) > ng-component:nth-of-type(1), nw-portfolio-steps, nw-target-retirement-edit, div:nth-of-type(4) > nw-years-input:nth-of-type(1), input]]
        # ERROR: Caught exception [Error: unknown strategy [shadow] for locator [shadow=nw-root, div:nth-of-type(1) > ng-component:nth-of-type(1), nw-portfolio-steps, nw-target-retirement-edit, div:nth-of-type(5) > nw-years-input:nth-of-type(1), input]]
        # ERROR: Caught exception [Error: unknown strategy [shadow] for locator [shadow=nw-root, div:nth-of-type(1) > ng-component:nth-of-type(1), nw-portfolio-steps, nw-target-retirement-edit, div:nth-of-type(5) > nw-years-input:nth-of-type(1), input]]
        # ERROR: Caught exception [Error: unknown strategy [shadow] for locator [shadow=nw-root, div:nth-of-type(1) > ng-component:nth-of-type(1), nw-portfolio-steps, nw-target-retirement-edit, div:nth-of-type(5) > nw-years-input:nth-of-type(1), input]]
        # ERROR: Caught exception [Error: unknown strategy [shadow] for locator [shadow=nw-root, div:nth-of-type(1) > ng-component:nth-of-type(1), nw-portfolio-steps, nw-target-retirement-edit, button]]
        # ERROR: Caught exception [Error: unknown strategy [shadow] for locator [shadow=nw-root, div:nth-of-type(1) > ng-component:nth-of-type(1), nw-portfolio-steps, nw-account-type-edit, div:nth-of-type(1) > div:nth-of-type(1) > label:nth-of-type(1)]]
        # ERROR: Caught exception [Error: unknown strategy [shadow] for locator [shadow=nw-root, div:nth-of-type(1) > ng-component:nth-of-type(1), nw-portfolio-steps, nw-account-type-edit, div:nth-of-type(2) > div:nth-of-type(1) > label:nth-of-type(1)]]
        # ERROR: Caught exception [Error: unknown strategy [shadow] for locator [shadow=nw-root, div:nth-of-type(1) > ng-component:nth-of-type(1), nw-portfolio-steps, nw-account-type-edit, div:nth-of-type(3) > div:nth-of-type(1) > label:nth-of-type(1)]]
        # ERROR: Caught exception [Error: unknown strategy [shadow] for locator [shadow=nw-root, div:nth-of-type(1) > ng-component:nth-of-type(1), nw-portfolio-steps, nw-account-type-edit, div:nth-of-type(4) > div:nth-of-type(1) > label:nth-of-type(1)]]
        # ERROR: Caught exception [Error: unknown strategy [shadow] for locator [shadow=nw-root, div:nth-of-type(1) > ng-component:nth-of-type(1), nw-portfolio-steps, nw-account-type-edit, div:nth-of-type(5) > div:nth-of-type(1) > label:nth-of-type(1)]]
        # ERROR: Caught exception [Error: unknown strategy [shadow] for locator [shadow=nw-root, div:nth-of-type(1) > ng-component:nth-of-type(1), nw-portfolio-steps, nw-account-type-edit, div:nth-of-type(1) > div:nth-of-type(1) > label:nth-of-type(1)]]
        # ERROR: Caught exception [Error: unknown strategy [shadow] for locator [shadow=nw-root, div:nth-of-type(1) > ng-component:nth-of-type(1), nw-portfolio-steps, nw-account-type-edit, select]]
        # ERROR: Caught exception [Error: unknown strategy [shadow] for locator [shadow=nw-root, div:nth-of-type(1) > ng-component:nth-of-type(1), nw-portfolio-steps, nw-account-type-edit, select]]
        # ERROR: Caught exception [Error: unknown strategy [shadow] for locator [shadow=nw-root, div:nth-of-type(1) > ng-component:nth-of-type(1), nw-portfolio-steps, nw-account-type-edit, button]]
        # ERROR: Caught exception [Error: unknown strategy [shadow] for locator [shadow=nw-root, div:nth-of-type(1) > ng-component:nth-of-type(1), nw-portfolio-steps, nw-contributions-edit, div:nth-of-type(1) > nw-currency-input:nth-of-type(1), input]]
        # ERROR: Caught exception [Error: unknown strategy [shadow] for locator [shadow=nw-root, div:nth-of-type(1) > ng-component:nth-of-type(1), nw-portfolio-steps, nw-contributions-edit, div:nth-of-type(1) > nw-currency-input:nth-of-type(1), input]]
        # ERROR: Caught exception [Error: unknown strategy [shadow] for locator [shadow=nw-root, div:nth-of-type(1) > ng-component:nth-of-type(1), nw-portfolio-steps, nw-contributions-edit, div:nth-of-type(2) > nw-currency-input:nth-of-type(1), input]]
        # ERROR: Caught exception [Error: unknown strategy [shadow] for locator [shadow=nw-root, div:nth-of-type(1) > ng-component:nth-of-type(1), nw-portfolio-steps, nw-contributions-edit, div:nth-of-type(2) > nw-currency-input:nth-of-type(1), input]]
        # ERROR: Caught exception [Error: unknown strategy [shadow] for locator [shadow=nw-root, div:nth-of-type(1) > ng-component:nth-of-type(1), nw-portfolio-steps, nw-contributions-edit, button]]
        # ERROR: Caught exception [Error: unknown strategy [shadow] for locator [shadow=nw-root, div:nth-of-type(1) > ng-component:nth-of-type(1), nw-portfolio-steps, nw-risk-level-edit, nw-risk-level-input, div:nth-of-type(3)]]
        # ERROR: Caught exception [Error: unknown strategy [shadow] for locator [shadow=nw-root, div:nth-of-type(1) > ng-component:nth-of-type(1), nw-portfolio-steps, nw-risk-level-edit, button]]
        # ERROR: Caught exception [Error: unknown strategy [shadow] for locator [shadow=nw-root, div:nth-of-type(1) > ng-component:nth-of-type(1), nw-portfolio-steps, nw-projection-results, nw-asset-composition-table-modal, button]]
        # ERROR: Caught exception [Error: unknown strategy [shadow] for locator [shadow=ngb-modal-window, button[type="button"] > span:nth-of-type(1)]]
        # ERROR: Caught exception [Error: unknown strategy [shadow] for locator [shadow=nw-root, header:nth-of-type(1) > ng-component:nth-of-type(1), nw-navbar, nw-navbar-menu:nth-of-type(2), nw-navbar-megamenu, nw-log-off-menu-item, h5]]
        driver.get("https://dev.netwealth.com/")
    
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
